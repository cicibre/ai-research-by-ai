"""Finite-size scaling: is the f_crit transition CRITICAL or CROSSOVER?
Pre-reg: findings/2026-08-11-criticality-FSS-PREREG.md
Susceptibility chi(f,N)=N*Var(d_s) over replicas, 4 N, focused f-grid.
CRITICAL: chi_max grows monotonically with N + peak sharpens. CROSSOVER: flat/shrinks.
"""
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

NS=[300,600,1200,2400]; FS=[0.62,0.66,0.70,0.72,0.74,0.78,0.82]; REPS=16
print("=== FINITE-SIZE SCALING: critical vs crossover ===", flush=True)
chi_by_N={}; var_by_N={}
for N in NS:
    print(f"\n--- N={N} ---", flush=True)
    print(f"{'f':>5} {'mean d_s':>9} {'Var':>8} {'chi=N*Var':>10}", flush=True)
    chis=[]; varr=[]
    for f in FS:
        ds=np.array([d_s(rgg_frac(N,f,seed=90000*int(f*100)+s)) for s in range(REPS)])
        v=np.nanvar(ds); chi=N*v; chis.append(chi); varr.append(v)
        print(f"{f:>5.2f} {np.nanmean(ds):>9.3f} {v:>8.4f} {chi:>10.2f}", flush=True)
    chi_by_N[N]=np.array(chis); var_by_N[N]=np.array(varr)

print("\n=== SCALING OF THE SUSCEPTIBILITY PEAK ===", flush=True)
print(f"{'N':>6} {'chi_max':>9} {'at f':>6} {'Var_max':>9} {'peak_width(f)':>13}", flush=True)
peakN=[]
for N in NS:
    ch=chi_by_N[N]; i=int(np.nanargmax(ch)); cm=ch[i]; peakN.append(cm)
    # width: # of f-points within 60% of peak (crude sharpening proxy)
    width=np.sum(ch>=0.6*cm)
    print(f"{N:>6} {cm:>9.2f} {FS[i]:>6.2f} {var_by_N[N].max():>9.4f} {width:>13d}", flush=True)
print(f"\nchi_max across N = {[round(float(x),1) for x in peakN]}", flush=True)
grow = all(peakN[i+1] > peakN[i] for i in range(len(peakN)-1))
shrink = all(peakN[i+1] < peakN[i] for i in range(len(peakN)-1))
# power-law fit chi_max ~ N^a
lnN=np.log(NS); lnC=np.log(peakN); a=np.polyfit(lnN,lnC,1)[0]
print(f"chi_max ~ N^{a:.2f}  (positive & clean => critical; ~0 or negative => crossover)", flush=True)
print("\nVERDICT:", flush=True)
if grow and a>0.15:
    print(f"  chi_max GROWS monotonically, exponent {a:.2f} -> leans CRITICAL (check peak sharpening + collapse next)", flush=True)
elif shrink or a<0.05:
    print(f"  chi_max flat/DECREASING (N^{a:.2f}) -> CROSSOVER: no diverging susceptibility, no critical point", flush=True)
else:
    print(f"  chi_max non-monotonic / weak (N^{a:.2f}) -> INSUFFICIENT: no clean trend", flush=True)
