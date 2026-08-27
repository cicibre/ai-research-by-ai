#!/usr/bin/env python3
# MEDIATOR ABLATION 1 — per seal 0438e8b. Committed pre-fire.
import math, random, statistics as st, os
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
N, F = 900, 0.65

def mean_c(adj):
    tot=0.0; n2=0
    for v in range(N):
        nb=list(adj[v]); k=len(nb)
        if k>=2:
            n2+=1
            e=sum(1 for i in range(k) for j in range(i+1,k) if nb[j] in adj[nb[i]])
            tot+=2.0*e/(k*(k-1))
    return tot/n2 if n2 else 0.0

def degree_preserving_randomize(adj, rng):
    edges=[(a,b) for a in range(N) for b in adj[a] if a<b]
    target=10*len(edges); done=0; tries=0
    while done<target and tries<40*len(edges):
        tries+=1
        (a,b)=edges[rng.randrange(len(edges))]; (c,d)=edges[rng.randrange(len(edges))]
        if rng.random()<0.5: c,d=d,c
        if len({a,b,c,d})<4: continue
        if b not in adj[a] or d not in adj[c]: 
            edges=[(x,y) for x in range(N) for y in adj[x] if x<y]; continue
        if d in adj[a] or b in adj[c]: continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        done+=1
        if done % (2*len(edges)) == 0:
            edges=[(x,y) for x in range(N) for y in adj[x] if x<y]
    return adj

def build(arm, seed):
    rng=random.Random(seed)
    if arm in ("A","A-sw"):
        adj=rewire(rgg(N,rng), F, rng)
    else:
        adj=grow_prune(rewire(rgg(N,rng), 1.0, rng), rng)
        adj=rewire(adj, F, rng)
    if arm.endswith("sw"):
        adj=degree_preserving_randomize(adj, random.Random(seed+900000))
    return grow_prune(adj, rng)

res={}
for arm, blk in (("A",500000),("A-sw",500100),("B",500200),("B-sw",500300)):
    Cs=[mean_c(build(arm, blk+i)) for i in range(30)]
    res[arm]=(st.mean(Cs), st.stdev(Cs)/math.sqrt(30))
    print(f"{arm:5s} C={res[arm][0]:.4f} +/- {res[arm][1]:.4f}", flush=True)
adv=res["B"][0]-res["A"][0]; sadv=math.sqrt(res["B"][1]**2+res["A"][1]**2)
adv_sw=res["B-sw"][0]-res["A-sw"][0]; ssw=math.sqrt(res["B-sw"][1]**2+res["A-sw"][1]**2)
print(f"adv={adv:.4f}({adv/sadv:.1f}s)  adv_sw={adv_sw:.4f}({adv_sw/ssw:.1f}s)  ratio={adv_sw/adv:.2f}")
if adv < 2*sadv: v="INSUFFICIENT (sanity fail)"
elif adv_sw <= 0.35*adv: v="MEDIATED"
elif adv_sw >= 0.65*adv and adv_sw >= 2*ssw: v="NOT-MEDIATED (degree state suffices — report loudly)"
else: v="PARTIAL/INSUFFICIENT"
print("VERDICT:", v)
