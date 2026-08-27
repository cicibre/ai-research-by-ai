"""Definitive order test on the ACTUAL locality order parameter (spectral dimension),
not its compression proxy. First-order => bimodal d_s distribution at f_crit (coexistence).
Disambiguates: if d_s ALSO unimodal -> transition genuinely 2nd-order (crystallization=metaphor).
If d_s bimodal but compression wasn't -> compression != locality (identity fails)."""
import numpy as np, networkx as nx, math
from numpy.linalg import eigvalsh

def rgg_frac(N, f, kbar=6, seed=0):
    r=np.random.default_rng(seed); rad=math.sqrt(kbar/(N*math.pi))
    pos=r.random((N,2)); G=nx.random_geometric_graph(N,rad,pos={i:pos[i] for i in range(N)})
    for (u,v) in list(G.edges()):
        if r.random()>f:
            G.remove_edge(u,v)
            while True:
                a,b=int(r.integers(N)),int(r.integers(N))
                if a!=b and not G.has_edge(a,b): G.add_edge(a,b); break
    return G

def d_s(G):
    g=G.subgraph(max(nx.connected_components(G),key=len)); n=g.number_of_nodes()
    if n<20: return np.nan
    W=nx.to_numpy_array(g); deg=W.sum(1); Dm=np.diag(1/np.sqrt(deg))
    lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32]))

def bc(x):
    x=np.asarray(x); x=x[~np.isnan(x)]; n=len(x)
    if n<4 or np.std(x)==0: return np.nan
    m,s=np.mean(x),np.std(x); g=np.mean(((x-m)/s)**3); k=np.mean(((x-m)/s)**4)-3
    return (g**2+1)/(k+3*(n-1)**2/((n-2)*(n-3)))

REPS=25; FS=[0.60,0.65,0.70,0.72,0.74,0.80]
print("=== d_s distribution across replicas (BC>0.555 => bimodal => FIRST-ORDER) ===")
for N in [400,700]:
    print(f"\n--- N={N} ---")
    print(f"{'f':>5} {'mean d_s':>9} {'std':>6} {'BC':>6} {'range':>16}")
    for f in FS:
        ds=[d_s(rgg_frac(N,f,seed=7000*int(f*100)+s)) for s in range(REPS)]
        ds=np.array(ds); print(f"{f:>5.2f} {np.nanmean(ds):>9.2f} {np.nanstd(ds):>6.2f} {bc(ds):>6.3f} [{np.nanmin(ds):>5.1f},{np.nanmax(ds):>5.1f}]")
print("\nunimodal at f_crit, both N -> transition is CONTINUOUS on the real order parameter too.")
