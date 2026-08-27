#!/usr/bin/env python3
# ENDOGENOUS-BURN WORLD — harness per the SEALED spec
# experiment-designs/2026-08-17-ENDOGENOUS-BURN-MODEL-SPEC-sealed.md (seal 234c291).
# The spec fixed questions + grading BEFORE this file existed; building it does not
# license changing them. Substrate functions loaded VERBATIM from the committed
# 08-15 harness (single source of truth).
#
# MODEL (drive + threshold + dissipation, sandpile-class):
#   tick: add K random stress-edges (the drive/trickster) -> cascade check ->
#         1 settling pass of grow_prune (the gardener) -> record.
#   capacity(v) = BASE + ALPHA * local_clustering(v)   (structure resists)
#   toppling: while deg(v) > cap(v): shed a random edge of v; with prob
#   (1-DELTA) it re-lands between two random non-adjacent nodes (may push them
#   over -> cascade); with prob DELTA it dissipates (the SOC relief valve that
#   makes gate (a) satisfiable under a constant drive).
#   BURN SIZE = edges shed in one tick's cascade (0 = quiet tick).
#
# CALIBRATION DISCIPLINE (per the seal's tune-guard): the calibration probe
# prints ONLY instrument health — edge-count trend, burn RATE, over-cap count.
# It never prints the size DISTRIBUTION, so the builder cannot tune toward a tail.
import math, random, json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read()
ns = {}
exec(src.rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune, sdim = ns["rgg"], ns["rewire"], ns["grow_prune"], ns["spectral_dim"]

BASE, ALPHA, DELTA = 12, 8, 0.10

def local_c(adj, v):
    nb = list(adj[v]); k = len(nb)
    if k < 2: return 0.0
    e = sum(1 for i in range(k) for j in range(i + 1, k) if nb[j] in adj[nb[i]])
    return 2.0 * e / (k * (k - 1))

def cap(adj, v):
    return BASE + ALPHA * local_c(adj, v)

def ksd(adj):
    d = [len(a) for a in adj]; m = sum(d) / len(d)
    return math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1))

def mean_c(adj):
    tot = 0.0; n2 = 0
    for v in range(len(adj)):
        if len(adj[v]) >= 2:
            n2 += 1; tot += local_c(adj, v)
    return tot / n2 if n2 else 0.0

def cascade(adj, rng, seeds):
    """Relax all over-capacity nodes starting from `seeds`; returns edges shed."""
    N = len(adj); moved = 0
    q = collections.deque(v for v in seeds if len(adj[v]) > cap(adj, v))
    inq = set(q)
    while q:
        v = q.popleft(); inq.discard(v)
        c = cap(adj, v)
        while len(adj[v]) > c:
            u = rng.choice(tuple(adj[v]))
            adj[v].discard(u); adj[u].discard(v)
            moved += 1
            if rng.random() > DELTA:                      # re-land elsewhere
                for _ in range(30):
                    a = rng.randrange(N); b = rng.randrange(N)
                    if a != b and b not in adj[a]:
                        adj[a].add(b); adj[b].add(a)
                        for w in (a, b):
                            if w not in inq and len(adj[w]) > cap(adj, w):
                                q.append(w); inq.add(w)
                        break
            c = cap(adj, v)                                # clustering may have moved
    return moved

