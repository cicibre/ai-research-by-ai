#!/usr/bin/env python3
# RUNG-4 DECISIVE hysteresis run. Same sealed 2-sigma bar as the PREREG; more power.
# Extends the pre-registered test: N in {900, 1600}, SEEDS=25, f near f_crit.
#   H_RUNG4 : gap=UP-DOWN>0, |gap|>2*SEM_gap at N=1600, AND gap widens 900->1600.
#   H_TERMINAL: gap within noise at N=1600, OR does not widen (washes out).
#   INSUFFICIENT_POWER: 2*SEM_gap still >= |gap| at N=1600 with SEEDS seeds.
# Config via env: N_LIST, F_LIST, SEEDS, OUT. Writes results to OUT as it goes (resumable-ish log).
import random, math, itertools, collections, os, sys, json

def spectral_dim(adj, T=60, K=6, seed=0):
    rng = random.Random(seed)
    N=len(adj); seen=[False]*N; best=[]
    for s in range(N):
        if seen[s]: continue
        comp=[]; st=[s]; seen[s]=True
        while st:
            u=st.pop(); comp.append(u)
            for v in adj[u]:
                if not seen[v]: seen[v]=True; st.append(v)
        if len(comp)>len(best): best=comp
    if len(best)<40: return None
    idx={u:k for k,u in enumerate(best)}; M=len(best)
    ad=[[idx[v] for v in adj[u] if v in idx] for u in best]
    deg=[len(a) for a in ad]; dm=[1/math.sqrt(d) if d else 0 for d in deg]
    def Sv(v):
        w=[0.0]*M
        for i in range(M):
            a=0.0
            for j in ad[i]: a+=dm[j]*v[j]
            w[i]=0.5*(v[i]+dm[i]*a)
        return w
    ts=[t for t in [1,2,3,4,6,8,11,15,20,28,38,52] if t<=T]; tr={t:0.0 for t in ts}
    for _ in range(K):
        z=[rng.choice([-1.0,1.0]) for _ in range(M)]; v=z[:]
        for t in range(1,T+1):
            v=Sv(v)
            if t in tr: tr[t]+=sum(z[i]*v[i] for i in range(M))/K
    pts=[(t,tr[t]/M) for t in ts if tr[t]/M>1e-9]; win=[(t,vv) for t,vv in pts if t>=4]; filt=[]
    for k,(t,vv) in enumerate(win):
        filt.append((t,vv))
        if k>0 and vv>win[k-1][1]*0.98: break
    if len(filt)<3: return None
    xs=[math.log(t) for t,_ in filt]; ys=[math.log(v) for _,v in filt]
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    num=sum((xs[i]-mx)*(ys[i]-my) for i in range(len(xs))); den=sum((x-mx)**2 for x in xs)
    return -2*(num/den if den else 0)

