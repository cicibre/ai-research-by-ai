#!/usr/bin/env python3
# MYTH BATTERY — four sealed experiments per myth-models/2026-08-16-MYTH-BATTERY-PREREG.md
# (seal commit 923374d, BEFORE this harness ran). World physics loaded verbatim from the
# committed 08-15 harness. N=900, f=0.65, n=60/arm, seeds per prereg. Verdicts mechanical.
import math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read()
ns = {}
exec(src.rsplit("\nSEEDS=15", 1)[0], ns)
sdim, rgg, rewire, grow_prune, ov = ns["spectral_dim"], ns["rgg"], ns["rewire"], ns["grow_prune"], ns["ov"]

N, F, NARM = 900, 0.65, 60
OUT = os.path.join(HERE, "..", "results", "2026-08-16-myth-battery-RAW.log")

def log(m):
    print(m, flush=True)
    with open(OUT, "a") as fh: fh.write(m + "\n")

def stats(xs):
    xs = [x for x in xs if x is not None]; n = len(xs); m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, math.sqrt(var / n), n

def contrast(name, a, b, la, lb, low_verdict, high_verdict, mid_verdict):
    am, ae, _ = stats(a); bm, be, _ = stats(b)
    d = am - bm; sem = math.sqrt(ae * ae + be * be)
    v = low_verdict if d < -2 * sem else (high_verdict if d > 2 * sem else mid_verdict)
    log(f"  {name}: {la}={am:.3f}±{ae:.3f} {lb}={bm:.3f}±{be:.3f} | diff={d:+.3f} sigma={d/sem:+.2f} => {v}")
    return v

def ksd(adj):
    degs = [len(a) for a in adj]; m = sum(degs) / len(degs)
    return math.sqrt(sum((d - m) ** 2 for d in degs) / (len(degs) - 1))

log(f"# MYTH BATTERY  N={N} f={F} n={NARM}/arm  (seal 923374d)")

# ---- E1 KINTSUGI: second burn on burned vs matched-budget never-burned ----
log("\n## E1 KINTSUGI — the second burn")
kb_final, ka_final, kb_delta, ka_delta = [], [], [], []
for s in range(NARM):
    rng = random.Random(7000 + s)
    adj = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)          # establish
    adj = grow_prune(rewire(adj, F, rng), rng)                    # first burn + settle -> K-B world
    pre = sdim(adj, seed=(7000 + s) * 7 + 2)
    adj = grow_prune(rewire(adj, F, rng), rng)                    # SECOND burn + settle
    post = sdim(adj, seed=(7000 + s) * 7 + 4)
    if pre is not None and post is not None:
        kb_final.append(post); kb_delta.append(post - pre)
for s in range(NARM):
    rng = random.Random(8000 + s)
    adj = grow_prune(rewire(rgg(N, rng), F, rng), rng)
    adj = grow_prune(adj, rng)                                    # matched budget, never burned
    pre = sdim(adj, seed=(8000 + s) * 7 + 3)
    adj = grow_prune(rewire(adj, F, rng), rng)                    # identical second burn + settle
    post = sdim(adj, seed=(8000 + s) * 7 + 5)
    if pre is not None and post is not None:
        ka_final.append(post); ka_delta.append(post - pre)
contrast("PRIMARY final d_s", kb_final, ka_final, "K-B", "K-A2x",
         "TEMPERED (burned arm more geometric after burn 2)",
         "FATIGUED (burned arm worse after burn 2)", "NO-MEMORY-OF-BURN")
dm, de, _ = stats(kb_delta); am2, ae2, _ = stats(ka_delta)
log(f"  secondary damage-response: dDelta K-B={dm:+.3f}±{de:.3f}  K-A2x={am2:+.3f}±{ae2:.3f}")

# ---- E2 FIVE SUNS vs AGES: iterated burn-rebuild cycles ----
log("\n## E2 FIVE SUNS vs AGES OF MAN — iterated cycles")
cyc_ds = [[] for _ in range(5)]; cyc_ksd = [[] for _ in range(5)]
for s in range(NARM):
    rng = random.Random(9000 + s)
    adj = grow_prune(rewire(rgg(N, rng), F, rng), rng)            # cycle 0 (cold world)
    d0 = sdim(adj, seed=(9000 + s) * 7 + 1)
    if d0 is not None: cyc_ds[0].append(d0); cyc_ksd[0].append(ksd(adj))
    for c in range(1, 5):
        adj = grow_prune(rewire(adj, F, rng), rng)                # burn + settle
        dc = sdim(adj, seed=(9000 + s) * 7 + 1 + c)
        if dc is not None: cyc_ds[c].append(dc); cyc_ksd[c].append(ksd(adj))
for c in range(5):
    m, e, n_ = stats(cyc_ds[c]); km, ke, _ = stats(cyc_ksd[c])
    log(f"  cycle {c}: d_s={m:.3f}±{e:.3f}  k_sd={km:.3f}±{ke:.3f}  (n={n_})")
contrast("PRIMARY cycle4 vs cycle1", cyc_ds[4], cyc_ds[1], "cyc4", "cyc1",
         "AZTEC (worlds improve with cycles)", "HESIOD (worlds degrade with cycles)", "SATURATION")

# ---- E3 NOAH: curated vs random remnant after total flood ----
log("\n## E3 NOAH — the curated remnant")
ark, rnd_ = [], []
for s in range(NARM):
    rng = random.Random(10000 + s)
    adj = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)          # antediluvian world
    orig = [(a, b) for a in range(N) for b in adj[a] if a < b]
    ranked = sorted(orig, key=lambda e: -ov(adj, e[0], e[1]))
    keep = max(1, int(0.15 * len(orig)))
    flood = grow_prune(rewire([set(x) for x in adj], 0.0, rng), rng)  # total scramble (then settle)
    for arm, chosen in (("ARK", ranked[:keep]), ("RANDOM", rng.sample(orig, keep))):
        w = [set(x) for x in flood]
        for a, b in chosen: w[a].add(b); w[b].add(a)              # restore remnant
        w = grow_prune(w, random.Random(10000 + s + (0 if arm == "ARK" else 500000)))
        d = sdim(w, seed=(10000 + s) * 7 + (6 if arm == "ARK" else 8))
        (ark if arm == "ARK" else rnd_).append(d)
contrast("PRIMARY ARK vs RANDOM", ark, rnd_, "ARK", "RANDOM",
         "CURATED-SEED CONFIRMED (ark more geometric)",
         "INVERTED (random remnant beat the ark — report loudly)", "NOT DETECTED")

# ---- E4 GIANTS: establishment level before the burn ----
log("\n## E4 GIANTS — the over-rigid first world")
arms = {}
for f0 in (0.85, 0.95, 1.0):
    vals = []
    for s in range(NARM):
        rng = random.Random(11000 + s + int(f0 * 1000) * 1000)
        adj = grow_prune(rewire(rgg(N, rng), f0, rng), rng)       # establish at f0
        adj = grow_prune(rewire(adj, F, rng), rng)                # drag to F + settle
        vals.append(sdim(adj, seed=(11000 + s) * 7 + int(f0 * 100)))
    arms[f0] = vals
    m, e, n_ = stats(vals); log(f"  f0={f0}: d_s={m:.3f}±{e:.3f} (n={n_})")
contrast("PRIMARY f0=0.85 vs f0=1.0", arms[0.85], arms[1.0], "f0=0.85", "f0=1.0",
         "GIANTS-CONFIRMED (moderate establishment beats maximal)",
         "SEED-MONOTONE (maximal establishment wins)", "FLAT")

log("\n# DONE")
