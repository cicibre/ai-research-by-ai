"""Measure THEIR actual R_experimental.npy — no reconstruction. Referent object."""
import numpy as np, networkx as nx
from numpy.linalg import eigvalsh
import os
D=os.path.expanduser("~/Downloads")
R=np.load(f"{D}/R_experimental.npy"); S=np.load(f"{D}/S_experimental.npy")
print(f"R shape {R.shape}  S shape {S.shape}")
W=np.abs(R).copy(); np.fill_diagonal(W,0)
A=(W>0).astype(int)
G=nx.from_numpy_array(A)
comps=sorted([len(c) for c in nx.connected_components(G)],reverse=True)
print(f"edges={G.number_of_edges()} (theirs 448)  <k>={2*G.number_of_edges()/150:.2f}")
print(f"components={len(comps)}  sizes(top5)={comps[:5]}  CONNECTED={nx.is_connected(G)}")

# ---- their estimator, their EXACT scaling region: eigenvalue ranks 32..81 ----
L=np.diag(W.sum(1))-W
ev=np.sort(eigvalsh(L)); nz=ev[ev>1e-8]
print(f"\nnonzero eigenvalues={len(nz)}  top5={np.round(ev[-5:],3)} (theirs top5 [4.04,4.02,4.01,4.01,2.76])")
def idos_rank(nz,a,b):
    Nl=np.arange(1,len(nz)+1); x,y=np.log10(nz[a:b]),np.log10(Nl[a:b])
    A_=np.vstack([x,np.ones_like(x)]).T; sl=np.linalg.lstsq(A_,y,rcond=None)[0][0]
    pred=A_@np.linalg.lstsq(A_,y,rcond=None)[0]; r2=1-np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
    return 2*sl,r2
d,r2=idos_rank(nz,31,81)   # ranks 32..81 (1-indexed) = idx 31..81
print(f"\ntheir estimator, their window (ranks 32-81): d={d:.3f} r2={r2:.3f}   [handoff 3.765, r2 0.996]")

# ---- honest ruler on their actual giant component ----
giant=sorted(max(nx.connected_components(G),key=len)); Wg=W[np.ix_(giant,giant)]
deg=Wg.sum(1); n=len(deg); Dm=np.diag(1/np.sqrt(deg))
lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@Wg@Dm)),0,2)
ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
dst=-2*np.gradient(np.log(P),np.log(ts))
print(f"honest heat-kernel d (giant N={n}): median={np.median(dst[10:32]):.2f}  climb(t)={dst[31]-dst[10]:+.2f}")

# ---- the inference check on THEIR graph: null vs 2D, measured their way ----
def cfg(A_,seed=1):
    g=nx.from_numpy_array(A_); H=nx.Graph(nx.configuration_model([d for _,d in g.degree()],seed=seed))
    H.remove_edges_from(nx.selfloop_edges(H)); return nx.to_numpy_array(H)
def er(A_,seed=1):
    g=nx.from_numpy_array(A_); H=nx.gnm_random_graph(g.number_of_nodes(),g.number_of_edges(),seed=seed); return nx.to_numpy_array(H)
def idos_of(Adj):
    Wl=Adj.astype(float); L=np.diag(Wl.sum(1))-Wl; e=np.sort(eigvalsh(L)); z=e[e>1e-8]
    return idos_rank(z,31,81)[0] if len(z)>81 else np.nan
print(f"\ninference check (their estimator, ranks 32-81):")
print(f"  model d={d:.2f}   config-null d={idos_of(cfg(A)):.2f}   ER-null d={idos_of(er(A)):.2f}   [handoff 2.81/2.50]")
# 1D/2D calibration their way
r1=nx.to_numpy_array(nx.cycle_graph(150)); g2=nx.to_numpy_array(nx.grid_graph([13,12],periodic=False))
print(f"  1D-ring d={idos_of(r1):.2f} [handoff 1.16]   2D-grid d={idos_of(g2):.2f} [handoff 2.16]")
print(f"  --> is config-null > 2D-grid on their own estimator?  {'YES (inference invalid)' if idos_of(cfg(A))>idos_of(g2) else 'NO'}")
