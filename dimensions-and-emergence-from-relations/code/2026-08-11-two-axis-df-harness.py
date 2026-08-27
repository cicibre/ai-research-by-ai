"""Does BRANCHING make a lung (space-filling, high d_f) or a line (low d_f)?
Measure ball-growth d_f alongside spectral d_s across p_close. d_s is blind to
space-filling trees (reads ~4/3); d_f (ball growth N(r)~r^d_f) sees them.
Contrast at low p_close (branching) is the lung test."""
import numpy as np, networkx as nx
from collections import defaultdict, deque
from numpy.linalg import eigvalsh

def grow(p_fire,p_close,init=((0,1),(0,2)),max_nodes=4000,max_edges=250000,seed=0):
    rng=np.random.default_rng(seed); edges=[tuple(e) for e in init]; nxt=1+max(max(e) for e in edges)
    for t in range(400):
        bh=defaultdict(list)
        for i,(a,b) in enumerate(edges): bh[a].append(i)
        used,jobs=set(),[]
        for h,idxs in bh.items():
            rng.shuffle(idxs)
            for k in range(0,len(idxs)-1,2):
                if rng.random()>p_fire: continue
                i,j=idxs[k],idxs[k+1]; used|={i,j}; jobs.append((h,edges[i][1],edges[j][1]))
        edges=[e for i,e in enumerate(edges) if i not in used]
        for x,y,z in jobs:
            w=nxt; nxt+=1
            edges += ([(x,z),(x,w),(y,w),(z,w)] if rng.random()<p_close else [(x,w),(x,w),(y,w),(z,w)])
        if not jobs or nxt>max_nodes or len(edges)>max_edges: break
    G=nx.Graph()
    for a,b in edges:
        if a!=b: G.add_edge(a,b)
    return G.subgraph(max(nx.connected_components(G),key=len)).copy()

def d_s(G):
    n=G.number_of_nodes()
    if n<30: return np.nan
    W=nx.to_numpy_array(G); deg=W.sum(1); Dm=np.diag(1/np.sqrt(deg))
    lam=np.clip(np.sort(eigvalsh(np.eye(n)-Dm@W@Dm)),0,2)
    ts=np.geomspace(1.0,2.0/max(lam[1],1e-6),40); P=np.array([np.mean(np.exp(-lam*t)) for t in ts])
    return float(np.median((-2*np.gradient(np.log(P),np.log(ts)))[10:32]))

def d_f_ballgrowth(G, nsrc=40, seed=0):
    """N(r) = avg nodes within graph-distance r from source; slope logN vs logr."""
    rng=np.random.default_rng(seed); nodes=list(G.nodes())
    srcs=rng.choice(nodes,size=min(nsrc,len(nodes)),replace=False)
    Rmax=8; curves=[]
    for s in srcs:
        d={s:0}; dq=deque([s]); cnt=np.zeros(Rmax+1)
        while dq:
            u=dq.popleft()
            if d[u]>=Rmax: continue
            for v in G.neighbors(u):
                if v not in d: d[v]=d[u]+1; dq.append(v)
        vals=np.array(list(d.values()))
        curves.append([np.sum(vals<=r) for r in range(1,Rmax+1)])
    Nr=np.mean(curves,axis=0); r=np.arange(1,Rmax+1)
    a,b=2,7  # intermediate window
    return float(np.polyfit(np.log(r[a:b]),np.log(Nr[a:b]),1)[0])

def interior(G,N):
    seed=min(G.nodes()); seen=[seed]; ss={seed}; dq=deque([seed])
    while dq and len(seen)<N:
        u=dq.popleft()
        for v in G.neighbors(u):
            if v not in ss: ss.add(v); seen.append(v); dq.append(v)
    return G.subgraph(seen[:N]).copy()

print("=== d_s (spectral, blind to trees) vs d_f (ball-growth, sees space-filling) ===", flush=True)
print(f"{'p_close':>8} {'d_s':>6} {'d_f':>6} {'C':>7}  <- low p_close = branching (lung test)", flush=True)
for pc in [0.0,0.3,0.5,0.7,1.0]:
    dss=[];dfs=[];cs=[]
    for s in range(5):
        G=grow(1.0,pc,seed=s)
        if G.number_of_nodes()<1500: continue
        P=interior(G,1400)
        dss.append(d_s(P)); dfs.append(d_f_ballgrowth(P,seed=s)); cs.append(nx.average_clustering(P))
    print(f"{pc:>8.2f} {np.nanmean(dss):>6.2f} {np.nanmean(dfs):>6.2f} {np.nanmean(cs):>7.4f}", flush=True)
print("\nread: if p_close=0 shows d_f >> d_s -> branching IS space-filling (LUNG), d_s undercounted it.", flush=True)
print("      if d_f ~ d_s ~ low -> it's a LINE, not a lung; our rule's branching isn't space-filling.", flush=True)
