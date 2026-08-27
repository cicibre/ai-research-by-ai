"""Is burn-down self-organized-critical (power-law avalanches = phoenix) or damped
(exponential = even the cascade fades)? BTW sandpile on grown fabrics.
Pre-reg: findings/2026-08-11-cascade-SOC-PREREG.md. Validate on 2D lattice (must be power-law).
"""
import numpy as np, networkx as nx
from collections import defaultdict

def grow(p_fire,p_close,init=((0,1),(0,2)),max_nodes=2500,max_edges=150000,seed=0):
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

def sandpile_avalanches(G, n_drive=8000, transient=3000, sink_frac=0.05, seed=0):
    G=nx.convert_node_labels_to_integers(G); n=G.number_of_nodes()
    rng=np.random.default_rng(seed)
    nbrs=[list(G.neighbors(i)) for i in range(n)]
    cap=np.array([max(len(nb),1) for nb in nbrs])          # capacity = degree
    sinks=set(rng.choice(n, size=max(1,int(sink_frac*n)), replace=False))
    issink=np.zeros(n,bool);
    for s in sinks: issink[s]=True
    nonsink=[i for i in range(n) if not issink[i]]
    h=np.zeros(n,int); sizes=[]
    for step in range(n_drive):
        h[rng.choice(nonsink)] += 1
        toppled=0
        stack=[i for i in range(n) if h[i]>=cap[i] and not issink[i]]
        stack=list(dict.fromkeys(stack))
        while stack:
            i=stack.pop()
            if h[i]<cap[i] or issink[i]: continue
            h[i]-=cap[i]; toppled+=1
            for j in nbrs[i]:
                if issink[j]: continue                     # sink absorbs+discards
                h[j]+=1
                if h[j]>=cap[j]: stack.append(j)
        if step>=transient and toppled>0: sizes.append(toppled)
    return np.array(sizes)

def fit_discriminate(sizes):
    if len(sizes)<200: return "INSUFFICIENT", np.nan, np.nan, np.nan
    # log-binned histogram
    smax=sizes.max()
    bins=np.unique(np.floor(np.geomspace(1,smax+1,25)).astype(int))
    cnt,edg=np.histogram(sizes,bins=bins)
    ctr=np.sqrt(edg[:-1]*edg[1:]); w=np.diff(edg)
    dens=cnt/w/len(sizes)
    m=(cnt>0)&(ctr>1)&(ctr<smax*0.5)                       # drop tail cutoff + s=1
    if m.sum()<4: return "INSUFFICIENT", np.nan, np.nan, np.nan
    x,y=ctr[m],dens[m]
    # power-law: log y vs log x
    pl=np.polyfit(np.log(x),np.log(y),1); ypl=np.polyval(pl,np.log(x))
    r2_pl=1-np.sum((np.log(y)-ypl)**2)/np.sum((np.log(y)-np.log(y).mean())**2)
    # exponential: log y vs x
    ex=np.polyfit(x,np.log(y),1); yex=np.polyval(ex,x)
    r2_ex=1-np.sum((np.log(y)-yex)**2)/np.sum((np.log(y)-np.log(y).mean())**2)
    tau=-pl[0]; decades=np.log10(x.max()/x.min())
    if r2_pl>r2_ex+0.02 and 1<=tau<=2.5 and decades>=1.5: v="POWER-LAW (SOC/phoenix)"
    elif r2_ex>=r2_pl: v="EXPONENTIAL (damped)"
    else: v="ambiguous"
    return v, tau, decades, (r2_pl,r2_ex)

def torus2d(L): return nx.convert_node_labels_to_integers(nx.grid_graph([L,L],periodic=False))

print("=== VALIDATION: 2D lattice sandpile must be POWER-LAW ===", flush=True)
G=torus2d(45)
s=sandpile_avalanches(G,seed=1)
v,tau,dec,r2=fit_discriminate(s)
print(f"  2D 45x45: {v}  tau={tau:.2f} decades={dec:.2f} R2(pl,exp)={tuple(round(x,3) for x in r2) if isinstance(r2,tuple) else r2}  n_av={len(s)}", flush=True)
print("  (expect POWER-LAW, tau~1.0-1.4)\n", flush=True)

print("=== TEST: grown fabric ===", flush=True)
for pc,name in [(1.0,"sheet p_close=1"),(0.5,"mixed p_close=.5"),(0.0,"line p_close=0")]:
    vs=[]
    G=grow(1.0,pc,seed=3)
    s=sandpile_avalanches(G,seed=2)
    v,tau,dec,r2=fit_discriminate(s)
    print(f"  {name:18s} N={G.number_of_nodes():5d}: {v}  tau={tau:.2f} decades={dec:.2f} R2(pl,exp)={tuple(round(x,3) for x in r2) if isinstance(r2,tuple) else r2}  n_av={len(s)}", flush=True)
print("\nPOWER-LAW on grown fabric = phoenix REAL (self-organized scale-free burn).", flush=True)
print("EXPONENTIAL = even the cascade fades; death is a fade all the way down.", flush=True)
