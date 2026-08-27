#!/usr/bin/env python3
# Seed-fraction UP-SWEEP harness — spectral dimension d_s vs geometric-edge fraction f, across N.
# PROVENANCE: original run captured in quant session transcript
#   conversations/2026-08-11-three-nights-dimension-locality-seed.jsonl line 1360
#   tool_result timestamp 2026-08-11T04:26:49Z (tool_use_id toolu_013SmQHzBaiNkWaPtqdDo1iu).
# DETERMINISTIC: random.seed(20260810). Re-run 2026-08-12 by quant reproduces the original
#   table bit-for-bit (see ../results/2026-08-11-seed-fraction-sweep-RAW.txt).
# This is the harness behind ledger-paper item 1 (f_crit table). Flag-1 closure: original raw
#   recovered AND independently reproduced from the recovered seeded code.

import random, math, itertools, collections
random.seed(20260810)
def spectral_dim(adj,T=60,K=6):
    N=len(adj);seen=[False]*N;best=[]
    for s in range(N):
        if seen[s]:continue
        comp=[];st=[s];seen[s]=True
        while st:
            u=st.pop();comp.append(u)
            for v in adj[u]:
                if not seen[v]:seen[v]=True;st.append(v)
        if len(comp)>len(best):best=comp
    if len(best)<40:return None
    idx={u:k for k,u in enumerate(best)};M=len(best)
    ad=[[idx[v] for v in adj[u] if v in idx] for u in best]
    deg=[len(a) for a in ad];dm=[1/math.sqrt(d) if d else 0 for d in deg]
    def Sv(v):
        w=[0.0]*M
        for i in range(M):
            a=0.0
            for j in ad[i]:a+=dm[j]*v[j]
            w[i]=0.5*(v[i]+dm[i]*a)
        return w
    ts=[t for t in [1,2,3,4,6,8,11,15,20,28,38,52] if t<=T];tr={t:0.0 for t in ts}
    for _ in range(K):
        z=[random.choice([-1.0,1.0]) for _ in range(M)];v=z[:]
        for t in range(1,T+1):
            v=Sv(v)
            if t in tr:tr[t]+=sum(z[i]*v[i] for i in range(M))/K
    pts=[(t,tr[t]/M) for t in ts if tr[t]/M>1e-9];win=[(t,vv) for t,vv in pts if t>=4];filt=[]
    for k,(t,vv) in enumerate(win):
        filt.append((t,vv))
        if k>0 and vv>win[k-1][1]*0.98:break
    if len(filt)<3:return None
    xs=[math.log(t) for t,_ in filt];ys=[math.log(v) for _,v in filt];mx=sum(xs)/len(xs);my=sum(ys)/len(ys)
    num=sum((xs[i]-mx)*(ys[i]-my) for i in range(len(xs)));den=sum((x-mx)**2 for x in xs)
    return -2*(num/den if den else 0)
def rgg(N,k=9):
    pos=[(random.random(),random.random()) for _ in range(N)];r=math.sqrt(k/(N*math.pi))
    cell=collections.defaultdict(list);g=max(1,int(1/r));key=lambda p:(min(g-1,int(p[0]*g)),min(g-1,int(p[1]*g)))
    for i,p in enumerate(pos):cell[key(p)].append(i)
    adj=[set() for _ in range(N)]
    for i,p in enumerate(pos):
        ci=key(p)
        for off in itertools.product((-1,0,1),repeat=2):
            c=(ci[0]+off[0],ci[1]+off[1])
            for j in cell.get(c,[]):
                if j>i and (pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2<r*r:adj[i].add(j);adj[j].add(i)
    return adj
def rewire(adj,frac):  # rewire fraction (1-frac) of edges to random long-range -> geometric fraction f=frac
    N=len(adj);edges=[(a,b) for a in range(N) for b in adj[a] if a<b]
    random.shuffle(edges)
    for (a,b) in edges:
        if random.random()>frac and b in adj[a]:
            adj[a].discard(b);adj[b].discard(a)
            for _ in range(10):
                c=random.randrange(N)
                if c!=a and c not in adj[a]:adj[a].add(c);adj[c].add(a);break
    return adj
def ov(adj,i,j):
    a,b=adj[i],adj[j];u=a|b;return len(a&b)/len(u) if u else 0
def grow_prune(adj,passes=6):
    N=len(adj)
    for _ in range(passes):
        nodes=list(range(N));random.shuffle(nodes);added=0
        for u in nodes[:N//4]:
            nb=list(adj[u])
            if len(nb)<2:continue
            x,y=random.sample(nb,2)
            if y not in adj[x]:adj[x].add(y);adj[y].add(x);added+=1
        edges=[(min(a,b),max(a,b)) for a in range(N) for b in adj[a] if a<b]
        edges.sort(key=lambda e:ov(adj,e[0],e[1]))
        pr=0
        for a,b in edges:
            if pr>=added:break
            if b in adj[a] and len(adj[a])>2 and len(adj[b])>2:adj[a].discard(b);adj[b].discard(a);pr+=1
    return adj
print("=== UP-SWEEP (cold start): build at geometric-fraction f, run grow-prune, measure final d_s ===")
print("   low d_s = geometry survived/repaired · high d_s = non-geometric phase")
fs=[0.3,0.5,0.65,0.8,1.0]
hdr="   N     " + "".join(f"f={f:<6}" for f in fs); print(hdr)
for N in [400,900,1600]:
    row=[]
    for f in fs:
        adj=rewire(rgg(N),f);adj=grow_prune(adj);ds=spectral_dim(adj)
        row.append(f"{ds:.2f}" if ds else "none")
    print(f"  {N:5}  " + "".join(f"{row[i]:<8}" for i in range(len(fs))))
print("(steepens with N between the low-f and high-f columns => phase transition; flat across N => crossover)")
print("DONE")
