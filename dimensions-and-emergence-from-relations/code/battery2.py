#!/usr/bin/env python3
# RUN 2 BATTERY v2 — built against P0-SEAL.md (616e589) + EXTRACTION.md (a01e3f3).
# Committed and self-tested BEFORE any Run-2 world exists. Every item cites its seal section.
# Usage:
#   battery2.py selftest
#   battery2.py run <universe_base> <outdir> <item>
#       items: e1_gate e2_ordering e3_matched e4_erasure e5_severity e6_floor
#              e7a_identity e7b_cycles e7c_living e8_fire e9_timing
#   battery2.py verdict <outdir> <name>
import json, math, os, random, statistics as st, sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, "..", "code")

# physics — verbatim imports (seal §Global/Physics)
ns = {}
exec(open(os.path.join(CODE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune, spectral_dim = ns["rgg"], ns["rewire"], ns["grow_prune"], ns["spectral_dim"]
bh = {"__file__": os.path.join(CODE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
local_c, BASE, ALPHA, cascade = bh["local_c"], bh["BASE"], bh["ALPHA"], bh["cascade"]
# CSN grader — the run-1 committed, self-tested instrument (seal P8.3)
csn = {}
_csrc = open(os.path.join(CODE, "2026-08-19-tail-analysis-CSN.py")).read()
exec(_csrc.split("# ── SELF-TESTS")[0], csn)
csn_grade = csn["grade"]

N = 900
# Rehearsal mode (Gate 5): RN2_QUICK=1 shrinks every loop to smoke-test scale and POISONS
# all outputs with "quick": true. verdict() refuses poisoned files unless tag starts with
# REHEARSAL — structural guard: rehearsal data cannot be graded as real. Never set in real runs.
QUICK = os.environ.get("RN2_QUICK") == "1"
def qn(real, quick): return quick if QUICK else real

# observables (seal §Observables)
def mean_c(adj):
    tot = 0.0; n2 = 0
    for v in range(len(adj)):
        if len(adj[v]) >= 2:
            n2 += 1; tot += local_c(adj, v)
    return tot / n2 if n2 else 0.0

def ksd(adj):
    d = [len(a) for a in adj]; m = sum(d) / len(d)
    return math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1))

def kvar(adj):
    d = [len(a) for a in adj]; m = sum(d) / len(d)
    return sum((x - m) ** 2 for x in d) / len(d)

def pathlen(adj, rng, samples=30):
    n = len(adj); tot = 0; cnt = 0
    for _ in range(samples):
        s = rng.randrange(n); dist = {s: 0}; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in dist: dist[w] = dist[v] + 1; q.append(w)
        tot += sum(dist.values()); cnt += len(dist)
    return tot / cnt

def lcc_frac(adj):
    n = len(adj); seen = [False] * n; best = 0
    for s in range(n):
        if seen[s]: continue
        c = 0; stk = [s]; seen[s] = True
        while stk:
            u = stk.pop(); c += 1
            for v in adj[u]:
                if not seen[v]: seen[v] = True; stk.append(v)
        best = max(best, c)
    return best / n

def edges_of(adj): return frozenset((a, b) for a in range(len(adj)) for b in adj[a] if a < b)
def jac(a, b):
    u = len(a | b); return len(a & b) / u if u else 0.0
def cosv(a, b):
    na = math.sqrt(sum(x * x for x in a)); nb2 = math.sqrt(sum(x * x for x in b))
    return sum(x * y for x, y in zip(a, b)) / (na * nb2) if na * nb2 else 0.0
def sem(x): return st.stdev(x) / math.sqrt(len(x))

# arms (seal §Arms; extraction §arms; d_s probe convention seed*7+{1,2,3} for A,B,A2x)
def arm_A(f, seed):
    rng = random.Random(seed); return grow_prune(rewire(rgg(N, rng), f, rng), rng)
def arm_A2x(f, seed):
    rng = random.Random(seed); a = grow_prune(rewire(rgg(N, rng), f, rng), rng); return grow_prune(a, rng)
def arm_B(f, seed):
    rng = random.Random(seed)
    a = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)
    return grow_prune(rewire(a, f, rng), rng)

# fire-world canonical tick (extraction §fire; dream-seals :20-30)
def fire_tick(adj, rng, K=3, cap_budget=None, budget=None):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = capped_cascade(adj, rng, touched, cap_budget, budget)
    adj2 = grow_prune(adj, rng, passes=1)
    burn += capped_cascade(adj2, rng, range(N), cap_budget, budget)
    return adj2, burn

def capped_cascade(adj, rng, seeds, cap_budget, budget):
    if cap_budget is None:
        return cascade(adj, rng, seeds)
    # capped variant per seal E9 / run-1 reset-null driver: shared per-tick budget
    import collections as _c
    def cap(v): return BASE + ALPHA * local_c(adj, v)
    moved = 0
    q = _c.deque(v for v in seeds if len(adj[v]) > cap(v)); inq = set(q)
    while q:
        if budget[0] >= cap_budget: return moved
        v = q.popleft(); inq.discard(v)
        c = cap(v)
        while len(adj[v]) > c:
            if budget[0] >= cap_budget: return moved
            u = rng.choice(tuple(adj[v]))
            adj[v].discard(u); adj[u].discard(v); moved += 1; budget[0] += 1
            if rng.random() > bh["DELTA"]:
                for _ in range(30):
                    a = rng.randrange(N); b = rng.randrange(N)
                    if a != b and b not in adj[a]:
                        adj[a].add(b); adj[b].add(a)
                        for w in (a, b):
                            if w not in inq and len(adj[w]) > cap(w): q.append(w); inq.add(w)
                        break
            c = cap(v)
    return moved

def load_gauge(adj):
    # seal P8.4 / extraction §oracle: total overhang over near-capacity nodes
    L = 0.0
    for v in range(N):
        d = len(adj[v])
        if d >= BASE:
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

# ---------------- items ----------------
def e1_gate(U, out):  # seal E1
    raw_deg, est_C, est_L = [], [], []
    for i in range(qn(50, 8)):
        rng = random.Random(U + i)
        raw = rgg(N, rng)
        raw_deg.append(sum(len(a) for a in raw) / N)
        est = grow_prune(rewire(raw, 1.0, rng), rng)
        est_C.append(mean_c(est)); est_L.append(lcc_frac(est))
    save(out, "e1_gate", {"raw_deg": st.mean(raw_deg), "est_C": st.mean(est_C), "est_LCC": st.mean(est_L),
                          "sems": [sem(raw_deg), sem(est_C), sem(est_L)]})

def e2_ordering(U, out):  # seal E2 (f=0.5 uses offsets 0-39, f=0.65 uses 40-79)
    res = {}
    for fi, f in enumerate((0.5, 0.65)):
        off = fi * 40
        cells = {}
        for arm, blk, probe in (("A", 1000, 1), ("A2x", 1100, 3), ("B", 1200, 2)):
            builder = {"A": arm_A, "A2x": arm_A2x, "B": arm_B}[arm]
            Cs, Ds = [], []
            for i in range(qn(40, 6)):
                seed = U + blk + off + i
                adj = builder(f, seed)
                Cs.append(mean_c(adj))
                d = spectral_dim(adj, seed=seed * 7 + probe)
                if d is not None: Ds.append(d)
            cells[arm] = {"C": [st.mean(Cs), sem(Cs)], "ds": [st.mean(Ds), sem(Ds), len(Ds)]}
        res[str(f)] = cells
    # P2.4 control: f=0.65 offsets 40-79 with blocks swapped (A<-1200, B<-1000)
    ctrl = {}
    for arm, blk in (("A", 1200), ("B", 1000)):
        builder = {"A": arm_A, "B": arm_B}[arm]
        Cs = [mean_c(builder(0.65, U + blk + 40 + i)) for i in range(qn(40, 6))]
        ctrl[arm] = [st.mean(Cs), sem(Cs)]
    res["control_swap_065"] = ctrl
    save(out, "e2_ordering", res)

def e3_matched(U, out):  # seal E3: A2x (blk 2000, probe +3) vs B (blk 2100, probe +2), d_s
    res = {}
    for fi, f in enumerate((0.5, 0.65)):
        off = fi * 40; cells = {}
        for arm, blk, probe in (("A2x", 2000, 3), ("B", 2100, 2)):
            builder = arm_A2x if arm == "A2x" else arm_B
            Ds = []
            for i in range(qn(40, 6)):
                seed = U + blk + off + i
                d = spectral_dim(builder(f, seed), seed=seed * 7 + probe)
                if d is not None: Ds.append(d)
            cells[arm] = [st.mean(Ds), sem(Ds), len(Ds)]
        res[str(f)] = cells
    save(out, "e3_matched", res)

def e4_erasure(U, out):  # seal E4, design per 2026-08-22-eraser-mde-recheck.py
    diffs = {"C": [], "L": [], "kvar": []}
    for i in range(qn(40, 6)):
        base = rgg(N, random.Random(U + 6000 + i))
        Ua = [set(s) for s in base]; Va = [set(s) for s in base]
        Ua = grow_prune(Ua, random.Random(U + 6100 + i))
        Ua = rewire(Ua, 0.0, random.Random(U + 6200 + i))
        Va = rewire(Va, 0.0, random.Random(U + 6200 + i))
        diffs["C"].append(mean_c(Ua) - mean_c(Va))
        diffs["kvar"].append(kvar(Ua) - kvar(Va))
        diffs["L"].append(pathlen(Ua, random.Random(U + 6300 + i)) - pathlen(Va, random.Random(U + 6400 + i)))
    save(out, "e4_erasure", {k: {"mean": st.mean(v), "sem": sem(v), "z": st.mean(v) / sem(v),
                                 "mde80": 2.8 * sem(v)} for k, v in diffs.items()})

def e5_severity(U, out):  # seal E5: shared-index bootstrap, arms A/A2x/B at 3000/3600/4200
    res = {}
    for si, s_ in enumerate((0.10, 0.20, 0.35, 0.50, 0.65, 0.80)):
        f = 1.0 - s_
        nn = qn(40, 6)
        A  = [mean_c(arm_A(f,  U + 3000 + si * 40 + i)) for i in range(nn)]
        X  = [mean_c(arm_A2x(f, U + 3600 + si * 40 + i)) for i in range(nn)]
        Bv = [mean_c(arm_B(f,  U + 4200 + si * 40 + i)) for i in range(nn)]
        rng = random.Random(9); vals = []
        for _ in range(qn(4000, 400)):
            idx = [rng.randrange(nn) for _ in range(nn)]
            ma = sum(A[k] for k in idx) / nn; mx = sum(X[k] for k in idx) / nn; mb = sum(Bv[k] for k in idx) / nn
            if abs(mx - ma) > 1e-12: vals.append((mb - ma) / (mx - ma))
        vals.sort()
        res[f"{s_:.2f}"] = {"rho_med": vals[len(vals) // 2],
                            "ci": [vals[int(.025 * len(vals))], vals[int(.975 * len(vals))]]}
    save(out, "e5_severity", res)

def e6_floor(U, out):  # seal E6: q in {0,6,42}, n=30, adv = C(B)-C(A)
    f = 0.65; res = {}
    for qi, q in enumerate((0, 6, 42) if not QUICK else (0, 2, 8)):
        advs = []
        for i in range(qn(30, 4)):
            a = arm_A(f, U + 5000 + qi * 100 + i)
            b = arm_B(f, U + 5300 + qi * 100 + i)
            ra = random.Random(U + 5600 + qi * 100 + i); rb = random.Random(U + 5900 + qi * 30 + i)
            for _ in range(q):
                a = grow_prune(a, ra, passes=1); b = grow_prune(b, rb, passes=1)
            advs.append(mean_c(b) - mean_c(a))
        res[str(q)] = {"adv": st.mean(advs), "sem": sem(advs)}
    save(out, "e6_floor", res)

def e7a_identity(U, out):  # seal E7a; channels per extraction §identity (thomas/mary)
    M = qn(40, 8)
    pre_deg, post_deg, pre_e, post_e, pre_sh, post_sh = [], [], [], [], [], []
    for i in range(M):
        seed = U + 7000 + i
        rng = random.Random(seed)
        adj = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)
        pre_deg.append([len(a) for a in adj]); pre_e.append(edges_of(adj))
        d1 = spectral_dim(adj, seed=seed * 7 + 1)
        pre_sh.append([mean_c(adj), d1 if d1 is not None else 0.0, ksd(adj)])
        adj = grow_prune(rewire(adj, 0.65, rng), rng)
        post_deg.append([len(a) for a in adj]); post_e.append(edges_of(adj))
        d2 = spectral_dim(adj, seed=seed * 7 + 2)
        post_sh.append([mean_c(adj), d2 if d2 is not None else 0.0, ksd(adj)])
    def zcols(rows):
        cols = list(zip(*rows)); zs = []
        for c in cols:
            m = st.mean(c); s = st.stdev(c) or 1
            zs.append([(x - m) / s for x in c])
        return list(zip(*zs))
    prz, poz = zcols(pre_sh), zcols(post_sh)
    deg_hits = sum(1 for i in range(M) if max(range(M), key=lambda j: cosv(post_deg[i], pre_deg[j])) == i)
    edge_hits = sum(1 for i in range(M) if max(range(M), key=lambda j: jac(post_e[i], pre_e[j])) == i)
    shape_hits = sum(1 for i in range(M) if min(range(M), key=lambda j: sum((a - b) ** 2 for a, b in zip(poz[i], prz[j]))) == i)
    selfj = [jac(post_e[i], pre_e[i]) for i in range(M)]
    crossj = [jac(post_e[i], pre_e[(i + 1) % M]) for i in range(M)]
    save(out, "e7a_identity", {"deg": deg_hits, "edge": edge_hits, "shape": shape_hits,
                               "selfj": st.mean(selfj), "selfj_sem": sem(selfj), "crossj": st.mean(crossj)})

def e7b_cycles(U, out):  # seal E7b: cold-start f=0.65, 4 cycles, d_s + ksd
    D = [[] for _ in range(5)]; K_ = [[] for _ in range(5)]
    for i in range(qn(30, 4)):
        seed = U + 8000 + i
        rng = random.Random(seed)
        adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
        d0 = spectral_dim(adj, seed=seed * 7 + 1)
        if d0 is not None: D[0].append(d0)
        K_[0].append(ksd(adj))
        for c in range(1, 5):
            adj = grow_prune(rewire(adj, 0.65, rng), rng)
            dc = spectral_dim(adj, seed=seed * 7 + 1 + c)
            if dc is not None: D[c].append(dc)
            K_[c].append(ksd(adj))
    save(out, "e7b_cycles", {"ds": [[st.mean(x), sem(x), len(x)] for x in D],
                             "ksd": [[st.mean(x), sem(x)] for x in K_]})

def e7c_living(U, out):  # seal E7c: M=20, mature 1300, horizons 300/1000/3000
    M = qn(20, 2); HOR = [300, 1000, 3000] if not QUICK else [30, 100, 300]
    pre_deg, pre_e, pre_sh = [], [], []
    post = {h: {"deg": [], "e": [], "sh": []} for h in HOR}
    for i in range(M):
        rng = random.Random(U + 10000 + i)
        adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
        for _ in range(qn(1300, 130)):
            adj, _ = fire_tick(adj, rng)
        pre_deg.append([len(a) for a in adj]); pre_e.append(edges_of(adj))
        pre_sh.append([mean_c(adj), sum(len(a) for a in adj) / N, ksd(adj)])
        lived = 0
        for h in HOR:
            for _ in range(h - lived):
                adj, _ = fire_tick(adj, rng)
            lived = h
            post[h]["deg"].append([len(a) for a in adj]); post[h]["e"].append(edges_of(adj))
            post[h]["sh"].append([mean_c(adj), sum(len(a) for a in adj) / N, ksd(adj)])
    def zc(rows):
        cols = list(zip(*rows)); zs = []
        for c in cols:
            m = st.mean(c); s = st.stdev(c) or 1
            zs.append([(x - m) / s for x in c])
        return list(zip(*zs))
    res = {}
    for h in HOR:
        scar = sum(1 for i in range(M) if max(range(M), key=lambda j: cosv(post[h]["deg"][i], pre_deg[j])) == i)
        name = sum(1 for i in range(M) if max(range(M), key=lambda j: jac(post[h]["e"][i], pre_e[j])) == i)
        prz, poz = zc(pre_sh), zc(post[h]["sh"])
        shp = sum(1 for i in range(M) if min(range(M), key=lambda j: sum((a - b) ** 2 for a, b in zip(poz[i], prz[j]))) == i)
        res[str(h)] = {"scar": scar, "name": name, "shape": shp}
    save(out, "e7c_living", res)

def e8_fire(U, out):  # seal E8: 10 runs, T=3000, delta=0.10, E10+load10 logged
    runs = []
    for i in range(qn(10, 2)):
        rng = random.Random(U + 9000 + i)
        adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
        burns, E10, load10 = [], [], []
        for t in range(qn(3000, 600)):
            adj, b = fire_tick(adj, rng)
            burns.append(b)
            if t % 10 == 0:
                E10.append(sum(len(a) for a in adj) // 2)
                load10.append(load_gauge(adj))
        runs.append({"burns": burns, "E10": E10, "load10": load10})
    json.dump(runs, open(os.path.join(out, "e8_fire_raw.json"), "w"))
    law1 = []
    for r in runs:
        W = 1000; T = len(r["burns"])
        Bw = st.mean(r["burns"][T - W:])
        E10 = r["E10"]; w10 = W // 10
        dEdt = (E10[-1] - E10[len(E10) - w10]) / ((w10 - 1) * 10)
        full = (3 - dEdt) / 0.10
        law1.append({"full_dev": (Bw - full) / full, "short_dev": (Bw - 30.0) / 30.0, "dEdt": dEdt})
    law2 = []
    for r in runs:
        ev = [t for t, b in enumerate(r["burns"]) if b >= 1000]; events = []
        for t in ev:
            if events and t - events[-1][-1] <= 5: events[-1].append(t)
            else: events.append([t])
        for e in events:
            s, t2 = e[0], e[-1]
            i_pre = max(0, s // 10 - 1); i_post = min(len(r["E10"]) - 1, t2 // 10 + 1)
            dE = r["E10"][i_pre] - r["E10"][i_post]
            tot = sum(r["burns"][s:t2 + 1])
            if dE > 0: law2.append(tot * 0.10 / dE)
    tails = []
    for i, r in enumerate(runs):
        g = csn_grade([b for b in r["burns"][500:] if b > 0], f"run{i}", rng=random.Random(1000 + i))
        tails.append(g[0] if isinstance(g, tuple) else g)
    oracles = []
    for r in runs:
        xs, ys = [], []
        for k in range(qn(130, 30), len(r["load10"]) - 2):   # fresh gauge samples only (run-1 fidelity: gauge never stale)
            xs.append(r["load10"][k]); ys.append(sum(r["burns"][10 * k + 1:10 * k + 11]))
        rho = spearman(xs, ys)
        rng2 = random.Random(99); nulls = []
        for _ in range(200):
            sh = xs[:]; rng2.shuffle(sh); nulls.append(spearman(sh, ys))
        nulls.sort()
        oracles.append({"rho": rho, "null95": nulls[189]})
    save(out, "e8_fire", {"law1": law1, "law2": law2, "tails": tails, "oracle": oracles})

def e9_timing(U, out):  # seal E9: delta=0.05, T=10000; capped budget 1500
    old_delta = bh["DELTA"]; bh["DELTA"] = 0.05
    try:
        def one(seed, capb):
            rng = random.Random(seed)
            adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
            burns, E10 = [], []
            budget = [0]
            for t in range(qn(10000, 1500)):
                budget[0] = 0
                adj, b = fire_tick(adj, rng, cap_budget=capb, budget=budget)
                burns.append(b)
                if t % 10 == 0: E10.append(sum(len(a) for a in adj) // 2)
            return {"burns": burns, "E10": E10}
        ctrl = [one(U + 9500 + i, None) for i in range(qn(10, 2))]
        capd = [one(U + 9600 + i, 1500) for i in range(qn(10, 2))]
    finally:
        bh["DELTA"] = old_delta
    json.dump(ctrl + capd, open(os.path.join(out, "e9_timing_raw.json"), "w"))
    def crash_stats(burns, E10, thresh=1000):
        ev = [i for i, b in enumerate(burns) if b >= thresh]; events = []
        for i in ev:
            if events and i - events[-1][-1] <= 5: events[-1].append(i)
            else: events.append([i])
        ev2 = [(e[0], e[-1]) for e in events]
        gaps, drops = [], []
        for k in range(len(ev2) - 1):
            s, e = ev2[k]
            i_pre = max(0, s // 10 - 1); i_post = min(len(E10) - 1, e // 10 + 1)
            drops.append(E10[i_pre] - E10[i_post]); gaps.append(ev2[k + 1][0] - s)
        ct = set()
        for s, e in ev2:
            for t in range(max(0, s - 20), min(len(burns), e + 60)): ct.add(t)
        incr = [E10[k] - E10[k - 1] for k in range(1, len(E10))
                if (k * 10) not in ct and (k * 10 - 10) not in ct]
        return gaps, drops, incr
    def pool(runs):
        G, D, I = [], [], []
        for r in runs:
            g, d, i = crash_stats(r["burns"], r["E10"]); G += g; D += d; I += i
        return G, D, I
    Gc, Dc, Ic = pool(ctrl); Gk, _, _ = pool(capd)
    res = {"n_ctrl": len(Gc), "n_capped": len(Gk)}
    if len(Gc) >= 40 and len(Gk) >= 40:
        cvc = st.stdev(Gc) / st.mean(Gc); cvk = st.stdev(Gk) / st.mean(Gk)
        mu, sd = st.mean(Ic), st.stdev(Ic)
        mx, my = st.mean(Gc), st.mean(Dc)
        cov = sum((g - mx) * (d - my) for g, d in zip(Gc, Dc)) / len(Gc)
        corr = cov / (st.pstdev(Gc) * st.pstdev(Dc))
        rng = random.Random(424242); ratios = []
        for _ in range(2000):
            bg = [Gc[rng.randrange(len(Gc))] for _ in range(len(Gc))]
            bd = [Dc[rng.randrange(len(Dc))] for _ in range(len(Dc))]
            bi = [Ic[rng.randrange(len(Ic))] for _ in range(min(2000, len(Ic)))]
            ci = st.stdev(bi) / (st.mean(bi) * math.sqrt(st.mean(bg) / 10))
            ratios.append((st.stdev(bg) / st.mean(bg)) / math.sqrt(ci ** 2 + (st.stdev(bd) / st.mean(bd)) ** 2))
        ratios.sort()
        res.update({"cv_control": cvc, "cv_capped": cvk, "corr_DT": corr,
                    "ratio_ci": [ratios[50], ratios[1949]]})
    save(out, "e9_timing", res)

def save(out, name, obj):
    os.makedirs(out, exist_ok=True)
    if QUICK: obj = dict(obj, quick=True) if isinstance(obj, dict) else obj
    json.dump(obj, open(os.path.join(out, name + ".json"), "w"), indent=1)

ITEMS = {f.__name__: f for f in (e1_gate, e2_ordering, e3_matched, e4_erasure, e5_severity,
                                 e6_floor, e7a_identity, e7b_cycles, e7c_living, e8_fire, e9_timing)}

# ---------------- verdicts: bars are P0-SEAL.md verbatim ----------------
def load(out, name):
    d = json.load(open(os.path.join(out, name + ".json")))
    if isinstance(d, dict): d.pop("quick", None)   # poison marker checked upstream; stripped for grading
    return d

def verdict(out, tag):
    V = {}
    for f in os.listdir(out):
        if f.endswith(".json") and not f.startswith("VERDICT"):
            try: d = json.load(open(os.path.join(out, f)))
            except Exception: continue
            if isinstance(d, dict) and d.get("quick") and not tag.startswith("REHEARSAL"):
                print(f"REFUSED: {f} is rehearsal (quick) data; verdict tag must start with REHEARSAL"); sys.exit(2)
    g = load(out, "e1_gate")
    V["E1_gate"] = "OPEN" if (8.27 <= g["raw_deg"] <= 8.87 and 0.682 <= g["est_C"] <= 0.742
                              and 0.586 <= g["est_LCC"] <= 0.706) else "FAILED"
    V["E1_values"] = {k: round(g[k], 4) for k in ("raw_deg", "est_C", "est_LCC")}
    o = load(out, "e2_ordering")
    p21 = "PASS"; p22C = True; p22D_hits = 0; rhos = {}
    for f in ("0.5", "0.65"):
        c = o[f]
        s2 = 2 * max(c[a]["C"][1] for a in ("A", "A2x", "B"))
        g1 = c["A2x"]["C"][0] - c["B"]["C"][0]; g2 = c["B"]["C"][0] - c["A"]["C"][0]
        if g1 <= -s2 or g2 <= -s2: p21 = "FAIL"
        elif (g1 < s2 or g2 < s2) and p21 != "FAIL": p21 = "INSUFFICIENT"
        if g2 < s2: p22C = False
        dg = c["A"]["ds"][0] - c["B"]["ds"][0]   # B below A = positive
        ds2 = 2 * math.sqrt(c["A"]["ds"][1] ** 2 + c["B"]["ds"][1] ** 2)
        if dg >= ds2: p22D_hits += 1
        rhos[f] = (c["B"]["C"][0] - c["A"]["C"][0]) / (c["A2x"]["C"][0] - c["A"]["C"][0])
    V["P2.1_ordering"] = p21
    V["P2.2_residue"] = ("PASS" if (p22C and p22D_hits >= 1) else
                         ("PASS-SCOPED" if p22C else "FAIL"))
    V["P2.2_ds_cells_hit"] = p22D_hits
    V["P2.3_rho"] = {f: round(rhos[f], 3) for f in rhos}
    V["P2.3_inband"] = "PASS" if (0.10 <= rhos["0.5"] <= 0.35 and 0.20 <= rhos["0.65"] <= 0.45) else "FAIL"
    main_gap = o["0.65"]["B"]["C"][0] - o["0.65"]["A"]["C"][0]
    ctl_gap = o["control_swap_065"]["B"][0] - o["control_swap_065"]["A"][0]
    V["P2.4_control"] = ("PASS" if (ctl_gap > 0 and ctl_gap <= 2 * main_gap and main_gap <= 2 * ctl_gap)
                         else "FAIL")
    V["P2.4_gaps"] = [round(main_gap, 4), round(ctl_gap, 4)]
    m = load(out, "e3_matched")
    hits = 0; fails = 0
    for f in ("0.5", "0.65"):
        d = m[f]["B"][0] - m[f]["A2x"][0]  # positive = A2x wins (lower ds)
        s2 = 2 * math.sqrt(m[f]["B"][1] ** 2 + m[f]["A2x"][1] ** 2)
        if d >= s2: hits += 1
        elif d <= -s2: fails += 1
    V["E3_matched"] = "FAIL" if fails else ("PASS" if hits == 2 else "INSUFFICIENT")
    e = load(out, "e4_erasure")
    z = e["kvar"]["z"]
    V["E4_kvar"] = "PASS" if z >= 8 else ("INSUFFICIENT" if z >= 4 else "FAIL")
    V["E4_silent"] = "PASS" if (abs(e["C"]["z"]) < 2.8 and abs(e["L"]["z"]) < 2.8) else "FAIL"
    V["E4_mde"] = {k: round(e[k]["mde80"], 5) for k in e}
    V["E4_subthreshold"] = {k: {"mean": round(e[k]["mean"], 5), "z": round(e[k]["z"], 2)} for k in ("C", "L")}
    sv = load(out, "e5_severity")
    ss = sorted((float(k) for k in sv))
    meds = [sv[f"{s:.2f}"]["rho_med"] for s in ss]
    V["P5.1_monotone"] = "PASS" if all(meds[i] >= meds[i + 1] - 0.02 for i in range(5)) else "FAIL"
    pts = [(math.log(1 - s), math.log(r)) for s, r in zip(ss, meds) if r > 0.05]
    if len(pts) >= 4:
        mx = st.mean([p[0] for p in pts]); my = st.mean([p[1] for p in pts])
        slope = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
        V["P5.2_exponent"] = round(slope, 2)
        V["P5.2_inband"] = "PASS" if 1.8 <= slope <= 2.8 else "FAIL"
    else:
        V["P5.2_inband"] = "INSUFFICIENT"
    V["P5.3_boundary"] = "PASS" if sv["0.80"]["ci"][0] <= 0.05 else "FAIL"
    V["P5_rhos"] = {f"{s:.2f}": round(sv[f"{s:.2f}"]["rho_med"], 3) for s in ss}
    fl = load(out, "e6_floor")
    _qs = sorted(int(k) for k in fl)
    a6, a42, s42 = fl[str(_qs[1])]["adv"], fl[str(_qs[2])]["adv"], fl[str(_qs[2])]["sem"]
    p61 = a42 >= 2 * s42
    V["E6_floor"] = ("PASS" if (p61 and a42 >= 0.5 * a6) else
                     ("FAIL" if a42 < 0.5 * a6 - 2 * s42 else "INSUFFICIENT"))
    V["E6_advs"] = {q: round(fl[q]["adv"], 4) for q in fl}
    idn = load(out, "e7a_identity")
    def band(x, hi=38, lo=33): return "PASS" if x >= hi else ("INSUFFICIENT" if x >= lo else "FAIL")
    V["E7a_deg"] = band(idn["deg"]); V["E7a_edge"] = band(idn["edge"])
    V["E7a_shape_blind"] = "PASS" if idn["shape"] <= 8 else "FAIL"
    V["E7a_selfj"] = round(idn["selfj"], 4)
    V["E7a_selfj_inband"] = "PASS" if 0.485 <= idn["selfj"] <= 0.501 else "FAIL"
    V["E7a_cross"] = "PASS" if idn["crossj"] < 0.02 else "FAIL"
    cy = load(out, "e7b_cycles")
    d1, d4 = cy["ds"][1], cy["ds"][4]
    dd = abs(d4[0] - d1[0]); s2 = 2 * math.sqrt(d1[1] ** 2 + d4[1] ** 2)
    V["E7b_ds_flat"] = "PASS" if dd < s2 else "FAIL"
    kv = [x[0] for x in cy["ksd"]]
    k_up = all(kv[i] < kv[i + 1] for i in range(1, 4)) and (kv[4] - kv[1]) >= 2 * math.sqrt(cy["ksd"][1][1] ** 2 + cy["ksd"][4][1] ** 2)
    V["E7b_ksd_climbs"] = "PASS" if k_up else "FAIL"
    lv = load(out, "e7c_living")
    _hs = [str(h) for h in sorted(int(k) for k in lv)]
    V["E7c_300_name"] = "PASS" if lv[_hs[0]]["name"] >= 5 else "FAIL"
    nm = lv[_hs[1]]["name"]
    inv = ("PASS" if (nm >= 10 and lv[_hs[1]]["scar"] <= 3) else
           ("INSUFFICIENT" if 5 <= nm < 10 else "FAIL"))
    V["E7c_1000_inversion"] = inv
    V["E7c_3000_mortality"] = "PASS" if all(lv[_hs[2]][c] <= 3 for c in ("scar", "name", "shape")) else "FAIL"
    V["E7c_counts"] = lv
    fi = load(out, "e8_fire")
    n_ok = sum(1 for x in fi["law1"] if abs(x["full_dev"]) <= 0.05)
    signs = all((x["short_dev"] < 0) == (x["dEdt"] > 0) for x in fi["law1"] if abs(x["short_dev"]) > 0.02)
    V["P8.1_law1"] = "PASS" if (n_ok >= 8 and signs) else "FAIL"
    if len(fi["law2"]) < 15: V["P8.2_law2"] = "INSUFFICIENT"
    else:
        frac = sum(1 for r in fi["law2"] if 0.85 <= r <= 1.10) / len(fi["law2"])
        V["P8.2_law2"] = "PASS" if frac >= 0.80 else "FAIL"
        V["P8.2_frac"] = round(frac, 3)
    pl = sum(1 for t in fi["tails"] if t == "POWER-LAW")
    V["P8.3_tail"] = "PASS" if pl >= 6 else ("INSUFFICIENT" if pl >= 4 else "FAIL")
    V["P8.3_counts"] = {t: fi["tails"].count(t) for t in set(fi["tails"])}
    orc = sum(1 for x in fi["oracle"] if x["rho"] >= 0.2 and x["rho"] > x["null95"])
    V["P8.4_oracle"] = "PASS" if orc >= 8 else ("INSUFFICIENT" if orc >= 6 else "FAIL")
    V["P8.4_rhos"] = [round(x["rho"], 3) for x in fi["oracle"]]
    ti = load(out, "e9_timing")
    if "cv_control" not in ti:
        V["E9"] = f"INSUFFICIENT (gaps {ti['n_ctrl']}/{ti['n_capped']})"
    else:
        V["P9.1_subpoisson"] = "PASS" if ti["cv_control"] <= 0.3 else "FAIL"
        V["P9.2_decoupled"] = "PASS" if ti["corr_DT"] <= 0.5 else "FAIL"
        V["P9.3_compression_AT_RISK"] = ("PASS" if ti["ratio_ci"][1] < 1.0 else
                                         ("FAIL" if ti["ratio_ci"][0] > 1.0 else "INSUFFICIENT"))
        V["P9.4_reset_null"] = "PASS" if ti["cv_capped"] <= 1.2 * ti["cv_control"] else "FAIL"
        V["E9_numbers"] = {k: (round(ti[k], 4) if isinstance(ti[k], float) else ti[k])
                           for k in ("cv_control", "cv_capped", "corr_DT", "ratio_ci")}
    path = os.path.join(out, f"VERDICT-{tag}.json")
    json.dump(V, open(path, "w"), indent=1)
    print(json.dumps(V, indent=1))

# ---------------- self-tests (known answers; must pass before any run) ----------------
def selftest():
    fails = []
    tri = [set([1, 2]), set([0, 2]), set([0, 1])]
    if abs(mean_c(tri) - 1.0) > 1e-9: fails.append("mean_c(K3) != 1")
    ring = [set([(i - 1) % 10, (i + 1) % 10]) for i in range(10)]
    if kvar(ring) != 0 or ksd(ring) != 0: fails.append("kvar/ksd(ring) != 0")
    if lcc_frac(ring) != 1.0: fails.append("lcc(ring) != 1")
    two = [set([1]), set([0]), set([3]), set([2])]
    if lcc_frac(two) != 0.5: fails.append("lcc(two pairs) != 0.5")
    if jac(frozenset([1, 2]), frozenset([1, 2])) != 1.0 or jac(frozenset([1]), frozenset([2])) != 0.0:
        fails.append("jaccard")
    if abs(cosv([1, 0], [1, 0]) - 1) > 1e-9 or abs(cosv([1, 0], [0, 1])) > 1e-9: fails.append("cosine")
    xs = list(range(50)); ys = [2 * x + 1 for x in xs]
    if abs(spearman(xs, ys) - 1.0) > 1e-9: fails.append("spearman(+1)")
    if abs(spearman(xs, ys[::-1]) + 1.0) > 1e-9: fails.append("spearman(-1)")
    r = random.Random(7)
    gaps = [max(2, int(r.gauss(100, 8))) for _ in range(300)]
    cv = st.stdev(gaps) / st.mean(gaps)
    if not (0.05 < cv < 0.12): fails.append("synthetic CV sanity")
    import subprocess
    p = subprocess.run([sys.executable, os.path.join(CODE, "2026-08-19-tail-analysis-CSN.py"), "selftest"],
                       capture_output=True, text=True)
    if p.returncode != 0: fails.append("CSN grader selftest failed")
    d = spectral_dim([set([(i - 1) % 60, (i + 1) % 60]) for i in range(60)], seed=1)
    if d is None or not (0.5 < d < 1.6): fails.append(f"spectral_dim(ring60) = {d}, expected ~1")
    if fails:
        print("SELFTEST FAIL:", fails); sys.exit(1)
    print("SELFTEST PASS (12 checks incl. CSN grader's own suite + spectral_dim ring)")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "selftest": selftest()
    elif cmd == "run":
        U, out, item = int(sys.argv[2]), sys.argv[3], sys.argv[4]
        os.makedirs(out, exist_ok=True)
        ITEMS[item](U, out)
        print(f"{item} U={U} done -> file count: {len([f for f in os.listdir(out) if f.endswith('.json')])}")
    elif cmd == "verdict":
        verdict(sys.argv[2], sys.argv[3])
