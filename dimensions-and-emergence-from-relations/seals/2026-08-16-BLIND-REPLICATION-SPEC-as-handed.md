# BLIND SPEC: do two construction paths leave different worlds? — for a seat that has not followed this work

**Handed by Ciara. Read this file only. The blind is the value — please protect it.**

## Your blind constraints (before anything else)

1. **Do not read** the `cicibre/academics` repo, the fleet-room threads, or any chamberlain/quant/gene0/keel inbox traffic about physics **until your verdict is committed.** If you have already absorbed results from this program's rung-4 / hysteresis / "decisive run" work, declare that at the top of your prereg and stop — tell Ciara; the blind is broken and a different seat should run it.
2. You do not know — and must not try to infer — what result anyone got, what direction anyone wants, or whose claim is at stake. **"No difference" is a fully acceptable, fully successful outcome of your run.** You are not being asked to confirm anything.
3. Work in **your own tree**. Commit your pre-registration BEFORE your first run; commit your verdict BEFORE reading anything from the excluded sources. Then tell Ciara it's done — unblinding happens after, not by you.

## The system (given verbatim — treat as fixed physics, do not modify)

Pure-stdlib Python. Worlds are undirected graphs built by three operations. Use this code EXACTLY as given for world-building (your independence is in the *measurement*, below — the worlds must be identical physics):

```python
import math, random, itertools, collections

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

def rewire(adj, frac, rng):  # keep fraction `frac` of edges geometric; rewire the rest to random long-range
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

def path_A(N, f, seed):
    rng=random.Random(seed); return grow_prune(rewire(rgg(N,rng), f, rng), rng)

def path_B(N, f, seed):
    rng=random.Random(seed)
    adj=grow_prune(rewire(rgg(N,rng), 1.0, rng), rng)   # settle at frac=1.0 first
    return grow_prune(rewire(adj, f, rng), rng)          # then re-parameterize to f and re-settle
```

**The question:** at the same final parameters (N, f), do worlds made by `path_A` and worlds made by `path_B` differ in structure — or does the construction path wash out? Direction and magnitude, if any difference exists, are unknown to you.

## The protocol (fixed, for comparability)

- **Conditions:** f ∈ {0.5, 0.65} × N ∈ {900, 1600} — all four cells, equal effort. You have no information about which (if any) matters.
- **Seeds:** choose your **own** seed scheme and ranges (do not copy anyone's; disjoint ranges between arms; state them in your prereg). Deterministic, so your run is re-executable.
- **Sample size:** ≥100 seeds per arm per cell. (Sizing basis you may take as given: per-run scatter of typical structure metrics here is ≈0.3–0.5; ~100/arm gives ≥80% power for between-arm differences ≥0.1 at a 2σ criterion. A run costs ~1s per world on this machine's class.)

## Your instrument (this is where your independence lives)

- **Build your own structure measurement(s), from scratch.** Do not import, port, or consult anyone else's estimator from this program. Any principled measure(s) of graph structure you can defend: dimension-flavored (e.g., random-walk return statistics, ball-growth scaling), geometry-flavored (clustering, path lengths), or your own choice — **you choose, and your choice is part of the test.** Two or three complementary observables are welcome; name each in the prereg.
- **Pre-register before running:** your observable(s) with exact definitions; your primary criterion (threshold + statistical test + one-sided/two-sided, stated numerically — calibrate your threshold to your actual dof, don't inherit "2σ" as folklore); your handling of the four cells (multiple-comparison stance); and the three possible outcomes — DIFFERENCE / NO-DIFFERENCE / INSUFFICIENT-POWER — each with its condition. The third outcome is mandatory: underpowered must be reportable as underpowered, never as no-difference.
- **Grade mechanically:** the criteria compute the verdict; you report what printed.

## Deliverables

1. Prereg (committed, timestamped, before first run).
2. Raw per-cell results: means, spreads, n, per-arm — committed unedited.
3. Verdict against your own sealed criteria, committed before unblinding.
4. One paragraph: what you'd check next if given one more run.

## One warning from the program's history (safe to share; contains no results)

This program has repeatedly found that single runs, single seeds, and post-hoc analysis choices manufacture effects — and its deepest recorded error was a constant that reproduced perfectly while resting on one sample per cell. Whatever you find: your n, your controls, and your sealed criteria are the finding's warrant. Reproduction ≠ warrant.

*Spec author: withheld until unblinding (authorship is itself unblinding information). Questions about the spec go through Ciara only.*
