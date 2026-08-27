"""Item-5 falsifier: is |Δd_s|≤0.07 real convergence or within replica scatter?
Two attacks the original verdict couldn't answer (it reported means only):
  (A) per-cell SD across replicas (8, up from 5) — is 0.07 << scatter or ~ scatter?
  (B) fit-window robustness — recompute d_s over several windows on the SAME
      eigenvalues; if the ≤0.07 / all-converge conclusion flips, it was window-luck.
Eigenvalues computed ONCE per (pc,seed,size); windows are cheap re-reads.
"""
import numpy as np, networkx as nx
from collections import defaultdict, deque
from numpy.linalg import eigvalsh

def grow(p_fire,p_close,init=((0,1),(0,2)),max_nodes=4000,max_edges=250000,seed=0):
    rng=np.random.default_rng(seed)
    edges=[tuple(e) for e in init]; nxt=1+max(max(e) for e in edges)
    for t in range(400):
        by_head=defaultdict(list)
        for i,(a,b) in enumerate(edges): by_head[a].append(i)
        used,jobs=set(),[]
        for h,idxs in by_head.items():
            rng.shuffle(idxs)
            for k in range(0,len(idxs)-1,2):
                if rng.random()>p_fire: continue
                i,j=idxs[k],idxs[k+1]; used|={i,j}; jobs.append((h,edges[i][1],edges[j][1]))
        edges=[e for i,e in enumerate(edges) if i not in used]
        for x,y,z in jobs:
            w=nxt; nxt+=1
            if rng.random()<p_close: edges+=[(x,z),(x,w),(y,w),(z,w)]
            else:                    edges+=[(x,w),(x,w),(y,w),(z,w)]
        if not jobs or nxt>max_nodes or len(edges)>max_edges: break
    G=nx.Graph()
    for a,b in edges:
        if a!=b: G.add_edge(a,b)
    return G

def interior_patch(G,N):
    g=G.subgraph(max(nx.connected_components(G),key=len))
    seed=min(g.nodes()); seen=[seed]; ss={seed}; dq=deque([seed])
    while dq and len(seen)<N:
        u=dq.popleft()
        for v in g.neighbors(u):
            if v not in ss: ss.add(v); seen.append(v); dq.append(v)
    return g.subgraph(seen[:N]).copy()

def eigs(G):
    g=G.subgraph(max(nx.connected_components(G),key=len)); n=g.number_of_nodes()
    if n<30: return None
    W=nx.to_numpy_array(g); deg=W.sum(1); Dm=np.diag(1/np.sqrt(deg))
    return np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)

def d_s_from(lam, lo, hi, npts=40):
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),npts)
    P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[lo:hi]))

REPS=8                                # up from 5
WINDOWS=[(10,32),(8,34),(12,30),(5,35),(14,28)]   # original + 4 perturbations
PCS=[0.0,0.3,0.5,0.7,0.85,1.0]

# collect eigenvalues once
store={}   # (pc,size) -> list of lam arrays over reps
for pc in PCS:
    for size in (700,1400):
        store[(pc,size)]=[]
    for s in range(REPS):
        G=grow(1.0,pc,seed=s)
        if G.number_of_nodes()<1600: continue
        store[(pc,700)].append(eigs(interior_patch(G,700)))
        store[(pc,1400)].append(eigs(interior_patch(G,1400)))

print("=== ITEM-5 FALSIFIER: |Δd_s| vs replica scatter, across fit windows ===")
print("orig window [10:32]; claim under test: |Δd_s|≤0.07 = convergence at every p_close\n")
for (lo,hi) in WINDOWS:
    print(f"--- fit window [{lo}:{hi}] ---")
    print(f"{'p_close':>7} {'d700 (sd)':>14} {'d1400 (sd)':>14} {'|Δmeans|':>9} {'Δ/pooledSD':>11}")
    maxdd=0.0; flips=[]
    for pc in PCS:
        a=[d_s_from(l,lo,hi) for l in store[(pc,700)] if l is not None]
        b=[d_s_from(l,lo,hi) for l in store[(pc,1400)] if l is not None]
        if not a or not b: continue
        m1,s1=np.mean(a),np.std(a); m2,s2=np.mean(b),np.std(b)
        dd=abs(m2-m1); pooled=np.sqrt((s1**2+s2**2)/2)+1e-9
        maxdd=max(maxdd,dd)
        if dd>=0.4: flips.append(pc)
        print(f"{pc:>7.2f} {m1:>7.2f} ({s1:>4.2f}) {m2:>7.2f} ({s2:>4.2f}) {dd:>9.3f} {dd/pooled:>11.2f}")
    verdict = "ALL CONVERGE (max|Δ|<0.4)" if not flips else f"DIVERGE at p_close={flips}"
    print(f"   -> max|Δmeans|={maxdd:.3f}   {verdict}\n")
