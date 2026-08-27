# Verify the SCAR (airtight, matched): is B > A2x on DEGREE DISPERSION (both 2 settles), and does
# it survive rebuild? Also B vs A (bigguy's floor test) for reference. Observables: degree SD (scar),
# clustering (seed). Rebuild = extra grow_prune passes added to each path. SEEDS=50, f=0.65, N=1600.
import random, math, itertools, collections, statistics as st
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
def _ov(adj,i,j):
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
        edges.sort(key=lambda e:_ov(adj,e[0],e[1])); pr=0
        for a,b in edges:
            if pr>=added: break
            if b in adj[a] and len(adj[a])>2 and len(adj[b])>2: adj[a].discard(b); adj[b].discard(a); pr+=1
    return adj
def degSD(adj): d=[len(a) for a in adj]; return st.pstdev(d)
def clus(adj):
    tot=0.0;cnt=0
    for u in range(len(adj)):
        nb=list(adj[u]); dd=len(nb)
        if dd<2: continue
        L=sum(1 for a in range(dd) for b in range(a+1,dd) if nb[b] in adj[nb[a]]); tot+=2*L/(dd*(dd-1)); cnt+=1
    return tot/cnt if cnt else 0
def A(N,f,seed): rng=random.Random(seed); return rewire(rgg(N,rng),f,rng) and grow_prune(rewire(rgg(random.Random(seed).randint(0,0) or N, random.Random(seed)),f,random.Random(seed)),random.Random(seed))
def buildA(N,f,seed): rng=random.Random(seed); return grow_prune(rewire(rgg(N,rng),f,rng),rng)
def buildB(N,f,seed): rng=random.Random(seed); a=grow_prune(rewire(rgg(N,rng),1.0,rng),rng); return grow_prune(rewire(a,f,rng),rng)
def buildA2x(N,f,seed): rng=random.Random(seed); return grow_prune(grow_prune(rewire(rgg(N,rng),f,rng),rng),rng)
SEEDS=50; f=0.65; N=1600
def mean_se(xs): m=st.mean(xs); return m, st.pstdev(xs)/math.sqrt(len(xs)-1)
for q in (0, 42):
    dA=[];dB=[];dX=[]; cA=[];cB=[];cX=[]
    for s in range(SEEDS):
        rgA=random.Random(90000+s); a=buildA(N,f,s);  a=grow_prune(a,rgA,passes=q) if q else a
        rgB=random.Random(91000+s); b=buildB(N,f,1000+s); b=grow_prune(b,rgB,passes=q) if q else b
        rgX=random.Random(95000+s); x=buildA2x(N,f,5000+s); x=grow_prune(x,rgX,passes=q) if q else x
        dA.append(degSD(a));dB.append(degSD(b));dX.append(degSD(x)); cA.append(clus(a));cB.append(clus(b));cX.append(clus(x))
    (mA,eA),(mB,eB),(mX,eX)=mean_se(dA),mean_se(dB),mean_se(dX)
    (kA,_),(kB,_),(kX,_)=mean_se(cA),mean_se(cB),mean_se(cX)
    BA=mB-mA; sBA=math.sqrt(eB**2+eA**2); BX=mB-mX; sBX=math.sqrt(eB**2+eX**2)
    print(f"rebuild q={q}:", flush=True)
    print(f"  DEGREE-SD (scar): A={mA:.3f} B={mB:.3f} A2x={mX:.3f} | B-A={BA:+.3f}({BA/sBA:+.1f}s) | B-A2x={BX:+.3f}({BX/sBX:+.1f}s)  <- >0 = SCAR real (B above matched control)", flush=True)
    print(f"  CLUSTERING (seed): A={kA:.4f} B={kB:.4f} A2x={kX:.4f}  <- B between A and A2x = mixture", flush=True)
print("DONE", flush=True)
