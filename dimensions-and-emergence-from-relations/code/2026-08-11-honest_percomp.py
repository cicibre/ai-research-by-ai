"""Fair test after my pooling-hypothesis DIED: each ~40-node component reads d~3.7 on
their IDOS. Is that a dimension, or does IDOS over-read clustered blobs?
Test: measure their components on BOTH rulers, against size-matched references of
KNOWN dimension (2D grid, 3D grid, random-geometric=real 2D, ER=no geometry)."""
import numpy as np, networkx as nx, os
from numpy.linalg import eigvalsh
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R).copy(); np.fill_diagonal(W,0); G=nx.from_numpy_array((W>0).astype(int))

def idos(Wsub):
    L=np.diag(Wsub.sum(1))-Wsub; nz=np.sort(eigvalsh(L)); nz=nz[nz>1e-8]
    if len(nz)<8: return np.nan
    a=max(int(0.22*len(nz)),2); b=max(int(0.55*len(nz)),a+4)
    x,y=np.log10(nz[a:b]),np.log10(np.arange(1,len(nz)+1)[a:b])
    return 2*np.linalg.lstsq(np.vstack([x,np.ones_like(x)]).T,y,rcond=None)[0][0]

def heat(Wsub):
    Wsub=np.abs(Wsub).copy(); np.fill_diagonal(Wsub,0)
    g=nx.from_numpy_array(Wsub); giant=sorted(max(nx.connected_components(g),key=len))
    Wg=Wsub[np.ix_(giant,giant)]; deg=Wg.sum(1); n=len(deg)
    if n<20: return np.nan,np.nan
    Dm=np.diag(1/np.sqrt(deg)); lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@Wg@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    dst=-2*np.gradient(np.log(P),np.log(ts))
    return float(np.median(dst[10:32])), float(dst[31]-dst[10])

def clust(Wsub):
    return nx.average_clustering(nx.from_numpy_array((np.abs(Wsub)>0).astype(int)))

print(f"{'graph (N~40)':28s} {'IDOS d':>7} {'heat d':>7} {'climb':>6} {'clust':>6}")
# their 4 components
comps=sorted(nx.connected_components(G),key=len,reverse=True)
for i,c in enumerate(comps):
    idx=sorted(c); Wc=W[np.ix_(idx,idx)]; h,cl=heat(Wc)
    print(f"{'their comp '+str(i)+' (N='+str(len(c))+')':28s} {idos(Wc):>7.2f} {h:>7.2f} {cl:>+6.2f} {clust(Wc):>6.2f}")
print()
# size-matched references of KNOWN dimension
def A(g): return nx.to_numpy_array(g)
refs=[
 ("2D grid 6x6 (d=2)", A(nx.grid_graph([6,6]))),
 ("3D grid 3x3x4 (d=3)", A(nx.grid_graph([3,3,4]))),
 ("rand-geometric N40 (real 2D)", A(nx.random_geometric_graph(40,0.33,seed=3))),
 ("ER random N40 m~120 (no geom)", A(nx.gnm_random_graph(40,120,seed=3))),
 ("Watts-Strogatz N40 k6 p.1 (clustered,1D)", A(nx.watts_strogatz_graph(40,6,0.1,seed=3))),
]
for name,Wr in refs:
    h,cl=heat(Wr)
    print(f"{name:28s} {idos(Wr):>7.2f} {h:>7.2f} {cl:>+6.2f} {clust(Wr):>6.2f}")
print("\nread: IDOS 'd' vs the honest ruler + the KNOWN dimension of each reference.")
print("if their comp IDOS~3.7 but honest-d and known-refs say otherwise, IDOS is over-reading, not measuring dimension.")
