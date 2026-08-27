#!/usr/bin/env python3
# THOMAS TEST — identity across burn+rebuild: scar channel vs shape channel. Seal: survey addendum 13:12.
import math, random
src = open('/Users/cc/academics/dimensions-and-emergence-from-relations/code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py').read()
ns = {}; exec(src.rsplit('\nSEEDS=15',1)[0], ns)
sdim, rgg, rewire, grow_prune = ns['spectral_dim'], ns['rgg'], ns['rewire'], ns['grow_prune']
N, M, F = 900, 40, 0.65
def degvec(adj): return [len(a) for a in adj]
def shape_stats(adj, seed):
    degs=degvec(adj); m=sum(degs)/N
    ksd=math.sqrt(sum((d-m)**2 for d in degs)/(N-1))
    tri=0; deg2=0
    for u in range(N):
        nb=list(adj[u]); k=len(nb)
        if k>=2:
            deg2+=1
            e=sum(1 for i in range(len(nb)) for j in range(i+1,len(nb)) if nb[j] in adj[nb[i]])
            tri+=2*e/(k*(k-1))
    C=tri/deg2 if deg2 else 0
    ds=sdim(adj, seed=seed)
    return [C, ds if ds is not None else 0.0, ksd]
def cos(a,b):
    na=math.sqrt(sum(x*x for x in a)); nb=math.sqrt(sum(x*x for x in b))
    return sum(x*y for x,y in zip(a,b))/(na*nb) if na*nb else 0
pre_deg, post_deg, pre_shape, post_shape = [], [], [], []
for i in range(M):
    rng=random.Random(12000+i)
    adj=grow_prune(rewire(rgg(N,rng),1.0,rng),rng)
    pre_deg.append(degvec(adj)); pre_shape.append(shape_stats(adj,(12000+i)*7+1))
    adj=grow_prune(rewire(adj,F,rng),rng)   # burn + return
    post_deg.append(degvec(adj)); post_shape.append(shape_stats(adj,(12000+i)*7+2))
    print(f"world {i} done", flush=True)
# z-score shape stats across worlds for fair distance
import statistics as st
def zcols(rows):
    cols=list(zip(*rows)); zs=[]
    for c in cols:
        m=st.mean(c); s=st.stdev(c) or 1
        zs.append([(x-m)/s for x in c])
    return list(zip(*zs))
przs, pozs = zcols(pre_shape), zcols(post_shape)
scar_hits=sum(1 for i in range(M) if max(range(M), key=lambda j: cos(post_deg[i], pre_deg[j]))==i)
shape_hits=sum(1 for i in range(M) if min(range(M), key=lambda j: sum((a-b)**2 for a,b in zip(pozs[i],przs[j])))==i)
sa, sh = scar_hits/M, shape_hits/M
verdict = ("SCAR-CARRIES-IDENTITY (Thomas confirmed)" if (sa>=0.25 and sa>sh) else ("SHAPE-CARRIES" if sh>=sa and sh>=0.25 else "NEITHER (identity lost)"))
print(f"\nscar-channel matching: {scar_hits}/{M} = {sa:.0%}  |  shape-channel: {shape_hits}/{M} = {sh:.0%}  |  chance 2.5%")
print(f"VERDICT: {verdict}")
