"""Re-anchor + confound tests, per advisor.
1. Find a single IDOS window reproducing their lattice anchors 1D=1.16, 2D=2.16.
2. On it, reproduce their model/null anchor (3.77 / 2.81)?  + test shape null>2D.
3. Confound A: is fragmentation T-dependent? (T=50/200/500/1000)
4. Confound B: heat-climb vs a 2D torus measured at the SAME small giant sizes.
"""
import numpy as np, networkx as nx
from numpy.linalg import eigvalsh

def run(N,K,T=200,k=6,eps=.15,gamma=.10,delta=.01,noise=.05,flip=.03,seed=0):
    r=np.random.default_rng(seed); S=r.choice([-1,1],(N,K)).astype(float); R=np.zeros((N,N))
    for t in range(T):
        dR=eps*(S@S.T)/K + gamma*np.tanh((R@R)/N) + r.normal(0,noise,(N,N))
        R=np.tanh((1-delta)*R+dR)
        absR=np.abs(R); np.fill_diagonal(absR,-np.inf)
        kth=np.partition(absR,N-k,axis=1)[:,N-k]
        R=np.where(absR>=kth[:,None],R,0.0); R=np.where(R*R.T!=0,(R+R.T)/2,0.0)
        if t%10==0:
            field=R@S; fl=r.random((N,K))<flip; nS=np.sign(field); nS=np.where(nS==0,S,nS); S=np.where(fl,nS,S)
    return R,S

def d_idos(W,lo,hi):
    W=W.copy(); np.fill_diagonal(W,0); L=np.diag(W.sum(1))-W
    nz=np.sort(eigvalsh(L)); nz=nz[nz>1e-8]
    if len(nz)<12: return np.nan
    Nl=np.arange(1,len(nz)+1); a,b=int(lo*len(nz)),max(int(hi*len(nz)),int(lo*len(nz))+5)
    x,y=np.log10(nz[a:b]),np.log10(Nl[a:b])
    return 2*np.linalg.lstsq(np.vstack([x,np.ones_like(x)]).T,y,rcond=None)[0][0]

def d_heat(W):
    W=np.abs(W).copy(); np.fill_diagonal(W,0); G=nx.from_numpy_array(W)
    if G.number_of_edges()==0: return np.nan,0,0
    comps=list(nx.connected_components(G)); giant=sorted(max(comps,key=len)); W=W[np.ix_(giant,giant)]
    deg=W.sum(1); n=len(deg)
    if n<20: return np.nan,len(comps),n
    Dm=np.diag(1/np.sqrt(deg)); lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32])),len(comps),n

def cfg_null(W,seed=1):
    G=nx.from_numpy_array((np.abs(W)>0).astype(int)); H=nx.Graph(nx.configuration_model([d for _,d in G.degree()],seed=seed))
    H.remove_edges_from(nx.selfloop_edges(H)); return nx.to_numpy_array(H)
def ring(n): return nx.to_numpy_array(nx.cycle_graph(n))
def grid2(L): return nx.to_numpy_array(nx.grid_graph([L,L],periodic=True))

# ---- 1. window search: reproduce 1D=1.16 AND 2D=2.16 simultaneously ----
R1=ring(150); G2=grid2(20)  # sizes unspecified in handoff; ~model scale
print("=== window search: target 1D-ring=1.16, 2D-grid=2.16 ===")
grid=[(round(lo,2),round(hi,2)) for lo in [0,.02,.05,.1,.15] for hi in [.2,.3,.4,.5,.6,.8]]
scored=sorted(grid,key=lambda w:(d_idos(R1,*w)-1.16)**2+(d_idos(G2,*w)-2.16)**2)
for w in scored[:3]:
    print(f"  lo={w[0]} hi={w[1]}:  1D={d_idos(R1,*w):.2f}  2D={d_idos(G2,*w):.2f}")
LO,HI=scored[0]
print(f"  -> using lo={LO} hi={HI}\n")

# ---- 2. reproduce their model/null anchor on the anchored window ----
print("=== 2. reproduce handoff anchor (N=150,K=3) on anchored window ===")
R,_=run(150,3,seed=7); W=np.abs(R); np.fill_diagonal(W,0)
dm=d_idos(W,LO,HI); dn=d_idos(cfg_null(W),LO,HI); d2=d_idos(G2,LO,HI)
print(f"  model d={dm:.2f}  config-null d={dn:.2f}   [handoff: 3.77 / 2.81]")
print(f"  shape check: is config-null({dn:.2f}) > 2D-lattice({d2:.2f})?  {'YES — estimator inflates random>geometry' if dn>d2 else 'no'}")
print(f"  reproduced their anchor? {'~yes' if abs(dm-3.77)<0.6 and abs(dn-2.81)<0.6 else 'NO — my graph != their graph; discrepancy is in model/impl, not just ruler'}\n")

# ---- 3. confound A: is fragmentation T-dependent? ----
print("=== 3. fragmentation vs T (N=150,K=3) ===")
print(f"{'T':>6} {'#comp':>6} {'giantN':>7}")
for T in [50,200,500,1000]:
    R,_=run(150,3,T=T,seed=7); _,nc,gn=d_heat(np.abs(R))
    print(f"{T:>6} {nc:>6} {gn:>7}")
print()

# ---- 4. confound B: heat-climb vs 2D torus at the SAME small giant sizes ----
print("=== 4. heat d: model vs 2D-torus control at matched small N ===")
print(f"{'N':>5} {'model heat':>11} {'giantN':>7} | {'torus heat @giantN':>18}")
for N in [150,300,600]:
    R,_=run(N,3,seed=7); dh,nc,gn=d_heat(np.abs(R))
    L=max(int(round(gn**.5)),4); dt,_,_=d_heat(grid2(L))  # torus with ~gn nodes
    print(f"{N:>5} {dh:>11.2f} {gn:>7} | {dt:>18.2f}  (torus N={L*L})")
print("  if torus climbs the same way, the model's climb is finite-size recovery, not expander.")
