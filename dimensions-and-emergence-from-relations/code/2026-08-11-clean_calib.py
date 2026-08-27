"""CORRECTION run. My '4.38 for 1D' fed a degree-6 Watts-Strogatz and mislabeled it
1D. Do a CLEAN, consistent calibration: lattices of known dimension AT MATCHED SCALE,
one fixed window rule for all. Then locate their graph honestly among them + the
degree-matched null. Report both estimators. Let the data set the real critique."""
import numpy as np, networkx as nx, os
from numpy.linalg import eigvalsh
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R); np.fill_diagonal(W,0); Gtheir=nx.from_numpy_array((W>0).astype(int))

# ONE fixed window rule for every graph: their fractional band 32/146..81/146 ~ [0.22,0.55]
def idos(Wsub):
    L=np.diag(Wsub.sum(1))-Wsub; nz=np.sort(eigvalsh(L)); nz=nz[nz>1e-8]
    if len(nz)<10: return np.nan
    a,b=int(0.22*len(nz)),int(0.55*len(nz))
    x,y=np.log10(nz[a:b]),np.log10(np.arange(1,len(nz)+1)[a:b])
    return 2*np.linalg.lstsq(np.vstack([x,np.ones_like(x)]).T,y,rcond=None)[0][0]
def heat(Wsub):
    Wsub=np.abs(Wsub).copy(); np.fill_diagonal(Wsub,0); g=nx.from_numpy_array(Wsub)
    if g.number_of_edges()==0: return np.nan
    gi=sorted(max(nx.connected_components(g),key=len)); Wg=Wsub[np.ix_(gi,gi)]
    deg=Wg.sum(1); n=len(deg)
    if n<20: return np.nan
    Dm=np.diag(1/np.sqrt(deg)); lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@Wg@Dm)),0,2)
    ts=np.geomspace(1.0,20.0,40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])  # FIXED window
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32]))
def A(g): return nx.to_numpy_array(g)

print(f"{'graph':34s} {'deg':>4} {'true-d':>6} {'IDOS':>6} {'heat':>6}")
# CLEAN lattices at ~their scale (N~150), degrees 2/4/6/8
rows=[
 ("1D ring N150 (deg2)",              A(nx.cycle_graph(150)),           2, 1),
 ("2D torus 12x12 (deg4)",            A(nx.grid_graph([12,12],periodic=True)), 4, 2),
 ("3D torus 5x5x6 (deg6)",            A(nx.grid_graph([5,5,6],periodic=True)),  6, 3),
 ("4D torus 3x3x4x4 (deg8)",          A(nx.grid_graph([3,3,4,4],periodic=True)),8, 4),
]
for name,Wr,dg,td in rows: print(f"{name:34s} {dg:>4} {td:>6} {idos(Wr):>6.2f} {heat(Wr):>6.2f}")
print(f"  -> does IDOS ORDER the clean lattices 1<2<3<4? (my earlier '4.38 1D' was a deg-6 small-world, mislabeled)\n")

# their graph + a degree-matched no-geometry null + a deg-6 clean 3D lattice
their=idos(W); heat_their=heat(W)
Hnull=G=nx.double_edge_swap(Gtheir.copy(),nswap=5*Gtheir.number_of_edges(),max_tries=200*Gtheir.number_of_edges(),seed=1) if False else None
# swap null (exact degree)
Hs=Gtheir.copy()
try: nx.double_edge_swap(Hs,nswap=5*Gtheir.number_of_edges(),max_tries=200*Gtheir.number_of_edges(),seed=1)
except nx.NetworkXError: pass
print(f"{'their experimental graph':34s} {6:>4} {'?':>6} {their:>6.2f} {heat_their:>6.2f}")
print(f"{'their degree-matched swap-null':34s} {6:>4} {'none':>6} {idos(A(Hs)):>6.2f} {heat(A(Hs)):>6.2f}")
t3=A(nx.grid_graph([5,5,6],periodic=True))
print(f"{'clean 3D torus deg6 (ref)':34s} {6:>4} {3:>6} {idos(t3):>6.2f} {heat(t3):>6.2f}")
print(f"\nHONEST QUESTION: is their {their:.2f} closer to the deg-matched NULL or to the true-3D lattice,")
print(f"  on the estimator AND on the validated heat ruler? That is the real, corrected test.")
print(f"  clustering: their={nx.average_clustering(Gtheir):.3f}  null={nx.average_clustering(Hs):.3f}")
