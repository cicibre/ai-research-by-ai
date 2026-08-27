"""
Re-derive handoff.md on two rulers. Model = handoff §9 (fully specified).
Their estimator = IDOS/Weyl slope. Honest estimator = heat-kernel return prob
(normalized Laplacian, giant component) + N-companion.
PRE-REG: P1 IDOS null ~2.5-2.8 on no-geometry; P2 d tracks K (rank leak);
         P3 on honest ruler + N-companion, 3.77 does not stay flat.
"""
import numpy as np, networkx as nx
from numpy.linalg import eigvalsh

def run(N, K, T=200, k=6, eps=.15, gamma=.10, delta=.01, noise=.05, flip=.03, seed=0):
    r = np.random.default_rng(seed)
    S = r.choice([-1,1], (N,K)).astype(float); R = np.zeros((N,N))
    for t in range(T):
        sim = (S @ S.T)/K
        dR = eps*sim + gamma*np.tanh((R @ R)/N) + r.normal(0, noise, (N,N))
        R = np.tanh((1-delta)*R + dR)
        absR = np.abs(R); np.fill_diagonal(absR, -np.inf)
        kth = np.partition(absR, N-k, axis=1)[:, N-k]
        R = np.where(absR >= kth[:,None], R, 0.0)
        R = np.where(R*R.T != 0, (R+R.T)/2, 0.0)          # mutual agreement
        if t % 10 == 0:
            field = R @ S; fl = r.random((N,K)) < flip
            newS = np.sign(field); newS = np.where(newS==0, S, newS)
            S = np.where(fl, newS, S)
    return R, S

def d_idos(W, lo, hi):
    W = W.copy(); np.fill_diagonal(W, 0)
    L = np.diag(W.sum(1)) - W
    ev = np.sort(eigvalsh(L)); nz = ev[ev > 1e-8]
    if len(nz) < 12: return np.nan
    Nl = np.arange(1, len(nz)+1)
    a, b = int(lo*len(nz)), max(int(hi*len(nz)), int(lo*len(nz))+5)
    x, y = np.log10(nz[a:b]), np.log10(Nl[a:b])
    A = np.vstack([x, np.ones_like(x)]).T
    slope = np.linalg.lstsq(A, y, rcond=None)[0][0]
    return 2*slope

def d_heat(W):
    W = np.abs(W).copy(); np.fill_diagonal(W, 0)
    G = nx.from_numpy_array(W)
    if G.number_of_edges()==0: return np.nan, 0, 0
    comps = list(nx.connected_components(G)); ncomp = len(comps)
    giant = sorted(max(comps, key=len)); W = W[np.ix_(giant, giant)]
    deg = W.sum(1); n = len(deg)
    if n < 20: return np.nan, ncomp, n
    Dm = np.diag(1/np.sqrt(deg)); Ln = np.eye(n) - Dm @ W @ Dm
    lam = np.clip(np.sort(eigvalsh(Ln)), 0, 2)
    ts = np.geomspace(1.0, 2.0/max(lam[1],1e-6), 40)
    P = np.array([np.mean(np.exp(-lam*t)) for t in ts])
    ds_t = -2*np.gradient(np.log(P), np.log(ts))
    return float(np.median(ds_t[10:32])), ncomp, n

def W_from_R(R): W=np.abs(R).copy(); np.fill_diagonal(W,0); return W
def config_null(W, seed=1):
    G = nx.from_numpy_array((W>0).astype(int)); deg=[d for _,d in G.degree()]
    H = nx.Graph(nx.configuration_model(deg, seed=seed)); H.remove_edges_from(nx.selfloop_edges(H))
    return nx.to_numpy_array(H)
def torus(dim,L): return nx.to_numpy_array(nx.grid_graph([L]*dim, periodic=True))

# ---- calibrate IDOS window to reproduce their published validation (2D~2.16) ----
tor2 = torus(2,28)
best = min([(round(lo,2),round(hi,2)) for lo in [0,.02,.05] for hi in [.2,.3,.4,.5]],
           key=lambda w: abs(d_idos(tor2,*w)-2.16))
LO,HI = best
print(f"=== IDOS window calibrated to their 2D validation: lo={LO} hi={HI} -> 2D d={d_idos(tor2,LO,HI):.2f} (theirs 2.16) ===\n")

print("=== ESTIMATOR VALIDATION (known answers) ===")
print(f"{'graph':20s} {'IDOS':>7} {'heat':>7}   (theirs: 1D 1.16 / 2D 2.16 / null 2.81)")
for name,W in [("1D ring 800", nx.to_numpy_array(nx.cycle_graph(800))),
               ("2D torus 28x28", tor2), ("3D torus 9x9x9", torus(3,9)),
               ("ER random <k>=6", nx.to_numpy_array(nx.gnm_random_graph(800,2400,seed=7)))]:
    dh,_,_ = d_heat(W)
    print(f"{name:20s} {d_idos(W,LO,HI):>7.2f} {dh:>7.2f}")
print("  KEY: does IDOS separate 2D-torus from ER-random? heat does (2.1 vs 3.6+)\n")

print("=== REPRODUCE handoff (N=150,K=3) on their IDOS ===")
R,_ = run(150,3,seed=7); W=W_from_R(R)
print(f"  model IDOS d = {d_idos(W,LO,HI):.2f}   config-null IDOS d = {d_idos(config_null(W),LO,HI):.2f}   [handoff 3.77 vs 2.81]\n")

print("=== P2  does dimension track distinction-rank K? ===")
print(f"{'K':>2} {'IDOS':>6} {'null':>6} {'gap':>6} | {'heat':>6} {'#comp':>6} {'giantN':>6}")
for K in [1,2,3,4,5]:
    R,_=run(150,K,seed=7); W=W_from_R(R); dh,nc,gn=d_heat(W)
    di=d_idos(W,LO,HI); dn=d_idos(config_null(W),LO,HI)
    print(f"{K:>2} {di:>6.2f} {dn:>6.2f} {di-dn:>6.2f} | {dh:>6.2f} {nc:>6} {gn:>6}")
print("  P2 holds if IDOS d / gap grows with K = rank of S leaking into spectrum\n")

print("=== P3  N-companion (K=3): flat across N? ===")
print(f"{'N':>5} {'IDOS':>6} {'null':>6} | {'heat':>6} {'#comp':>6} {'giantN':>6}")
iser,hser=[],[]
for N in [150,300,600]:
    R,_=run(N,3,seed=7); W=W_from_R(R); dh,nc,gn=d_heat(W)
    di=d_idos(W,LO,HI); dn=d_idos(config_null(W),LO,HI); iser.append(di); hser.append(dh)
    print(f"{N:>5} {di:>6.2f} {dn:>6.2f} | {dh:>6.2f} {nc:>6} {gn:>6}")
print(f"\n  IDOS across N = {[round(v,2) for v in iser]} drift {iser[-1]-iser[0]:+.2f}")
print(f"  heat across N = {[round(v,2) for v in hser]} drift {hser[-1]-hser[0]:+.2f}")
