"""Nail the CORRECTED critique without overcorrecting. Two checks:
(1) debias 3.77 with a CI from lattice anchors (not a point estimate).
(2) is the ~0.4d 'signal over null' real, or does it vanish vs a null matched on
    connectivity too (their graph is 4 comps; a connected swap-null isn't matched)?
    Build a 4-component degree-matched null and a fully-random-4-comp null."""
import numpy as np, networkx as nx, os
from numpy.linalg import eigvalsh
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R); np.fill_diagonal(W,0); Gt=nx.from_numpy_array((W>0).astype(int))
def idos(Wsub):
    L=np.diag(Wsub.sum(1))-Wsub; nz=np.sort(eigvalsh(L)); nz=nz[nz>1e-8]
    if len(nz)<10: return np.nan
    a,b=int(0.22*len(nz)),int(0.55*len(nz))
    x,y=np.log10(nz[a:b]),np.log10(np.arange(1,len(nz)+1)[a:b])
    return 2*np.linalg.lstsq(np.vstack([x,np.ones_like(x)]).T,y,rcond=None)[0][0]
def Af(g): return nx.to_numpy_array(g)

# lattice anchors (several seeds/sizes for a CI on the calibration)
anchors={1:[],2:[],3:[]}
for L in [(140,),(150,),(160,)]: anchors[1].append(idos(Af(nx.cycle_graph(L[0]))))
for L in [(11,11),(12,12),(13,13)]: anchors[2].append(idos(Af(nx.grid_graph(list(L),periodic=True))))
for L in [(5,5,6),(5,6,5),(4,5,7)]: anchors[3].append(idos(Af(nx.grid_graph(list(L),periodic=True))))
a1,a2,a3=[np.mean(anchors[d]) for d in (1,2,3)]
print(f"lattice anchors IDOS: 1D={a1:.2f} 2D={a2:.2f} 3D={a3:.2f}")
def debias(v):
    if v<a2: return 1+(v-a1)/(a2-a1)
    return 2+(v-a2)/(a3-a2)
their=idos(W)
print(f"their graph IDOS={their:.2f}  -> DEBIASED effective-d = {debias(their):.2f}\n")

# nulls, increasingly matched to their graph
Egraph=Gt.number_of_edges(); deg=[d for _,d in Gt.degree()]
def swap_null(seed):
    H=Gt.copy()
    try: nx.double_edge_swap(H,nswap=5*Egraph,max_tries=200*Egraph,seed=seed)
    except nx.NetworkXError: pass
    return H
def comp_matched_null(seed):
    # rewire WITHIN each component: preserves 4-component structure + per-comp degrees
    r=np.random.default_rng(seed); H=nx.Graph()
    for c in nx.connected_components(Gt):
        sub=Gt.subgraph(c).copy()
        try: nx.double_edge_swap(sub,nswap=5*sub.number_of_edges(),max_tries=500*sub.number_of_edges(),seed=int(r.integers(1e9)))
        except nx.NetworkXError: pass
        H=nx.union(H,sub) if H.number_of_nodes() else sub
    return H
sw=[idos(Af(swap_null(s))) for s in range(20)]
cm=[idos(Af(comp_matched_null(s))) for s in range(20)]
print(f"connected swap-null (degree-matched, C=1):     IDOS {np.mean(sw):.2f}±{np.std(sw):.2f} -> debiased {debias(np.mean(sw)):.2f}")
print(f"component-matched null (degree+4comps matched): IDOS {np.mean(cm):.2f}±{np.std(cm):.2f} -> debiased {debias(np.mean(cm)):.2f}")
print(f"\ntheir debiased {debias(their):.2f} vs component-matched-null debiased {debias(np.mean(cm)):.2f}")
gap=debias(their)-debias(np.mean(cm))
print(f"  SIGNAL over the properly-matched null = {gap:+.2f} effective dimensions")
z=(their-np.mean(cm))/np.std(cm)
print(f"  z vs component-matched null = {z:+.2f}")
print(f"  => {'real but small structural signal' if abs(z)>2 else 'NOT distinguishable from the matched null'}")
