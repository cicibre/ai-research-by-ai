#!/usr/bin/env python3
# RUNG-4 TEST: is "arrangement" terminal, or is TRAJECTORY a real rung above it?
# ============================================================================
# The ladder (from the 2026-08-11 arc): difference -> relation -> arrangement.
# Rung 4 candidate: TRAJECTORY = the difference BETWEEN arrangements (history/path).
# It is a REAL rung iff it carries information no single arrangement holds — i.e.
# two systems with the SAME current arrangement but DIFFERENT histories behave
# differently. That is exactly HYSTERESIS / path-dependence.
#
# Operationalized on the relational-growth model (recovered harness, pure stdlib):
#   UP   (cold start): build at geometric fraction f_test, grow-prune, measure d_s.
#   DOWN (established): build at f=1.0, grow-prune (ESTABLISH geometry), THEN rewire
#         down to f_test, grow-prune again, measure d_s.
#   Low d_s = geometry survived. If established geometry DEFENDS itself below f_crit,
#   DOWN d_s < UP d_s at the same f  ->  the current arrangement does NOT determine
#   the outcome; the history does  ->  TRAJECTORY IS A REAL RUNG.
#
# PRE-REGISTERED CRITERIA (sealed before running; the arc saw a suggestive-but-noisy
# DOWN<UP hint at f=0.5, and the ESTIMATOR bounces +-0.5 single-run, so seed-averaging
# is mandatory). f_crit ~ 0.72, so f_test below it is the defended region.
#   H_RUNG4 (trajectory real):  gap = mean(UP) - mean(DOWN) > 0 at f_test,
#       AND |gap| > 2 * SEM_gap  (survives seed-averaging),
#       AND the gap WIDENS from N=400 to N=900 (a real rung sharpens with scale).
#   H_TERMINAL (arrangement terminal): gap within noise (|gap| <= 2*SEM_gap),
#       OR does not widen with N -> history washes out, state-only.
#   INSUFFICIENT_POWER (third outcome, mandatory): 2*SEM_gap still larger than the
#       gap magnitude at the max seeds run -> cannot decide; report as such, not as H_TERMINAL.
# SEEDS=15 per (path, f, N). f_test = 0.5 (arc's hint point) and 0.65 (arc's anti-hint).
# ============================================================================
import random, math, itertools, collections

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

def rewire(adj, frac, rng):  # keep fraction `frac` geometric; rewire the rest long-range
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
    adj=rewire(rgg(N,rng), 1.0, rng); adj=grow_prune(adj, rng)      # ESTABLISH at f=1
    adj=rewire(adj, f, rng); adj=grow_prune(adj, rng)               # DRAG down to f, re-settle
    return spectral_dim(adj, seed=seed*7+2)

def stats(xs):
    xs=[x for x in xs if x is not None]; n=len(xs)
    if n<2: return (float('nan'),float('nan'),n)
    m=sum(xs)/n; var=sum((x-m)**2 for x in xs)/(n-1); return (m, math.sqrt(var/n), n)  # mean, SEM, n

SEEDS=15
print("RUNG-4 / TRAJECTORY hysteresis test — seed-averaged, N-companion")
print(f"seeds={SEEDS} per cell; UP=cold start, DOWN=establish-at-1-then-drag; low d_s=geometry survived\n")
print(f"{'N':>5} {'f':>5} {'UP(SEM)':>14} {'DOWN(SEM)':>14} {'gap=UP-DOWN':>12} {'2*SEM_gap':>10} {'verdict':>18}")
results={}
for f in (0.5, 0.65):
    for N in (400, 900):
        up=[up_path(N,f,s) for s in range(SEEDS)]
        dn=[down_path(N,f,s+1000) for s in range(SEEDS)]
        um,ue,un=stats(up); dm,de,dn_=stats(dn)
        gap=um-dm; sem_gap=math.sqrt(ue**2+de**2); thr=2*sem_gap
        if abs(gap)<=thr: v="within noise"
        elif gap>0: v="DOWN<UP (defends)"
        else: v="DOWN>UP (anti)"
        results[(f,N)]=(gap,thr,v)
        print(f"{N:>5} {f:>5.2f} {um:>7.2f}({ue:>4.2f}) {dm:>7.2f}({de:>4.2f}) {gap:>12.3f} {thr:>10.3f} {v:>18}")
    # widening check across N at this f
    g4,t4,_=results[(f,400)]; g9,t9,_=results[(f,900)]
    widen = "WIDENS" if (g9>g4 and g4>0) else ("narrows/flat" if g4>0 else "n/a(no gap@400)")
    print(f"   -> f={f}: gap 400->900 = {g4:.3f} -> {g9:.3f}  [{widen}]\n")
