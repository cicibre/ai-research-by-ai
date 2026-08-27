#!/usr/bin/env python3
# DREAM SEALS harness — Seals 1+2 (oracle, horizon) and Seal 3 (identity-under-living).
# Per prereg 2026-08-20-DREAM-SEALS (committed pre-fire). Usage: harness.py oracle | living
import math, random, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
cascade, local_c, BASE, ALPHA = bh["cascade"], bh["local_c"], bh["BASE"], bh["ALPHA"]

N = 900
OUT = os.path.join(HERE, "..", "results", "2026-08-20-dream-seals-RAW.log")
def log(m):
    print(m, flush=True)
    with open(OUT, "a") as fh: fh.write(m + "\n")

def tick(adj, rng, K=3):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = cascade(adj, rng, touched)
    adj2 = grow_prune(adj, rng, passes=1)
    burn += cascade(adj2, rng, range(N))
    return adj2, burn

def load_gauge(adj):
    L = 0.0
    for v in range(N):
        d = len(adj[v])
        if d >= BASE:  # only near-capacity nodes need the (costly) clustering
            c = BASE + ALPHA * local_c(adj, v)
            if d > c - 1: L += max(0.0, d - c + 1)
    return L

def spearman(xs, ys):
    n = len(xs)
    def ranks(v):
        idx = sorted(range(n), key=lambda i: v[i]); r = [0] * n
        for k, i in enumerate(idx): r[i] = k
        return r
    ax, ay = ranks(xs), ranks(ys)
    mx = my = (n - 1) / 2
    cov = sum((a - mx) * (b - my) for a, b in zip(ax, ay))
    s = math.sqrt(sum((a - mx) ** 2 for a in ax) * sum((b - my) ** 2 for b in ay))
    return cov / s if s else float("nan")

def oracle():
    log("## SEAL 1+2 — ORACLE + HORIZON (seed 7001, T=2500)")
    rng = random.Random(7001)
    adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
    gauges, burns = [], []
    clones = {}   # checkpoint t -> (twin adj snapshot for horizon leg)
    CHK = set(1400 + 120 * i for i in range(8))
    twin_series = {}
    for t in range(2500):
        if t in CHK:
            clones[t] = [set(x) for x in adj]
        adj, b = tick(adj, rng)
        burns.append(b)
        if t >= 1300: gauges.append(load_gauge(adj))
        else: gauges.append(None)
    # ORACLE grading
    xs, ys = [], []
    for t in range(1300, 2489):
        L = gauges[t]
        if L is None: continue
        xs.append(L); ys.append(sum(burns[t + 1:t + 11]))
    rho = spearman(xs, ys)
    rng2 = random.Random(99); nulls = []
    for _ in range(200):
        sh = xs[:]; rng2.shuffle(sh)
        nulls.append(spearman(sh, ys))
    nulls.sort(); n95 = nulls[189]
    v = ("ORACLE-CONFIRMED" if (rho >= 0.2 and rho > n95)
         else ("INVERTED" if rho < nulls[10] and rho < -0.2 else "BLIND-WORLD"))
    log(f"SEAL1 ORACLE: Spearman(load, next-10-tick burns) = {rho:+.3f}; shuffled-null 95th = {n95:+.3f} => {v}")
    # HORIZON leg: run twins from each checkpoint with different rng
    horizons = []
    for t0 in sorted(clones):
        twin = clones[t0]; trng = random.Random(50000 + t0)
        tb = []
        for _ in range(240):
            twin, b = tick(twin, trng)
            tb.append(b)
        wb = burns[t0:t0 + 240]
        # window correlation vs lead
        W = 20; leads = []
        for w0 in range(0, 240 - W, W):
            a = wb[w0:w0 + W]; c = tb[w0:w0 + W]
            leads.append((w0 + W // 2, spearman(a, c)))
        h = next((mid for mid, r in leads if r < 0.5), 240)
        horizons.append(h)
        log(f"  horizon@t={t0}: first window-corr<0.5 at lead ~{h} ticks  ({', '.join(f'{m}:{r:+.2f}' for m,r in leads[:4])} ...)")
    horizons.sort()
    med = horizons[len(horizons) // 2]
    log(f"SEAL2 HORIZON: median ~{med} ticks (~{med*8.5/30:.0f} months by the turnover calibration); spread {horizons[0]}–{horizons[-1]}")

def living():
    log("## SEAL 3 — WHAT SURVIVES LIVING (M=40, horizons +300/+1000/+3000)")
    M = 40; HOR = [300, 1000, 3000]
    pre_deg, pre_edge, pre_shape = [], [], []
    post = {h: {"deg": [], "edge": [], "shape": []} for h in HOR}
    def edges_of(adj): return frozenset((a, b) for a in range(N) for b in adj[a] if a < b)
    def shape_of(adj):
        degs = [len(a) for a in adj]; m = sum(degs) / N
        ksd = math.sqrt(sum((d - m) ** 2 for d in degs) / (N - 1))
        tot = 0.0; n2 = 0
        for u in range(N):
            if len(adj[u]) >= 2:
                n2 += 1; tot += local_c(adj, u)
        return [tot / n2 if n2 else 0, m, ksd]
    for i in range(M):
        rng = random.Random(8000 + i)
        adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
        for t in range(1300):
            adj, _ = tick(adj, rng)
        pre_deg.append([len(a) for a in adj]); pre_edge.append(edges_of(adj)); pre_shape.append(shape_of(adj))
        lived = 0
        for h in HOR:
            for _ in range(h - lived):
                adj, _ = tick(adj, rng)
            lived = h
            post[h]["deg"].append([len(a) for a in adj])
            post[h]["edge"].append(edges_of(adj))
            post[h]["shape"].append(shape_of(adj))
        log(f"  world {i} lived to +3000")
    def cos(a, b):
        na = math.sqrt(sum(x * x for x in a)); nb = math.sqrt(sum(x * x for x in b))
        return sum(x * y for x, y in zip(a, b)) / (na * nb) if na * nb else 0
    def jac(a, b):
        u = len(a | b); return len(a & b) / u if u else 0
    import statistics as st
    def zcols(rows):
        cols = list(zip(*rows)); zs = []
        for c in cols:
            m = st.mean(c); s = st.stdev(c) or 1
            zs.append([(x - m) / s for x in c])
        return list(zip(*zs))
    for h in HOR:
        scar = sum(1 for i in range(M) if max(range(M), key=lambda j: cos(post[h]["deg"][i], pre_deg[j])) == i)
        name = sum(1 for i in range(M) if max(range(M), key=lambda j: jac(post[h]["edge"][i], pre_edge[j])) == i)
        prz, poz = zcols(pre_shape), zcols(post[h]["shape"])
        shape = sum(1 for i in range(M) if min(range(M), key=lambda j: sum((a - b) ** 2 for a, b in zip(poz[i], prz[j]))) == i)
        def g(x): return "CARRIES" if x >= 0.25 * M else ("LOST" if x < 0.10 * M else "PARTIAL")
        yrs = {300: 7, 1000: 23, 3000: 70}[h]
        log(f"+{h} ticks (~{yrs}y): SCAR {scar}/{M} [{g(scar)}]  NAME {name}/{M} [{g(name)}]  SHAPE {shape}/{M} [{g(shape)}] (chance 1)")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "oracle"
    (oracle if mode == "oracle" else living)()
    log(f"# {mode} DONE")