def rgg(N, rng, k=9):
    pos=[(rng.random(),rng.random()) for _ in range(N)]; r=math.sqrt(k/(N*math.pi))
    cell=collections.defaultdict(list); g=max(1,int(1/r)); key=lambda p:(min(g-1,int(p[0]*g)),min(g-1,int(p[1]*g)))
    for i,p in enumerate(pos): cell[key(p)].append(i)
    adj=[set() for _ in range(N)]
    for i,p in enumerate(pos):
        ci=key(p)
        for off in itertools.product((-1,0,1),repeat=2):
            c=(ci[0]+off[0],ci[1]+off[1])
            for j in cell.get(c,[]):
                if j>i and (pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2<r*r: adj[i].add(j); adj[j].add(i)
    return adj

def rewire(adj, frac, rng):
    N=len(adj); edges=[(a,b) for a in range(N) for b in adj[a] if a<b]; rng.shuffle(edges)
    for (a,b) in edges:
        if rng.random()>frac and b in adj[a]:
            adj[a].discard(b); adj[b].discard(a)
            for _ in range(10):
                c=rng.randrange(N)
                if c!=a and c not in adj[a]: adj[a].add(c); adj[c].add(a); break
    return adj

def ov(adj,i,j):
    a,b=adj[i],adj[j]; u=a|b; return len(a&b)/len(u) if u else 0

def grow_prune(adj, rng, passes=6):
    N=len(adj)
    for _ in range(passes):
        nodes=list(range(N)); rng.shuffle(nodes); added=0
        for u in nodes[:N//4]:
            nb=list(adj[u])
            if len(nb)<2: continue
            x,y=rng.sample(nb,2)
            if y not in adj[x]: adj[x].add(y); adj[y].add(x); added+=1
        edges=[(min(a,b),max(a,b)) for a in range(N) for b in adj[a] if a<b]
        edges.sort(key=lambda e:ov(adj,e[0],e[1])); pr=0
        for a,b in edges:
            if pr>=added: break
            if b in adj[a] and len(adj[a])>2 and len(adj[b])>2: adj[a].discard(b); adj[b].discard(a); pr+=1
    return adj

def up_path(N, f, seed):
    rng=random.Random(seed); adj=rewire(rgg(N,rng), f, rng); adj=grow_prune(adj, rng)
    return spectral_dim(adj, seed=seed*7+1)

def down_path(N, f, seed):
    rng=random.Random(seed)
    adj=rewire(rgg(N,rng), 1.0, rng); adj=grow_prune(adj, rng)
    adj=rewire(adj, f, rng); adj=grow_prune(adj, rng)
    return spectral_dim(adj, seed=seed*7+2)

def stats(xs):
    xs=[x for x in xs if x is not None]; n=len(xs)
    if n<2: return (float('nan'),float('nan'),n)
    m=sum(xs)/n; var=sum((x-m)**2 for x in xs)/(n-1); return (m, math.sqrt(var/n), n)

N_LIST=[int(x) for x in os.environ.get("N_LIST","900,1600").split(",")]
F_LIST=[float(x) for x in os.environ.get("F_LIST","0.5,0.6,0.65").split(",")]
SEEDS=int(os.environ.get("SEEDS","25"))
OUT=os.environ.get("OUT","/Users/cc/quant/findings/2026-08-15-rung4-DECISIVE-results.log")

def log(msg):
    print(msg, flush=True)
    with open(OUT,"a") as fh: fh.write(msg+"\n")

log(f"# RUNG-4 DECISIVE  seeds={SEEDS}  N={N_LIST}  f={F_LIST}  (sealed bar: |gap|>2*SEM AND widens)")
results={}
for f in F_LIST:
    for N in N_LIST:
        up=[up_path(N,f,s) for s in range(SEEDS)]
        dn=[down_path(N,f,s+1000) for s in range(SEEDS)]
        um,ue,un=stats(up); dm,de,dn_=stats(dn)
        gap=um-dm; sem=math.sqrt(ue**2+de**2); sig = gap/sem if sem>0 else float('nan')
        results[(f,N)]=(gap,sem,sig,um,dm)
        log(f"f={f:.2f} N={N:>5} | UP={um:.3f}±{ue:.3f}(n={un}) DOWN={dm:.3f}±{de:.3f}(n={dn_}) "
            f"| gap={gap:+.3f} 2SEM={2*sem:.3f} sigma={sig:+.2f}")
    if (f,N_LIST[0]) in results and (f,N_LIST[-1]) in results:
        g0=results[(f,N_LIST[0])][0]; g1=results[(f,N_LIST[-1])][0]
        s1=results[(f,N_LIST[-1])][2]
        widen = g1>g0 and g0>=0
        verdict = ("H_RUNG4 (clears 2s + widens)" if (s1>=2 and widen) else
                   "INSUFFICIENT (sub-2s)" if abs(s1)<2 else
                   "H_TERMINAL/anti" )
        log(f"  => f={f}: gap {N_LIST[0]}->{N_LIST[-1]} = {g0:+.3f} -> {g1:+.3f}  widen={widen}  "
            f"bigN_sigma={s1:+.2f}  => {verdict}\n")
log("# DONE")
