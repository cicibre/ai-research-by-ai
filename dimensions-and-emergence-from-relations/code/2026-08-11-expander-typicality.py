"""Re-derive their 'obstacle' table: random 4-regular graphs are expanders whose
d_eff = ln N / ln(diam) climbs, vs a 2-torus fixed at d=2. Cross-check their crude
d_eff against my validated spectral-dimension ruler on the SAME graphs."""
import numpy as np, networkx as nx
from numpy.linalg import eigvalsh

def deff(G):
    N=G.number_of_nodes()
    if not nx.is_connected(G): G=G.subgraph(max(nx.connected_components(G),key=len)).copy(); N=G.number_of_nodes()
    dia=nx.diameter(G)
    return N, dia, np.log(N)/np.log(dia)

def spectral_d(G):  # my validated ruler (normalized-Laplacian heat kernel)
    n=G.number_of_nodes(); W=nx.to_numpy_array(G); deg=W.sum(1)
    Dm=np.diag(1/np.sqrt(deg)); lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32]))

print(f"{'N':>6} {'rand4reg diam':>13} {'2torus diam':>12} {'d_eff(rand)':>12} {'d_s(rand)':>10} {'d_s(torus)':>11}")
for N in [64,256,1024,4096]:
    L=int(round(N**0.5)); tor=nx.grid_graph([L,L],periodic=True)
    G=nx.random_regular_graph(4,N,seed=7)
    _,dr,de=deff(G); _,dt,_=deff(tor)
    # spectral only for smaller (eig is O(n^3)); skip 4096
    dsr=spectral_d(G) if N<=1024 else float('nan')
    dst=spectral_d(tor) if N<=1024 else float('nan')
    print(f"{N:>6} {dr:>13} {dt:>12} {de:>12.2f} {dsr:>10.2f} {dst:>11.2f}")
print("\ntheir table d_eff(rand): 2.58 / 2.85 / 3.28 / 3.65 (drifting to inf); torus stays d=2")
print("cross-check: does my spectral ruler AGREE the random graph climbs & the torus is flat?")
