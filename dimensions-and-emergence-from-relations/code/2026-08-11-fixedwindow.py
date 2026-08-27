"""Advisor catch: my climb-sign may be a t-window artifact (tmax set per-graph from
lam[1]: poor mixers overrun to saturation=neg climb, fast mixers don't=pos climb).
Re-test with a FIXED t-window identical for every graph. If signs still separate
geometric from random, the finding holds; if they collapse/flip, it was placement."""
import numpy as np, networkx as nx, os
from numpy.linalg import eigvalsh
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R).copy(); np.fill_diagonal(W,0); G=nx.from_numpy_array((W>0).astype(int))

def heat_fixed(Wsub, tmax):
    Wsub=np.abs(Wsub).copy(); np.fill_diagonal(Wsub,0)
    g=nx.from_numpy_array(Wsub); giant=sorted(max(nx.connected_components(g),key=len))
    Wg=Wsub[np.ix_(giant,giant)]; deg=Wg.sum(1); n=len(deg)
    if n<20: return np.nan,np.nan
    Dm=np.diag(1/np.sqrt(deg)); lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@Wg@Dm)),0,2)
    ts=np.geomspace(1.0, tmax, 40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    dst=-2*np.gradient(np.log(P),np.log(ts))
    return float(np.median(dst[10:32])), float(dst[31]-dst[10])

def A(g): return nx.to_numpy_array(g)
rows=[("their comp "+str(i),W[np.ix_(sorted(c),sorted(c))])
      for i,c in enumerate(sorted(nx.connected_components(G),key=len,reverse=True))]
rows+=[("2D grid 6x6 (d2)",A(nx.grid_graph([6,6]))),
       ("3D grid 3x3x4 (d3)",A(nx.grid_graph([3,3,4]))),
       ("rand-geom N40 (real2D)",A(nx.random_geometric_graph(40,0.33,seed=3))),
       ("ER random N40 (nogeo)",A(nx.gnm_random_graph(40,120,seed=3))),
       ("WattsStrogatz N40 (1D)",A(nx.watts_strogatz_graph(40,6,0.1,seed=3)))]
for TMAX in [20, 50, 100]:
    print(f"=== FIXED t-window [1, {TMAX}] identical for all graphs ===")
    print(f"{'graph':26s} {'heat d':>7} {'climb':>7}")
    for name,Wr in rows:
        d,c=heat_fixed(Wr,TMAX)
        print(f"{name:26s} {d:>7.2f} {c:>+7.2f}")
    print()
