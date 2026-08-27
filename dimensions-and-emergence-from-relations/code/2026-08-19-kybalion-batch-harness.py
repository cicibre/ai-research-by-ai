#!/usr/bin/env python3
# KYBALION batch — K-VIBRATION, K-GENDER, K-CORRESPONDENCE per seal 642e43c.
import math, random, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
cascade, local_c = bh["cascade"], bh["local_c"]

OUT = os.path.join(HERE, "..", "results", "2026-08-19-kybalion-batch-RAW.log")
def log(m):
    print(m, flush=True)
    with open(OUT, "a") as fh: fh.write(m + "\n")

def mean_c(adj):
    tot = 0.0; n2 = 0
    for v in range(len(adj)):
        if len(adj[v]) >= 2: n2 += 1; tot += local_c(adj, v)
    return tot / n2 if n2 else 0.0

def edges_set(adj):
    return set((a, b) for a in range(len(adj)) for b in adj[a] if a < b)

def tick(adj, rng, N, K=3, mode="full"):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = cascade(adj, rng, touched)
    if mode == "full":
        adj = grow_prune(adj, rng, passes=1)
    elif mode == "grow":   # generative half only: triadic closure adds, no pruning
        nodes = list(range(N)); rng.shuffle(nodes)
        for u in nodes[:N // 4]:
            nb = list(adj[u])
            if len(nb) < 2: continue
            x, y = rng.sample(nb, 2)
            if y not in adj[x]: adj[x].add(y); adj[y].add(x)
    elif mode == "prune":  # receptive half only: prune lowest-overlap, no adding
        def ov(i, j):
            a, b = adj[i], adj[j]; u = a | b
            return len(a & b) / len(u) if u else 0
        edges = [(min(a, b), max(a, b)) for a in range(N) for b in adj[a] if a < b]
        edges.sort(key=lambda e: ov(*e))
        pr = 0
        for a, b in edges:
            if pr >= N // 4: break
            if b in adj[a] and len(adj[a]) > 2 and len(adj[b]) > 2:
                adj[a].discard(b); adj[b].discard(a); pr += 1
    burn += cascade(adj, rng, range(N))
    return adj, burn

def run(N, T, seed, mode="full", track_from=None, track_len=300):
    rng = random.Random(seed)
    adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
    burns, Cs = [], []
    marked, lifetimes, mark_t = None, [], None
    for t in range(T):
        adj, b = tick(adj, rng, N, mode=mode)
        burns.append(b)
        if t % 10 == 0: Cs.append(mean_c(adj))
        if track_from is not None:
            if t == track_from:
                marked = edges_set(adj); mark_t = t
            elif marked is not None and t <= track_from + track_len:
                cur = edges_set(adj)
                gone = {e for e in marked if e not in cur}
                for e in gone: lifetimes.append(t - mark_t)
                marked -= gone
    return burns, Cs, (lifetimes, len(marked) if marked is not None else 0)

log("# KYBALION batch (seal 642e43c)")

# ── K-VIBRATION: Ship of Theseus at stationarity ─────────────────────────────
burns, Cs, (lifetimes, survivors) = run(900, 1300 + 320, 6001, track_from=1300, track_len=300)
post_c = Cs[130:]
c_mean = sum(post_c) / len(post_c)
band_ok = all(abs(c - c_mean) / c_mean <= 0.05 for c in post_c)
total_marked = len(lifetimes) + survivors
lifetimes.sort()
if len(lifetimes) >= total_marked / 2:
    med_life = lifetimes[total_marked // 2 - 1] if total_marked // 2 - 1 < len(lifetimes) else None
else:
    med_life = None   # median beyond window: majority of edges survived 300 ticks
turnover = len(lifetimes) / total_marked if total_marked else 0
if not band_ok:
    v = "INSUFFICIENT (C band violated — not at stationarity)"
elif med_life is not None:
    v = f"VIBRATION-CONFIRMED (median edge lifetime {med_life} ticks; turnover {turnover:.0%}; C within ±5%)"
else:
    v = f"REFUTED (median lifetime beyond 300-tick window; turnover only {turnover:.0%})"
log(f"\nK-VIBRATION: marked {total_marked} edges at stationarity; {len(lifetimes)} died in 300 ticks ({turnover:.0%}); C band ±5% held={band_ok}")
log(f"VERDICT K-VIBRATION: {v}")

# ── K-GENDER: ablation arms ──────────────────────────────────────────────────
log("\nK-GENDER (800 ticks per arm):")
results = {}
for mode, seed in (("full", 6101), ("grow", 6102), ("prune", 6103)):
    b2, C2, _ = run(900, 800, seed, mode=mode)
    cfin = sum(C2[-20:]) / 20
    efin = "n/a"
    results[mode] = cfin
    log(f"  {mode}: final C={cfin:.3f}  (burn-rate {sum(1 for x in b2 if x>0)/len(b2):.2f})")
full_c = results["full"]
g_deg = results["grow"] < 0.5 * full_c
p_deg = results["prune"] < 0.5 * full_c
v = ("GENDER-CONFIRMED (both ablations degrade below half)" if (g_deg and p_deg)
     else "REFUTED (a single-natured world matched the full one)" if (not g_deg or not p_deg) and max(results["grow"], results["prune"]) >= 0.9 * full_c
     else f"PARTIAL (grow-only {'degraded' if g_deg else 'held'}, prune-only {'degraded' if p_deg else 'held'} — outside both sealed branches, reported as printed)")
log(f"VERDICT K-GENDER: {v}")

# ── K-CORRESPONDENCE: scale invariance ───────────────────────────────────────
log("\nK-CORRESPONDENCE (N=450, N=1800; T=3000):")
for N2, seed in ((450, 6201), (1800, 6202)):
    b3, C3, _ = run(N2, 3000, seed)
    rec = {"label": f"corr-N{N2}", "burns": b3}
    json.dump(rec, open(os.path.join(HERE, "..", "results", "endogenous-burns", f"corr-N{N2}.json"), "w"))
    cfin = sum(C3[-30:]) / 30
    log(f"  N={N2}: stationary C={cfin:.3f} (N=900 reference 0.86; within ±0.10: {abs(cfin-0.86)<=0.10})")
log("  (tail verdicts: run tail-analysis-CSN.py on corr-N450.json / corr-N1800.json)")
log("# BATCH DONE")
