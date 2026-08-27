#!/usr/bin/env python3
# RUN 2 BATTERY — committed BEFORE any Run-2 world exists. Physics imported verbatim from the
# frozen run-1 single-source-of-truth; all analysis fresh, self-tested, bars mechanical.
# Usage:
#   battery.py selftest
#   battery.py run <universe_base> <outdir> <item>     items: ordering matched rho floor erasure identity cycles fire timing
#   battery.py verdict <outdir> <replication_name>
import json, math, os, random, statistics as st, sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, "..", "code")
ns = {}
exec(open(os.path.join(CODE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(CODE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
local_c, BASE, ALPHA = bh["local_c"], bh["BASE"], bh["ALPHA"]

N = 900

# ---------------- observables ----------------
def clustering(adj):
    tot = 0.0; cnt = 0
    for u in range(len(adj)):
        nb = list(adj[u]); d = len(nb)
        if d < 2: continue
        links = sum(1 for a in range(d) for b in range(a + 1, d) if nb[b] in adj[nb[a]])
        tot += 2 * links / (d * (d - 1)); cnt += 1
    return tot / cnt if cnt else 0.0

def kvar(adj):
    ds = [len(a) for a in adj]; m = sum(ds) / len(adj)
    return sum((d - m) ** 2 for d in ds) / len(adj)

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

def edges_of(adj):
    return frozenset((a, b) for a in range(len(adj)) for b in adj[a] if a < b)

def jac(a, b):
    u = len(a | b); return len(a & b) / u if u else 0.0

def sem(x): return st.stdev(x) / math.sqrt(len(x))

# ---------------- arm builders (Kimi-seal identities: I=A, II=A2x, III=B) ----------------
def arm_A(f, seed):
    rng = random.Random(seed); return grow_prune(rewire(rgg(N, rng), f, rng), rng)
def arm_A2x(f, seed):
    rng = random.Random(seed); a = grow_prune(rewire(rgg(N, rng), f, rng), rng); return grow_prune(a, rng)
def arm_B(f, seed):
    rng = random.Random(seed)
    a = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)
    return grow_prune(rewire(a, f, rng), rng)

# ---------------- fire-world (identical physics to run-1 endogenous config) ----------------
def fire_run(seed, K=3, delta=0.10, T=3000, cap_budget=None, log_load=False):
    rng = random.Random(seed)
    def cap(adj, v): return BASE + ALPHA * local_c(adj, v)
    budget = [0]
    def cascade(adj, seeds):
        moved = 0
        q = deque(v for v in seeds if len(adj[v]) > cap(adj, v)); inq = set(q)
        while q:
            if cap_budget and budget[0] >= cap_budget: return moved
            v = q.popleft(); inq.discard(v)
            c = cap(adj, v)
            while len(adj[v]) > c:
                if cap_budget and budget[0] >= cap_budget: return moved
                u = rng.choice(tuple(adj[v]))
                adj[v].discard(u); adj[u].discard(v); moved += 1; budget[0] += 1
                if rng.random() > delta:
                    for _ in range(30):
                        a = rng.randrange(N); b = rng.randrange(N)
                        if a != b and b not in adj[a]:
                            adj[a].add(b); adj[b].add(a)
                            for w in (a, b):
                                if w not in inq and len(adj[w]) > cap(adj, w): q.append(w); inq.add(w)
                            break
                c = cap(adj, v)
        return moved
    adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
    burns, E10, load10 = [], [], []
    for t in range(T):
        budget[0] = 0
        touched = []
        for _ in range(K):
            for _ in range(30):
                a = rng.randrange(N); b = rng.randrange(N)
                if a != b and b not in adj[a]:
                    adj[a].add(b); adj[b].add(a); touched += [a, b]; break
        burn = cascade(adj, touched)
        adj = grow_prune(adj, rng, passes=1)
        burn += cascade(adj, range(N))
        burns.append(burn)
        if t % 10 == 0:
            E10.append(sum(len(a) for a in adj) // 2)
            if log_load:
                load10.append(sum(1 for v in range(N) if len(adj[v]) >= cap(adj, v) - 1) / N)
    return {"burns": burns, "E10": E10, "load10": load10}

# ---------------- CSN tail grader (fresh implementation, self-tested) ----------------
def csn_grade(data, xmin_grid=None):
    data = sorted(x for x in data if x > 0)
    if len(data) < 50: return {"verdict": "INSUFFICIENT", "n": len(data)}
    if xmin_grid is None:
        qs = [data[int(q * len(data))] for q in (0.5, 0.6, 0.7, 0.8, 0.9)]
        xmin_grid = sorted(set(q for q in qs if q >= 2))
    best = None
    for xmin in xmin_grid:
        tail = [x for x in data if x >= xmin]
        if len(tail) < 30: continue
        alpha = 1 + len(tail) / sum(math.log(x / (xmin - 0.5)) for x in tail)
        srt = tail; n = len(srt)
        ks = max(abs((i + 1) / n - (1 - (x / xmin) ** (1 - alpha))) for i, x in enumerate(srt))
        if best is None or ks < best[0]: best = (ks, xmin, alpha, tail)
    if best is None: return {"verdict": "INSUFFICIENT", "n": len(data)}
    ks, xmin, alpha, tail = best
    n = len(tail)
    ll_pl = sum(math.log((alpha - 1) / xmin * (x / xmin) ** (-alpha)) for x in tail)
    lam = 1.0 / (st.mean(tail) - xmin + 1e-9)
    ll_exp = sum(math.log(lam) - lam * (x - xmin) for x in tail)
    logs = [math.log(x) for x in tail]; mu = st.mean(logs); sd = max(st.pstdev(logs), 1e-6)
    ll_ln = sum(-math.log(x * sd * math.sqrt(2 * math.pi)) - (math.log(x) - mu) ** 2 / (2 * sd * sd) for x in tail)
    verdict = "POWER-LAW" if (ll_pl > ll_exp and ll_pl > ll_ln) else "NOT-POWER-LAW"
    return {"verdict": verdict, "alpha": round(alpha, 3), "xmin": xmin, "ntail": n,
            "beats_exp": ll_pl > ll_exp, "beats_ln": ll_pl > ll_ln}

# ---------------- timing analytics (fresh, self-tested) ----------------
def crash_stats(burns, E10, thresh=1000):
    ev = [i for i, b in enumerate(burns) if b >= thresh]; events = []
    for i in ev:
        if events and i - events[-1][-1] <= 5: events[-1].append(i)
        else: events.append([i])
    ev = [(e[0], e[-1]) for e in events]
    gaps, drops = [], []
    for k in range(len(ev) - 1):
        s, e = ev[k]
        i_pre = max(0, s // 10 - 1); i_post = min(len(E10) - 1, e // 10 + 1)
        drops.append(E10[i_pre] - E10[i_post]); gaps.append(ev[k + 1][0] - s)
    crashticks = set()
    for s, e in ev:
        for t in range(max(0, s - 20), min(len(burns), e + 60)): crashticks.add(t)
    incr = [E10[k] - E10[k - 1] for k in range(1, len(E10))
            if (k * 10) not in crashticks and (k * 10 - 10) not in crashticks]
    return gaps, drops, incr

def timing_analysis(runs):
    all_g, all_d, all_i = [], [], []
    for r in runs:
        g, d, i = crash_stats(r["burns"], r["E10"])
        all_g += g; all_d += d; all_i += i
    n = len(all_g)
    if n < 20: return {"verdict_parts": {}, "n": n, "insufficient": True}
    cv_meas = st.stdev(all_g) / st.mean(all_g)
    mu, sd = st.mean(all_i), st.stdev(all_i)
    cv_int = sd / (mu * math.sqrt(st.mean(all_g) / 10))
    cv_D = st.stdev(all_d) / st.mean(all_d)
    base = math.sqrt(cv_int ** 2 + cv_D ** 2)
    mx, my = st.mean(all_g), st.mean(all_d)
    r_gd = sum((g - d0) * (d - my) for g, d in zip(all_g, all_d) for d0 in [mx][:1]) # placeholder replaced below
    cov = sum((g - mx) * (d - my) for g, d in zip(all_g, all_d)) / n
    r_gd = cov / (st.pstdev(all_g) * st.pstdev(all_d))
    rng = random.Random(424242); ratios = []
    for _ in range(2000):
        bg = [all_g[rng.randrange(n)] for _ in range(n)]
        bd = [all_d[rng.randrange(n)] for _ in range(n)]
        bi = [all_i[rng.randrange(len(all_i))] for _ in range(min(2000, len(all_i)))]
        ci = st.stdev(bi) / (st.mean(bi) * math.sqrt(st.mean(bg) / 10))
        ratios.append((st.stdev(bg) / st.mean(bg)) / math.sqrt(ci ** 2 + (st.stdev(bd) / st.mean(bd)) ** 2))
    ratios.sort()
    return {"n": n, "cv_meas": round(cv_meas, 4), "cv_int": round(cv_int, 4), "cv_D": round(cv_D, 4),
            "baseline": round(base, 4), "corr_DT": round(r_gd, 3),
            "ratio_ci": [round(ratios[50], 3), round(ratios[1949], 3)], "insufficient": False}

# ---------------- items ----------------
def item_ordering(base, out):
    res = {}
    for f in (0.5, 0.65):
        A  = [clustering(arm_A(f, base + 1000 + i)) for i in range(30)]
        A2 = [clustering(arm_A2x(f, base + 1100 + i)) for i in range(30)]
        B  = [clustering(arm_B(f, base + 1200 + i)) for i in range(30)]
        res[str(f)] = {"A": [st.mean(A), sem(A)], "A2x": [st.mean(A2), sem(A2)], "B": [st.mean(B), sem(B)],
                       "rho": (st.mean(B) - st.mean(A)) / (st.mean(A2) - st.mean(A))}
    json.dump(res, open(os.path.join(out, "ordering.json"), "w"))

def item_matched(base, out):
    # direct-at-final with matched TOTAL settle budget (2x) vs establish-then-degrade
    res = {}
    for f in (0.5, 0.65):
        direct = [clustering(arm_A2x(f, base + 2000 + i)) for i in range(30)]   # build at f, settle x2
        estdeg = [clustering(arm_B(f, base + 2100 + i)) for i in range(30)]     # build 1.0, settle, burn to f, settle
        res[str(f)] = {"direct": [st.mean(direct), sem(direct)], "estdeg": [st.mean(estdeg), sem(estdeg)]}
    json.dump(res, open(os.path.join(out, "matched.json"), "w"))

def item_rho(base, out):
    res = {}
    for si, s in enumerate((0.9, 0.8, 0.65, 0.5, 0.35, 0.2)):
        A  = [clustering(arm_A(s, base + 3000 + si * 100 + i)) for i in range(30)]
        A2 = [clustering(arm_A2x(s, base + 3600 + si * 100 + i)) for i in range(30)]
        B  = [clustering(arm_B(s, base + 4200 + si * 100 + i)) for i in range(30)]
        res[str(s)] = {"rho": (st.mean(B) - st.mean(A)) / (st.mean(A2) - st.mean(A)),
                       "A": st.mean(A), "A2x": st.mean(A2), "B": st.mean(B), "semA": sem(A)}
    json.dump(res, open(os.path.join(out, "rho.json"), "w"))

def item_floor(base, out):
    f = 0.65; res = {}
    for q in (0, 6, 42):
        advs = []
        for i in range(30):
            sa = base + 5000 + q * 50 + i
            rngA = random.Random(sa); a = grow_prune(rewire(rgg(N, rngA), f, rngA), rngA)
            rngB = random.Random(sa + 25); b0 = grow_prune(rewire(rgg(N, rngB), 1.0, rngB), rngB)
            b = grow_prune(rewire(b0, f, rngB), rngB)
            for _ in range(q):
                a = grow_prune(a, rngA, passes=1); b = grow_prune(b, rngB, passes=1)
            advs.append(clustering(b) - clustering(a))
        res[str(q)] = {"adv": st.mean(advs), "sem": sem(advs)}
    json.dump(res, open(os.path.join(out, "floor.json"), "w"))

def item_erasure(base, out):
    diffs = {"C": [], "L": [], "kvar": []}
    for i in range(40):
        rng = random.Random(base + 6000 + i)
        b0 = rgg(N, rng)
        U = [set(s) for s in b0]; V = [set(s) for s in b0]
        U = grow_prune(U, random.Random(base + 6100 + i))
        U = rewire(U, 0.0, random.Random(base + 6200 + i))
        V = rewire(V, 0.0, random.Random(base + 6200 + i))
        diffs["C"].append(clustering(U) - clustering(V))
        diffs["kvar"].append(kvar(U) - kvar(V))
        diffs["L"].append(pathlen(U, random.Random(base + 6300 + i)) - pathlen(V, random.Random(base + 6400 + i)))
    res = {k: {"mean": st.mean(v), "sem": sem(v), "z": st.mean(v) / sem(v), "mde80": 2.8 * sem(v)} for k, v in diffs.items()}
    json.dump(res, open(os.path.join(out, "erasure.json"), "w"))

def item_identity(base, out):
    M = 40; f = 0.65
    pre_e, post_e, pre_deg, post_deg, pre_shape, post_shape = [], [], [], [], [], []
    for i in range(M):
        rng = random.Random(base + 7000 + i)
        adj = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)
        pre_e.append(edges_of(adj)); pre_deg.append(tuple(len(a) for a in adj))
        pre_shape.append((clustering(adj), kvar(adj), pathlen(adj, random.Random(base + 7100 + i))))
        adj = grow_prune(rewire(adj, f, rng), rng)
        post_e.append(edges_of(adj)); post_deg.append(tuple(len(a) for a in adj))
        post_shape.append((clustering(adj), kvar(adj), pathlen(adj, random.Random(base + 7200 + i))))
    def deg_dist(a, b): return sum((x - y) ** 2 for x, y in zip(sorted(a), sorted(b)))
    deg_hits = sum(1 for i in range(M) if min(range(M), key=lambda j: deg_dist(post_deg[i], pre_deg[j])) == i)
    edge_hits = sum(1 for i in range(M) if max(range(M), key=lambda j: jac(post_e[i], pre_e[j])) == i)
    dims = list(zip(*pre_shape)); mus = [st.mean(d) for d in dims]; sds = [max(st.pstdev(d), 1e-9) for d in dims]
    def shape_dist(a, b): return sum(((x - y) / s) ** 2 for x, y, s in zip(a, b, sds))
    shape_hits = sum(1 for i in range(M) if min(range(M), key=lambda j: shape_dist(post_shape[i], pre_shape[j])) == i)
    selfj = [jac(post_e[i], pre_e[i]) for i in range(M)]
    crossj = [jac(post_e[i], pre_e[(i + 1) % M]) for i in range(M)]
    json.dump({"deg": deg_hits, "edge": edge_hits, "shape": shape_hits,
               "selfj_mean": st.mean(selfj), "selfj_sem": sem(selfj), "crossj_mean": st.mean(crossj)},
              open(os.path.join(out, "identity.json"), "w"))

def item_cycles(base, out):
    Cs = [[] for _ in range(5)]; Ks = [[] for _ in range(5)]
    for i in range(30):
        rng = random.Random(base + 8000 + i)
        adj = grow_prune(rewire(rgg(N, rng), 1.0, rng), rng)
        Cs[0].append(clustering(adj)); Ks[0].append(kvar(adj))
        for c in range(1, 5):
            adj = grow_prune(rewire(adj, 0.65, rng), rng)
            Cs[c].append(clustering(adj)); Ks[c].append(kvar(adj))
    json.dump({"C": [[st.mean(x), sem(x)] for x in Cs], "kvar": [[st.mean(x), sem(x)] for x in Ks]},
              open(os.path.join(out, "cycles.json"), "w"))

def item_fire(base, out):
    runs = []
    for i in range(10):
        r = fire_run(base + 9000 + i, log_load=True)
        runs.append(r)
    law1 = []
    for r in runs:
        W = 1000; T = len(r["burns"])
        Bw = st.mean(r["burns"][T - W:])
        E10 = r["E10"]; w10 = W // 10
        dEdt = (E10[-1] - E10[len(E10) - w10]) / ((w10 - 1) * 10)
        full = (3 - dEdt) / 0.10
        short_dev = (Bw - 30.0) / 30.0
        law1.append({"full_dev": (Bw - full) / full, "short_dev": short_dev, "dEdt": dEdt})
    tails = [csn_grade([b for b in r["burns"][500:] if b > 0]) for r in runs]
    oracles = []
    for r in runs:
        load = r["load10"]; burns = r["burns"]
        xs, ys = [], []
        for k in range(50, len(load) - 1):
            xs.append(load[k]); ys.append(sum(burns[k * 10:k * 10 + 10]))
        mx, my = st.mean(xs), st.mean(ys)
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(xs)
        sx, sy = st.pstdev(xs), st.pstdev(ys)
        oracles.append(cov / (sx * sy) if sx > 0 and sy > 0 else 0.0)
    json.dump({"law1": law1, "tails": tails, "oracle": oracles},
              open(os.path.join(out, "fire.json"), "w"))
    json.dump([{"burns": r["burns"], "E10": r["E10"]} for r in runs], open(os.path.join(out, "fire_raw.json"), "w"))

def item_timing(base, out):
    ctrl = [fire_run(base + 9500 + i, delta=0.05, T=10000) for i in range(10)]
    capd = [fire_run(base + 9600 + i, delta=0.05, T=10000, cap_budget=1500) for i in range(10)]
    ta = timing_analysis(ctrl)
    def pooled_cv(runs):
        g = []
        for r in runs:
            gg, _, _ = crash_stats(r["burns"], r["E10"]); g += gg
        return (st.stdev(g) / st.mean(g), len(g)) if len(g) >= 20 else (None, len(g))
    cvc, nc = pooled_cv(ctrl); cvk, nk = pooled_cv(capd)
    json.dump({"control": ta, "cv_control": cvc, "cv_capped": cvk, "n_ctrl": nc, "n_capped": nk},
              open(os.path.join(out, "timing.json"), "w"))
    json.dump([{"burns": r["burns"], "E10": r["E10"]} for r in ctrl + capd], open(os.path.join(out, "timing_raw.json"), "w"))

ITEMS = {"ordering": item_ordering, "matched": item_matched, "rho": item_rho, "floor": item_floor,
         "erasure": item_erasure, "identity": item_identity, "cycles": item_cycles,
         "fire": item_fire, "timing": item_timing}

# ---------------- sealed bars (mirrored in the P0 seal document) ----------------
def verdict(out, name):
    V = {}
    o = json.load(open(os.path.join(out, "ordering.json")))
    ok = True; ins = False
    for f in ("0.5", "0.65"):
        c = o[f]
        g1 = c["A2x"][0] - c["B"][0]; g2 = c["B"][0] - c["A"][0]
        s = 2 * max(c["A"][1], c["A2x"][1], c["B"][1])
        if g1 < 0 or g2 < 0: ok = False
        elif g1 < s or g2 < s: ins = True
    V["ordering"] = "FAIL" if not ok else ("INSUFFICIENT" if ins else "PASS")
    V["rho_cells"] = {f: round(o[f]["rho"], 3) for f in o}
    m = json.load(open(os.path.join(out, "matched.json")))
    ok = all(m[f]["direct"][0] - m[f]["estdeg"][0] >= 2 * max(m[f]["direct"][1], m[f]["estdeg"][1]) for f in m)
    V["matched_direct_wins"] = "PASS" if ok else "FAIL"
    r = json.load(open(os.path.join(out, "rho.json")))
    ss = sorted((float(k) for k in r), reverse=True)
    rhos = [r[str(s)]["rho"] for s in ss]
    mono = all(rhos[i] >= rhos[i + 1] - 0.05 for i in range(len(rhos) - 1))
    pts = [(math.log(s), math.log(rh)) for s, rh in zip(ss, rhos) if rh > 0.02]
    if len(pts) >= 4:
        mx = st.mean([p[0] for p in pts]); my = st.mean([p[1] for p in pts])
        slope = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, y in pts)
    else: slope = float("nan")
    V["rho_monotone"] = "PASS" if mono else "FAIL"
    V["rho_exponent"] = round(slope, 2)
    V["rho_exponent_inband"] = "PASS" if 1.8 <= slope <= 3.2 else ("INSUFFICIENT" if math.isnan(slope) else "FAIL")
    fl = json.load(open(os.path.join(out, "floor.json")))
    a6, a42 = fl["6"]["adv"], fl["42"]["adv"]; s42 = fl["42"]["sem"]
    V["floor"] = "PASS" if (a42 >= 0.5 * a6 and a42 >= 2 * s42) else ("FAIL" if a42 < 0.5 * a6 - 2 * s42 else "INSUFFICIENT")
    e = json.load(open(os.path.join(out, "erasure.json")))
    V["erasure_kvar_survives"] = "PASS" if e["kvar"]["z"] >= 8 else "FAIL"
    V["erasure_nonconserved_silent"] = "PASS" if abs(e["C"]["z"]) < 2.8 and abs(e["L"]["z"]) < 2.8 else "FAIL"
    V["erasure_mde"] = {k: round(e[k]["mde80"], 5) for k in e}
    idn = json.load(open(os.path.join(out, "identity.json")))
    V["identity_deg"] = "PASS" if idn["deg"] >= 38 else ("INSUFFICIENT" if idn["deg"] >= 33 else "FAIL")
    V["identity_edge"] = "PASS" if idn["edge"] >= 38 else ("INSUFFICIENT" if idn["edge"] >= 33 else "FAIL")
    V["identity_shape_blind"] = "PASS" if idn["shape"] <= 8 else "FAIL"
    V["selfj"] = round(idn["selfj_mean"], 4)
    V["selfj_inband"] = "PASS" if 0.485 <= idn["selfj_mean"] <= 0.501 else "FAIL"
    cy = json.load(open(os.path.join(out, "cycles.json")))
    kv = [x[0] for x in cy["kvar"]]
    V["cycles_kvar_monotone"] = "PASS" if all(kv[i] < kv[i + 1] for i in range(4)) else "FAIL"
    cs = cy["C"]
    flat = all(abs(cs[c][0] - cs[1][0]) < 2 * (cs[c][1] + cs[1][1]) for c in (2, 3, 4))
    V["cycles_functional_flat"] = "PASS" if flat else "FAIL"
    fi = json.load(open(os.path.join(out, "fire.json")))
    fulldevs = [abs(x["full_dev"]) for x in fi["law1"]]
    V["law1_full"] = "PASS" if sum(1 for d in fulldevs if d <= 0.05) >= 8 else "FAIL"
    signs_ok = all((x["short_dev"] < 0) == (x["dEdt"] > 0) for x in fi["law1"] if abs(x["short_dev"]) > 0.02)
    V["law1_sign_count"] = "PASS" if signs_ok else "FAIL"
    pl = sum(1 for t in fi["tails"] if t.get("verdict") == "POWER-LAW")
    V["tail_powerlaw_midbody"] = "PASS" if pl >= 6 else ("INSUFFICIENT" if pl >= 4 else "FAIL")
    V["oracle"] = "PASS" if sum(1 for c in fi["oracle"] if c >= 0.8) >= 8 else ("INSUFFICIENT" if sum(1 for c in fi["oracle"] if c >= 0.6) >= 8 else "FAIL")
    ti = json.load(open(os.path.join(out, "timing.json")))
    ta = ti["control"]
    if ta.get("insufficient") or ti["cv_control"] is None or ti["cv_capped"] is None:
        V["timing"] = "INSUFFICIENT"
    else:
        V["timing_subpoisson"] = "PASS" if ta["cv_meas"] <= 0.3 else "FAIL"
        V["timing_decoupled"] = "PASS" if ta["corr_DT"] <= 0.5 else "FAIL"
        V["timing_compression"] = "PASS" if ta["ratio_ci"][1] < 1.0 else ("FAIL" if ta["ratio_ci"][0] > 1.0 else "INSUFFICIENT")
        V["reset_null_clock_survives"] = "PASS" if ti["cv_capped"] <= 1.2 * ti["cv_control"] else "FAIL"
        V["timing_numbers"] = {"cv": ta["cv_meas"], "baseline": ta["baseline"], "corr_DT": ta["corr_DT"],
                               "ratio_ci": ta["ratio_ci"], "cv_capped": ti["cv_capped"], "cv_control": ti["cv_control"]}
    json.dump(V, open(os.path.join(out, f"VERDICT-{name}.json"), "w"), indent=1)
    print(json.dumps(V, indent=1))

# ---------------- self-tests (must pass before any run) ----------------
def selftest():
    fails = []
    tri = [set([1, 2]), set([0, 2]), set([0, 1])]
    if abs(clustering(tri) - 1.0) > 1e-9: fails.append("clustering(K3) != 1")
    ring = [set([(i - 1) % 10, (i + 1) % 10]) for i in range(10)]
    if kvar(ring) != 0: fails.append("kvar(ring) != 0")
    if jac(frozenset([1, 2]), frozenset([1, 2])) != 1.0: fails.append("jac identity")
    if jac(frozenset([1]), frozenset([2])) != 0.0: fails.append("jac disjoint")
    rng = random.Random(1)
    pl_sample = [int(2 * (1 - rng.random()) ** (-1 / 1.5)) for _ in range(5000)]
    g = csn_grade(pl_sample)
    if g["verdict"] != "POWER-LAW": fails.append(f"CSN miss on power-law sample: {g}")
    exp_sample = [int(1 + rng.expovariate(0.2)) for _ in range(5000)]
    g2 = csn_grade(exp_sample)
    if g2["verdict"] == "POWER-LAW": fails.append(f"CSN false-positive on exponential: {g2}")
    rng = random.Random(2)
    gaps = [max(2, int(rng.gauss(100, 30))) for _ in range(200)]
    synth = {"burns": [], "E10": []}
    t = 0; E = 5000; e10 = []
    burns = []
    for g0 in gaps:
        for k in range(g0 - 1):
            burns.append(0); E += 3
            if len(burns) % 10 == 0: e10.append(E)
        burns.append(2000); E -= 300
        if len(burns) % 10 == 0: e10.append(E)
    gg, dd, ii = crash_stats(burns, e10)
    if not (len(gg) > 100): fails.append("crash_stats event detection")
    ta = timing_analysis([{"burns": burns, "E10": e10}])
    if ta["insufficient"]: fails.append("timing_analysis insufficient on synthetic")
    if fails:
        print("SELFTEST FAIL:", fails); sys.exit(1)
    print("SELFTEST PASS (7 checks)")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "selftest": selftest()
    elif cmd == "run":
        base, out, item = int(sys.argv[2]), sys.argv[3], sys.argv[4]
        os.makedirs(out, exist_ok=True)
        ITEMS[item](base, out)
        print(f"{item} done -> {out}")
    elif cmd == "verdict": verdict(sys.argv[2], sys.argv[3])
