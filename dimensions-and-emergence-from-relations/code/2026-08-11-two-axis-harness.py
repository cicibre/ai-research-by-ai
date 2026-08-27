"""Two-axis growth (k3 rule), FIXED harness. Grow once to a large cluster, then
interior-subsample to EXACT sizes 700 & 1400 (BFS from oldest node = interior) —
clean 2x doubling by construction + tractable eig + boundary control in one move.
Pre-reg: findings/2026-08-11-two-axis-growth-PREREG.md
"""
import numpy as np, networkx as nx, math
from collections import defaultdict, deque
from numpy.linalg import eigvalsh

def grow(p_fire, p_close, init=((0,1),(0,2)), max_nodes=4000, max_edges=250000, seed=0):
    rng = np.random.default_rng(seed)
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

def interior_patch(G, N):
    g=G.subgraph(max(nx.connected_components(G),key=len))
    seed=min(g.nodes())                    # lowest ID = oldest = interior
    seen=[seed]; ss={seed}; dq=deque([seed])
    while dq and len(seen)<N:
        u=dq.popleft()
        for v in g.neighbors(u):
            if v not in ss: ss.add(v); seen.append(v); dq.append(v)
    return g.subgraph(seen[:N]).copy()

def d_s(G):
    g=G.subgraph(max(nx.connected_components(G),key=len)); n=g.number_of_nodes()
    if n<30: return np.nan
    W=nx.to_numpy_array(g); deg=W.sum(1); Dm=np.diag(1/np.sqrt(deg))
    lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32]))

print("=== VALIDATION: geometry knob (p_fire=1, interior patch N=800) ===", flush=True)
print(f"{'p_close':>8} {'d_s':>6} {'C':>7} {'grownN':>7}", flush=True)
for pc in [0.0,1.0]:
    dss=[];cs=[];gn=[]
    for s in range(5):
        G=grow(1.0,pc,seed=s); gn.append(G.number_of_nodes())
        P=interior_patch(G,800); dss.append(d_s(P)); cs.append(nx.average_clustering(P))
    print(f"{pc:>8.2f} {np.nanmean(dss):>6.2f} {np.nanmean(cs):>7.4f} {int(np.mean(gn)):>7}", flush=True)
print("  expect p_close=1: finite d_s + C>0.02 (sheet); p_close=0: high/diverging d_s + C~0 (tree)\n", flush=True)

print("=== GEOMETRY axis: d_s(p_close), interior patch N=700 vs 1400 (exact 2x) ===", flush=True)
print(f"{'p_close':>8} {'d_s@700':>8} {'d_s@1400':>9} {'|d|':>5} {'C':>7} {'verdict':>12}", flush=True)
rows=[]
for pc in [0.0,0.3,0.5,0.7,0.85,1.0]:
    d1=[];d2=[];cs=[]
    for s in range(5):
        G=grow(1.0,pc,seed=s)
        if G.number_of_nodes()<1600: continue
        d1.append(d_s(interior_patch(G,700))); d2.append(d_s(interior_patch(G,1400)))
        cs.append(nx.average_clustering(interior_patch(G,700)))
    m1,m2=np.nanmean(d1),np.nanmean(d2); dd=abs(m2-m1)
    verdict="GEOMETRIC" if (dd<0.4 and m2<8) else ("DIVERGING" if (m2>=8 or m2-m1>0.4) else "converging?")
    rows.append((pc,m1,m2,dd,np.nanmean(cs),verdict))
    print(f"{pc:>8.2f} {m1:>8.2f} {m2:>9.2f} {dd:>5.2f} {np.nanmean(cs):>7.4f} {verdict:>12}", flush=True)
print("\nread: which p_close values are GEOMETRIC (converged finite d_s)? Is the boundary SHARP", flush=True)
print("      (narrow p_close* with finite above / diverging below) or BROAD (geometric only near 1)?", flush=True)
