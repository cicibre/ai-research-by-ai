"""Does d=3.77 live IN the structure, or is it a pooling artifact of 4 disconnected
components? Measure their IDOS d per-component vs pooled, on their literal matrix.
Also test the specific extension claims against the referent where possible."""
import numpy as np, networkx as nx, os
from numpy.linalg import eigvalsh
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R).copy(); np.fill_diagonal(W,0); A=(W>0).astype(int)
G=nx.from_numpy_array(A)

def idos(Wsub, lo_rank=32, hi_rank=81):
    L=np.diag(Wsub.sum(1))-Wsub; ev=np.sort(eigvalsh(L)); nz=ev[ev>1e-8]
    if len(nz) < hi_rank:
        # scale window to component size, keep same fractional band (their 32/146..81/146)
        a=max(int(0.22*len(nz)),2); b=max(int(0.55*len(nz)),a+4)
    else:
        a,b=lo_rank-1,hi_rank
    if b-a<4 or len(nz)<8: return np.nan,len(nz)
    x,y=np.log10(nz[a:b]),np.log10(np.arange(1,len(nz)+1)[a:b])
    M=np.vstack([x,np.ones_like(x)]).T; sl=np.linalg.lstsq(M,y,rcond=None)[0][0]
    return 2*sl,len(nz)

# pooled (their number)
dp,_=idos(W); print(f"POOLED (4 disconnected comps, their window ranks32-81): d={dp:.2f}  [their 3.77]\n")

# per component, each with a size-matched fractional window
print("PER-COMPONENT (each measured alone, fractional window matched to their band):")
comps=sorted(nx.connected_components(G),key=len,reverse=True)
percomp=[]
for i,c in enumerate(comps):
    idx=sorted(c); Wc=W[np.ix_(idx,idx)]; dc,nnz=idos(Wc)
    percomp.append(dc); print(f"  comp {i} (N={len(c)}, nonzero-ev={nnz}): d={dc:.2f}")
print(f"  mean per-component d = {np.nanmean(percomp):.2f}")
print(f"  --> if pooled({dp:.2f}) >> mean-per-component, the 3.77 is a POOLING artifact of stacking 4 spectra\n")

# control: take ONE connected ER graph of 150 nodes/448 edges (their edge count) vs
# a 4-component ER graph with same total edges — does disconnection alone inflate d?
def er_idos(n,m,seed,ncomp=1):
    if ncomp==1:
        g=nx.gnm_random_graph(n,m,seed=seed)
    else:
        # split into ncomp equal blobs, distribute edges
        g=nx.Graph(); sizes=[n//ncomp]*ncomp; off=0
        per=m//ncomp
        for s in sizes:
            h=nx.gnm_random_graph(s,per,seed=seed); h=nx.relabel_nodes(h,{k:k+off for k in h.nodes()})
            g=nx.union(g,h); off+=s
    W2=nx.to_numpy_array(g); return idos(W2)[0], nx.number_connected_components(g)
d1,c1=er_idos(150,448,7,1); d4,c4=er_idos(150,448,7,4)
print("CONTROL — does disconnection ALONE inflate IDOS d? (random graphs, 150 nodes, 448 edges)")
print(f"  1 connected ER component:  d={d1:.2f}")
print(f"  4 disconnected ER blobs:   d={d4:.2f}")
print(f"  --> disconnection inflates IDOS d by {d4-d1:+.2f} with ZERO geometry present" if not np.isnan(d4) else "")
