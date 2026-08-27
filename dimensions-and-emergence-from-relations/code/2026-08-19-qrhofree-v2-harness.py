#!/usr/bin/env python3
# Q-RHO-FREE v2 — per seal 8a042f3. Two legs in one file.
# Leg 1: imposed triad at s in {0.02, 0.05}  (exogenous curve extended down).
# Leg 2: endogenous world instrumented at burn time (triangle survival vs 1-s).
import math, random, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read()
ns = {}
exec(src.rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]

# endogenous mechanics: import from the committed burn harness (single source)
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
bsrc = open(os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")).read()
exec(bsrc.split('def run_world')[0].split("if __name__")[0], bh)
cascade, local_c = bh["cascade"], bh["local_c"]

N = 900
OUT = os.path.join(HERE, "..", "results", "2026-08-19-qrhofree-v2-RAW.log")
def log(m):
    print(m, flush=True)
    with open(OUT, "a") as fh: fh.write(m + "\n")

def mean_c(adj):
    tot = 0.0; n2 = 0
    for v in range(len(adj)):
        if len(adj[v]) >= 2:
            n2 += 1; tot += local_c(adj, v)
    return tot / n2 if n2 else 0.0

def tri_count(adj):
    t = 0
    for v in range(len(adj)):
        nb = [u for u in adj[v] if u > v]
        for i in range(len(nb)):
            for j in range(i + 1, len(nb)):
                if nb[j] in adj[nb[i]]: t += 1
    return t

def stats(xs):
    n = len(xs); m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, math.sqrt(var / n)

# ── LEG 1: imposed triad at small severities ─────────────────────────────────
def leg1():
    log("## LEG 1 — imposed triad at s in {0.02, 0.05} (n=60/arm)")
    for s_ in (0.02, 0.05):
        f = 1.0 - s_
        A, X, B = [], [], []
        for i in range(60):
            r1 = random.Random(30000 + i); A.append(mean_c(grow_prune(rewire(rgg(N, r1), f, r1), r1)))
            r2 = random.Random(31000 + i); a = grow_prune(rewire(rgg(N, r2), f, r2), r2); X.append(mean_c(grow_prune(a, r2)))
            r3 = random.Random(32000 + i); b = grow_prune(rewire(rgg(N, r3), 1.0, r3), r3); B.append(mean_c(grow_prune(rewire(b, f, r3), r3)))
        rng = random.Random(9); vals = []
        for _ in range(4000):
            ia = [rng.randrange(60) for _ in range(60)]
            ma = sum(A[k] for k in ia) / 60; mx = sum(X[k] for k in ia) / 60; mb = sum(B[k] for k in ia) / 60
            if abs(mx - ma) > 1e-12: vals.append((mb - ma) / (mx - ma))
        vals.sort()
        lo, med, hi = vals[int(.025 * len(vals))], vals[len(vals) // 2], vals[int(.975 * len(vals))]
        pred = (1 - s_) ** 2.28
        verdict = "MATCH" if (lo - 0.05) <= pred <= (hi + 0.05) else "MISS"
        log(f"s={s_:.2f}: rho={med:.3f} CI[{lo:.3f},{hi:.3f}]  predicted {pred:.3f}  => {verdict}")

# ── LEG 2: instrumented endogenous world ─────────────────────────────────────
def leg2(T=4000, seed=5001, K=3):
    log(f"\n## LEG 2 — endogenous, instrumented at burn time (T={T}, burn>=30 edges)")
    rng = random.Random(seed)
    adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
    events = []
    for t in range(T):
        touched = []
        for _ in range(K):
            for _ in range(30):
                a = rng.randrange(N); b = rng.randrange(N)
                if a != b and b not in adj[a]:
                    adj[a].add(b); adj[b].add(a); touched += [a, b]; break
        # pre-measure lazily: only worth it if a big burn happens — so measure
        # after drive, before cascade, every tick past transient guard t>1300
        if t > 1300:
            E = sum(len(x) for x in adj) // 2
            Tpre = tri_count(adj)
            burn = cascade(adj, rng, touched)
            if burn >= 30:
                Tpost = tri_count(adj)
                s_ = burn / E
                events.append((s_, Tpre, Tpost))
        else:
            burn = cascade(adj, rng, touched)
        adj = grow_prune(adj, rng, passes=1)
        # v2.1 AMENDMENT (instrument placement only; sealed criteria untouched):
        # the first run found ~ALL big burns are SETTLE-triggered — the gardener's
        # triadic additions light the fires, not the external drive. The pre-measure
        # now brackets this cascade too.
        if t > 1300:
            E2 = sum(len(x) for x in adj) // 2
            Tpre2 = tri_count(adj)
            extra = cascade(adj, rng, range(N))
            if extra >= 30:
                events.append((extra / E2, Tpre2, tri_count(adj)))
        else:
            extra = cascade(adj, rng, range(N))
    log(f"qualifying burns: {len(events)}")
    if len(events) < 100:
        log("VERDICT LEG 2: INSUFFICIENT (<100 qualifying burns)")
        return
    pts = [(math.log(1 - s_), math.log(max(tp, 1) / max(t0, 1))) for s_, t0, tp in events if 0 < s_ < 1 and t0 > 50]
    def slope(sample):
        mx = sum(x for x, _ in sample) / len(sample); my = sum(y for _, y in sample) / len(sample)
        den = sum((x - mx) ** 2 for x, _ in sample)
        return sum((x - mx) * (y - my) for x, y in sample) / den if den else float("nan")
    k_hat = slope(pts)
    rng2 = random.Random(11); ks = []
    for _ in range(2000):
        samp = [pts[rng2.randrange(len(pts))] for _ in range(len(pts))]
        kv = slope(samp)
        if not math.isnan(kv): ks.append(kv)
    ks.sort()
    lo, hi = ks[int(.025 * len(ks))], ks[int(.975 * len(ks))]
    inside = 2.0 <= lo and hi <= 3.0
    overlaps = not (hi < 2.0 or lo > 2.6)
    v = "MATCH" if (inside and overlaps) else ("MISMATCH" if (hi < 2.0 or lo > 3.0) else "UNDECIDED")
    log(f"k_free={k_hat:.2f} CI[{lo:.2f},{hi:.2f}] (n={len(pts)})  sealed bars: within[2,3]={inside} overlaps[2.0,2.6]={overlaps}")
    log(f"VERDICT LEG 2: {v}")
    # secondary descriptive: severity distribution of qualifying burns
    svals = sorted(s_ for s_, _, _ in events)
    log(f"severity range of qualifying burns: {svals[0]:.3f}..{svals[-1]:.3f} median {svals[len(svals)//2]:.3f}")

if __name__ == "__main__":
    leg1()
    leg2()
    log("# DONE")
