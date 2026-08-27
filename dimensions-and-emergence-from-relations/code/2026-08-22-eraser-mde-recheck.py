#!/usr/bin/env python3
# Brief 3.2 support: fresh f=0 eraser cell with per-channel MDEs (referee v1 request).
# Paired n=40: arm-with-history (settled) vs arm-without, both totally rewired (f=0).
# Reported in brief: C MDE 0.00076 z=+1.64 | L MDE 0.027 z=-1.70 | kvar z=+14.6
import math, random, statistics as st, os
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read()
ns = {}; exec(src.rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
N, M = 900, 40
def clustering(adj):
    tot=0.0; cnt=0
    for u in range(N):
        nb=list(adj[u]); d=len(nb)
        if d<2: continue
        links=sum(1 for a in range(d) for b in range(a+1,d) if nb[b] in adj[nb[a]])
        tot+=2*links/(d*(d-1)); cnt+=1
    return tot/cnt if cnt else 0.0
def pathlen(adj, rng, samples=30):
    tot=0; cnt=0
    for _ in range(samples):
        s=rng.randrange(N); dist={s:0}; q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in dist: dist[w]=dist[v]+1; q.append(w)
        tot+=sum(dist.values()); cnt+=len(dist)
    return tot/cnt
def kvar(adj):
    ds=[len(a) for a in adj]; m=sum(ds)/N
    return sum((d-m)**2 for d in ds)/N
diffs={"C":[],"L":[],"kvar":[]}
for i in range(M):
    rng=random.Random(15000+i)
    base=rgg(N,rng)
    U=[set(s) for s in base]; V=[set(s) for s in base]
    U=grow_prune(U, random.Random(25000+i))
    U=rewire(U,0.0,random.Random(35000+i))
    V=rewire(V,0.0,random.Random(35000+i))
    diffs["C"].append(clustering(U)-clustering(V))
    diffs["kvar"].append(kvar(U)-kvar(V))
    diffs["L"].append(pathlen(U,random.Random(45000+i))-pathlen(V,random.Random(55000+i)))
print("paired n=40, with-history minus without, after TOTAL rewiring (f=0):")
for k in ("C","L","kvar"):
    d=diffs[k]; mu=st.mean(d); se=st.stdev(d)/math.sqrt(M)
    print(f"  {k:5s} diff={mu:+.5f}  SE={se:.5f}  z={mu/se:+6.2f}  MDE(80%)={2.8*se:.5f}")
