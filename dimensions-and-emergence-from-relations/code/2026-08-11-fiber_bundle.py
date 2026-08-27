"""Honest model of 'too many dependencies to support itself': IRREVERSIBLE
load-redistribution (fiber-bundle). Node fails when load>capacity, dumps load on
living neighbors (cascade), and is REMOVED (one-way burn). NOT SOC-by-construction.
Q: sharp catastrophic collapse (a giant final avalanche) or self-organized scale-free?
"""
import numpy as np, networkx as nx
from collections import defaultdict
def grow(p_fire,p_close,init=((0,1),(0,2)),max_nodes=1600,max_edges=80000,seed=0):
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
    return nx.convert_node_labels_to_integers(G.subgraph(max(nx.connected_components(G),key=len)).copy())

def fiber_bundle(G, seed=0):
    n=G.number_of_nodes(); rng=np.random.default_rng(seed)
    nbrs=[set(G.neighbors(i)) for i in range(n)]
    cap=np.array([max(len(nbrs[i]),1) for i in range(n)],float)  # capacity = degree
    load=np.zeros(n); alive=np.ones(n,bool); aval=[]
    drives=0
    while alive.sum()>0.1*n and drives<3*n:
        living=np.where(alive)[0]
        if len(living)==0: break
        load[rng.choice(living)] += 1.0; drives+=1        # add one unit of load
        stack=[i for i in living if load[i]>=cap[i]]; failed=0
        while stack:
            i=stack.pop()
            if not alive[i] or load[i]<cap[i]: continue
            alive[i]=False; failed+=1
            liv_n=[j for j in nbrs[i] if alive[j]]
            if liv_n:
                share=load[i]/len(liv_n)
                for j in liv_n:
                    load[j]+=share
                    if load[j]>=cap[j]: stack.append(j)
            load[i]=0
        if failed>0: aval.append(failed)
    return np.array(aval), n, 1-alive.mean()   # avalanches, N, final dead fraction

print("=== FIBER-BUNDLE (irreversible burn): sharp catastrophe or scale-free? ===",flush=True)
print(f"{'fabric':18s} {'N':>5} {'#aval':>6} {'max_aval':>9} {'max/N':>6} {'deadfrac':>9} {'signature':>22}",flush=True)
for pc,name in [(1.0,"sheet p_close=1"),(0.5,"mixed p_close=.5"),(0.0,"line p_close=0")]:
    G=grow(1.0,pc,seed=3); av,N,dead=fiber_bundle(G,seed=2)
    mx=av.max() if len(av) else 0
    # signature: one giant avalanche (catastrophe) vs many-scales (SOC-ish)
    frac_in_biggest = mx/av.sum() if av.sum()>0 else 0
    sig = "CATASTROPHE (1 giant)" if frac_in_biggest>0.3 else ("scale-free-ish" if len(av)>30 else "damped/small")
    print(f"  {name:16s} {N:>5} {len(av):>6} {mx:>9} {mx/N:>6.2f} {dead:>9.2f} {sig:>22}",flush=True)
print("\nmax_aval/N near 1 + one avalanche holding most failures = SHARP CATASTROPHE (tuned, not SOC).",flush=True)
print("many avalanches, no single giant = closer to self-organized scale-free.",flush=True)