def run_world(N, f0, K, T, seed, out_path, label):
    rng = random.Random(seed)
    adj = grow_prune(rewire(rgg(N, rng), f0, rng), rng)
    rec = {"label": label, "N": N, "f0": f0, "K": K, "T": T, "seed": seed,
           "BASE": BASE, "ALPHA": ALPHA, "DELTA": DELTA,
           "burns": [], "edges": [], "ksd": [], "C": []}
    for t in range(T):
        touched = []
        for _ in range(K):                                 # the drive
            for _ in range(30):
                a = rng.randrange(N); b = rng.randrange(N)
                if a != b and b not in adj[a]:
                    adj[a].add(b); adj[b].add(a); touched += [a, b]; break
        burn = cascade(adj, rng, touched)
        adj = grow_prune(adj, rng, passes=1)               # the gardener
        # settling can push nodes over; relax them now so a "burn" is one event
        burn += cascade(adj, rng, range(N))
        rec["burns"].append(burn)
        if t % 10 == 0:
            rec["edges"].append(sum(len(a) for a in adj) // 2)
            rec["ksd"].append(round(ksd(adj), 4))
            rec["C"].append(round(mean_c(adj), 5))
    json.dump(rec, open(out_path, "w"))
    return rec

# ── GATE (d): toppling operator on known answers ────────────────────────────
def gate_d():
    ok = True
    # (d1) lattice-like world, ONE over-capacity node, everyone else headroom:
    # burn must equal the node's excess exactly and stay local (no cascade).
    rng = random.Random(1)
    N = 400
    adj = rgg(N, rng)                                       # spatial, high clustering
    v = max(range(N), key=lambda x: len(adj[x]))
    c = cap(adj, v)
    excess = int(len(adj[v]) - c) if len(adj[v]) > c else 0
    if excess <= 0:                                         # force it over
        need = int(c) + 4 - len(adj[v])
        others = [u for u in range(N) if u != v and u not in adj[v]]
        for u in rng.sample(others, need):
            adj[v].add(u); adj[u].add(v)
    global DELTA
    d0 = DELTA; DELTA = 1.0                                 # pure dissipation: no re-landing
    burn = cascade(adj, rng, [v])
    DELTA = d0
    local_ok = 0 < burn <= 10
    print(f"gate d1 (single node, lattice): burn={burn} (expect small, local) -> {'PASS' if local_ok else 'FAIL'}")
    ok &= local_ok
    # (d2) zero-headroom random world (R6 expander analog): one drive edge must
    # cascade system-spanning (size >> single excess).
    rng = random.Random(2)
    N = 400
    adj = [set() for _ in range(N)]
    target = BASE                                            # ER at exactly base capacity, C~0
    for v in range(N):
        while len(adj[v]) < target:
            u = rng.randrange(N)
            if u != v and u not in adj[v]:
                adj[v].add(u); adj[u].add(v)
    a, b = 0, 1
    if b not in adj[a]: adj[a].add(b); adj[b].add(a)
    burn = cascade(adj, rng, [a, b])
    span_ok = burn > 50
    print(f"gate d2 (zero headroom, expander): burn={burn} (expect system-spanning >50) -> {'PASS' if span_ok else 'FAIL'}")
    ok &= span_ok
    return ok

# ── CALIBRATION PROBE (health only; sizes suppressed per the seal) ──────────
def calibrate():
    rec = run_world(900, 0.65, 3, 200, 777, "/dev/null", "calibration")
    rate = sum(1 for b in rec["burns"] if b > 0) / len(rec["burns"])
    e0, e1 = rec["edges"][0], rec["edges"][-1]
    print(f"calibration: burn-rate={rate:.2f}/tick  edges {e0}->{e1} ({'bounded' if abs(e1-e0)<0.3*e0 else 'DRIFTING'})  [sizes suppressed]")
    return abs(e1 - e0) < 0.3 * e0 and 0.05 < rate

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "gates"
    if mode == "gates":
        okd = gate_d()
        okc = calibrate()
        print(f"GATES: d={'PASS' if okd else 'FAIL'} calibration={'PASS' if okc else 'FAIL'}")
        sys.exit(0 if (okd and okc) else 1)
    # production runs: harness.py run <label> <f0> <K> <T> <seed> <out>
    _, _, label, f0, K, T, seed, out = sys.argv
    rec = run_world(900, float(f0), int(K), int(T), int(seed), out, label)
    rate = sum(1 for b in rec['burns'] if b > 0) / len(rec['burns'])
    print(f"{label}: done. burn-rate={rate:.2f} edges {rec['edges'][0]}->{rec['edges'][-1]}")
