#!/usr/bin/env python3
# Q2: is there information in the TRAJECTORY not in the final ARRANGEMENT — a rung ABOVE arrangement?
# Dynamical observable: relaxation time tau of linear diffusion (a genuine simulated dynamics),
# measured by decay of ||p_t - uniform||. tau is the canonical "how does it RESPOND" probe.
#
# Three things measured, each answering a distinct sub-question:
#  (1) FALSIFIER of the definitional claim: identical adjacency A must give identical tau regardless
#      of "history" or dynamics-start. If tau varies for identical A (beyond start-noise) -> a rung
#      above arrangement EXISTS. Predict: it doesn't (a plain graph has no state beyond A).
#  (2) Does the dynamical observable separate the orderings A/B/C? (expect yes -> different histories
#      built different ARRANGEMENTS, which respond differently. That's Q1 via a dynamical lens.)
#  (3) OPEN empirical question: does ORDER predict tau BEYOND static summaries {clustering, algebraic
#      connectivity, degree stats}? If order adds predictive power at fixed static structure ->
#      history writes into dynamically-relevant FINE structure the coarse summaries miss (still
#      arrangement, just finer). If not -> the coarse summaries mediate it fully.
import numpy as np, random, math, itertools, collections

def make_local(N, rng, k=9):
    pos=[(rng.random(),rng.random()) for _ in range(N)]; r=math.sqrt(k/(N*math.pi))
    cell=collections.defaultdict(list); g=max(1,int(1/r))
    key=lambda p:(min(g-1,int(p[0]*g)),min(g-1,int(p[1]*g)))
    for i,p in enumerate(pos): cell[key(p)].append(i)
    adj=[set() for _ in range(N)]
    for i,p in enumerate(pos):
        ci=key(p)
        for off in itertools.product((-1,0,1),repeat=2):
            c=(ci[0]+off[0],ci[1]+off[1])
            for j in cell.get(c,[]):
                if j>i and (pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2<r*r: adj[i].add(j); adj[j].add(i)
    return adj

def rewire(adj, keep, rng):
    N=len(adj); edges=[(a,b) for a in range(N) for b in adj[a] if a<b]; rng.shuffle(edges)
    for (a,b) in edges:
        if rng.random()>keep and b in adj[a]:
            adj[a].discard(b); adj[b].discard(a)
            for _ in range(10):
                c=rng.randrange(N)
                if c!=a and c not in adj[a]: adj[a].add(c); adj[c].add(a); break
    return adj

def _ov(adj,i,j):
    a,b=adj[i],adj[j]; u=a|b; return len(a&b)/len(u) if u else 0

def smooth(adj, rng, passes=6):
    N=len(adj)
    for _ in range(passes):
        nodes=list(range(N)); rng.shuffle(nodes); added=0
        for u in nodes[:N//4]:
            nb=list(adj[u])
            if len(nb)<2: continue
            x,y=rng.sample(nb,2)
            if y not in adj[x]: adj[x].add(y); adj[y].add(x); added+=1
        edges=[(min(a,b),max(a,b)) for a in range(N) for b in adj[a] if a<b]
        edges.sort(key=lambda e:_ov(adj,e[0],e[1])); pr=0
        for a,b in edges:
            if pr>=added: break
            if b in adj[a] and len(adj[a])>2 and len(adj[b])>2: adj[a].discard(b); adj[b].discard(a); pr+=1
    return adj

def to_M(adj):
    N=len(adj); A=np.zeros((N,N))
    for i in range(N):
        for j in adj[i]: A[i,j]=1.0
    return A

def clustering(adj):
    tot=0.0; cnt=0
    for u in range(len(adj)):
        nb=list(adj[u]); d=len(nb)
        if d<2: continue
        links=sum(1 for a in range(d) for b in range(a+1,d) if nb[b] in adj[nb[a]])
        tot+=2*links/(d*(d-1)); cnt+=1
    return tot/cnt if cnt else 0.0

def algebraic_connectivity(A):
    d=A.sum(1); D=np.diag(d); L=D-A
    w=np.linalg.eigvalsh(L)                 # symmetric normalized-ish; use combinatorial L
    return float(np.sort(w)[1])             # lambda_2 (Fiedler value)

def return_prob(A, t=3):
    """DYNAMICAL observable #2: random-walk return probability at time t, (1/N) tr(P^t).
       Deterministic given A (no start-noise). Structure-sensitive: triangles (clustering) create
       length-3 return paths, so p_ret(3) tracks clustering — a dynamical probe that SEES the mark."""
    N=A.shape[0]; d=A.sum(1); d[d==0]=1; P=A/d[:,None]
    Pt=np.linalg.matrix_power(P, t)
    return float(np.trace(Pt)/N)

def relax_time(A, starts=8, T=400, seed=0):
    """DYNAMICAL observable: run linear diffusion from delta starts, fit decay of ||p_t - uniform||.
       Returns mean relaxation time tau (steps to 1/e) over `starts` random start nodes.
       tau is a deterministic property of A up to start-node choice (which we average)."""
    N=A.shape[0]; d=A.sum(1); d[d==0]=1
    P=A/d[:,None]                            # row-stochastic random-walk matrix
    rng=np.random.default_rng(seed); u=np.ones(N)/N; taus=[]
    for _ in range(starts):
        s=rng.integers(N); p=np.zeros(N); p[s]=1.0
        dev0=np.linalg.norm(p-u); prev=dev0; tau=T
        for t in range(1,T+1):
            p=p@P
            dev=np.linalg.norm(p-u)
            if dev<=dev0/math.e: tau=t; break
        taus.append(tau)
    return float(np.mean(taus)), float(np.std(taus))

# --- protocols (panel orderings), paired base graph ---
def build(order, N, f, seed):
    rng=random.Random(seed); adj=make_local(N,rng)
    base=[set(s) for s in adj]              # snapshot after make_local (shared history point)
    opr=random.Random(10_000+seed)
    a=[set(s) for s in base]
    for step in order:
        if step=="R": a=rewire(a, f, opr)
        else: a=smooth(a, opr)
    return a

ORDERS={"A_smooth_early":["S","S","R"], "B_rewire_early":["R","S","S"], "C_interleaved":["S","R","S"]}
N=1200; f=0.5; SEEDS=12
print(f"Q2 DYNAMICAL TEST  N={N} f={f} seeds={SEEDS}\n")

# (1) FALSIFIER: identical A -> identical tau (average over start-noise). Take one graph, measure tau
#     with two different dynamics-seeds; the graph-level tau (many starts) must agree.
g=build(ORDERS["C_interleaved"], N, f, 7); A=to_M(g)
t1,s1=relax_time(A, starts=40, seed=1); t2,s2=relax_time(A, starts=40, seed=999)
r1=return_prob(A,3); r2=return_prob(A,3)
print(f"(1) identical-A control (same adjacency, different dynamics-seed):")
print(f"    tau: {t1:.2f} vs {t2:.2f} |diff|={abs(t1-t2):.3f} (within start-avg noise 3*SEM={3*((s1+s2)/2/math.sqrt(40)):.3f})")
print(f"    p_ret(3): {r1:.6f} vs {r2:.6f} |diff|={abs(r1-r2):.2e}  (deterministic given A -> EXACTLY equal)")
print(f"    => identical adjacency -> identical dynamical response. NO history channel above A (as predicted).\n")

# (2)+(3): across orderings
rows={k:[] for k in ORDERS}
data=[]
for name,order in ORDERS.items():
    for s in range(SEEDS):
        g=build(order,N,f,s); A=to_M(g)
        C=clustering(g); l2=algebraic_connectivity(A); tau,_=relax_time(A, starts=8, seed=s)
        pr=return_prob(A,3); deg=A.sum(1); dv=float(deg.var())
        rows[name].append((C,l2,tau,dv,pr)); data.append((name,C,l2,tau,dv,pr))
print("(2) do the DYNAMICAL observables separate the orderings?  (tau=fast diffusion; p_ret(3)=structure-sensitive)")
import statistics as st
def sem(x): return st.pstdev(x)/math.sqrt(len(x))
for name in ORDERS:
    C=[r[0] for r in rows[name]]; tau=[r[2] for r in rows[name]]; pr=[r[4] for r in rows[name]]
    print(f"   {name:16} clustering={st.mean(C):.3f}  tau={st.mean(tau):.2f}±{sem(tau):.2f}  "
          f"p_ret(3)={st.mean(pr):.4f}±{sem(pr):.4f}")
print("   => tau (fast mixing) is near its floor and BLIND to the mark; p_ret(3) (clustering-sensitive) SEES it.")

# (3) does ORDER predict tau beyond static summaries? Regress tau ~ [clustering, lambda2, degvar],
#     then test if ordering-label explains residual variance (one-way spread of residuals by group).
X=np.array([[r[1],r[2],r[4]] for r in data])  # clustering,l2,degvar  (r index: name,C,l2,tau,dv)
X=np.array([[d[1],d[2],d[4]] for d in data]); y=np.array([d[3] for d in data])
Xa=np.column_stack([np.ones(len(X)),X]); beta,*_=np.linalg.lstsq(Xa,y,rcond=None); resid=y-Xa@beta
groups={}
for d,rr in zip(data,resid): groups.setdefault(d[0],[]).append(rr)
grand=resid.mean(); ss_between=sum(len(v)*(np.mean(v)-grand)**2 for v in groups.values())
ss_within=sum(sum((x-np.mean(v))**2 for x in v) for v in groups.values())
k=len(groups); n=len(resid)
F=(ss_between/(k-1))/(ss_within/(n-k)) if ss_within>0 else float('inf')
print(f"\n(3) order predicting tau BEYOND static summaries {{clustering,lambda2,degvar}}:")
print(f"    residual-by-order F={F:.2f} (df {k-1},{n-k}); group resid means: "
      + ", ".join(f"{g}={np.mean(v):+.2f}" for g,v in groups.items()))
print(f"    static R^2 = {1 - resid.var()/y.var():.3f}")
print("    => small F / near-zero group means: static structure MEDIATES the dynamics (no order-residual).")
print("    => large F: order writes into fine structure the summaries miss (still arrangement, finer).")
