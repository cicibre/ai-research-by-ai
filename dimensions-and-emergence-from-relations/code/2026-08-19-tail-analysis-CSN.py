#!/usr/bin/env python3
# TAIL ANALYSIS (Clauset–Shalizi–Newman discipline) for the endogenous-burn runs.
# Per the sealed spec: POWER-LAW may be declared ONLY if the PL fit is plausible
# AND beats BOTH lognormal and exponential by likelihood ratio. "Straight-ish on
# log-log" is the named enemy and appears nowhere in this file.
#
# SELF-TESTS FIRST (the dead-mutant lesson): synthetic known-answer samples must
# grade correctly before any real data is touched — a tail-grader that cannot
# tell a Pareto from an exponential is the defect, not the data.
#
# Honest simplifications, stated: alpha via the CSN continuous approximation
# with the x-0.5 discrete correction (good for xmin >= ~5); goodness via
# semi-parametric KS bootstrap (150 reps, alpha refit at fixed xmin — full
# xmin re-scan per rep is stated as not done); LR tests Vuong-normalized.
import math, random, json, sys

def fit_alpha(xs, xmin):
    tail = [x for x in xs if x >= xmin]
    n = len(tail)
    if n < 20: return None, n
    s = sum(math.log(x / (xmin - 0.5)) for x in tail)
    return 1.0 + n / s, n

def ks_stat(xs, xmin, alpha):
    tail = sorted(x for x in xs if x >= xmin); n = len(tail)
    def cdf(x):  # continuous approx with discrete shift
        return 1.0 - ((x + 0.5) / (xmin - 0.5)) ** (1.0 - alpha)
    return max(abs((i + 1) / n - cdf(x)) for i, x in enumerate(tail))

def scan_xmin(xs):
    cands = sorted(set(x for x in xs if x >= 2))
    best = None
    for xm in cands:
        if sum(1 for x in xs if x >= xm) < 50: break
        a, n = fit_alpha(xs, xm)
        if a is None or a <= 1.0: continue
        d = ks_stat(xs, xm, a)
        if best is None or d < best[2]: best = (xm, a, d, n)
    return best   # (xmin, alpha, KS, ntail)

def gen_pl(alpha, xmin, n, rng):
    return [int(round(xmin * (1 - rng.random()) ** (-1 / (alpha - 1)))) for _ in range(n)]

def gof_p(xs, xmin, alpha, reps=150, rng=None):
    rng = rng or random.Random(5)
    d_obs = ks_stat(xs, xmin, alpha)
    tail = [x for x in xs if x >= xmin]; n = len(tail)
    worse = 0
    for _ in range(reps):
        synth = gen_pl(alpha, xmin, n, rng)
        a2, _ = fit_alpha(synth, xmin)
        if a2 is None: continue
        if ks_stat(synth, xmin, a2) >= d_obs: worse += 1
    return worse / reps

def loglik_pl(tail, xmin, alpha):
    c = (alpha - 1) / (xmin - 0.5)
    return sum(math.log(c) - alpha * math.log(x / (xmin - 0.5)) for x in tail)

def loglik_exp(tail, xmin):
    m = sum(x - xmin for x in tail) / len(tail)
    lam = 1.0 / max(m, 1e-9)
    return sum(math.log(lam) - lam * (x - xmin) for x in tail), lam

def loglik_ln(tail, xmin):
    ls = [math.log(x) for x in tail]
    mu = sum(ls) / len(ls)
    sg = math.sqrt(sum((l - mu) ** 2 for l in ls) / len(ls)) or 1e-9
    # truncated-at-xmin lognormal: normalize by survival at xmin (erfc)
    def sf(x):
        return 0.5 * math.erfc((math.log(x) - mu) / (sg * math.sqrt(2)))
    Z = max(sf(xmin), 1e-12)
    ll = sum(-math.log(x * sg * math.sqrt(2 * math.pi))
             - (math.log(x) - mu) ** 2 / (2 * sg * sg) - math.log(Z) for x in tail)
    return ll, (mu, sg)

def vuong(ll_pl_pts, ll_alt_pts):
    n = len(ll_pl_pts)
    diffs = [a - b for a, b in zip(ll_pl_pts, ll_alt_pts)]
    R = sum(diffs); m = R / n
    sd = math.sqrt(sum((d - m) ** 2 for d in diffs) / n) or 1e-12
    z = R / (sd * math.sqrt(n))
    p = math.erfc(abs(z) / math.sqrt(2))
    return R, z, p

def grade(xs, label, rng=None):
    res = scan_xmin(xs)
    if res is None:
        print(f"{label}: INSUFFICIENT (no viable xmin)"); return "INSUFFICIENT"
    xmin, alpha, d, ntail = res
    p_gof = gof_p(xs, xmin, alpha, rng=rng)
    tail = [x for x in xs if x >= xmin]
    pl_pts = [math.log((alpha - 1) / (xmin - 0.5)) - alpha * math.log(x / (xmin - 0.5)) for x in tail]
    ll_e, lam = loglik_exp(tail, xmin)
    e_pts = [math.log(lam) - lam * (x - xmin) for x in tail]
    ll_l, (mu, sg) = loglik_ln(tail, xmin)
    def sf(x): return 0.5 * math.erfc((math.log(x) - mu) / (sg * math.sqrt(2)))
    Z = max(sf(xmin), 1e-12)
    l_pts = [-math.log(x * sg * math.sqrt(2 * math.pi)) - (math.log(x) - mu) ** 2 / (2 * sg * sg) - math.log(Z) for x in tail]
    Re, ze, pe = vuong(pl_pts, e_pts)
    Rl, zl, pl_ = vuong(pl_pts, l_pts)
    beats_exp = Re > 0 and pe < 0.1
    beats_ln = Rl > 0 and pl_ < 0.1
    ln_beats_pl = Rl < 0 and pl_ < 0.1
    plausible = p_gof > 0.10
    if plausible and beats_exp and beats_ln: v = "POWER-LAW"
    elif (plausible or ln_beats_pl or (Re > 0)) and not beats_ln:
        # heavy-tailed family but PL not distinguished from (or beaten by) lognormal
        v = "HEAVY-TAILED-NOT-PL" if Re > 0 and pe < 0.1 else ("THIN-TAILED" if Re < 0 and pe < 0.1 else "UNDECIDED-TAIL")
    else:
        v = "THIN-TAILED" if Re < 0 and pe < 0.1 else "UNDECIDED-TAIL"
    print(f"{label}: xmin={xmin} alpha={alpha:.2f} ntail={ntail} KS={d:.3f} gof-p={p_gof:.2f} | vsEXP R={Re:+.1f} p={pe:.3f} | vsLN R={Rl:+.1f} p={pl_:.3f} => {v}")
    return v, alpha, xmin, ntail

# ── SELF-TESTS ───────────────────────────────────────────────────────────────
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] == "selftest"):
    rng = random.Random(42)
    print("── self-tests (known answers; must pass before real data) ──")
    pl = gen_pl(2.5, 5, 3000, rng)
    v1 = grade(pl, "synthetic Pareto(2.5)", rng=random.Random(1))
    exp_s = [int(round(5 + rng.expovariate(0.15))) for _ in range(3000)]
    v2 = grade(exp_s, "synthetic exponential", rng=random.Random(2))
    ln_s = [max(2, int(round(math.exp(rng.gauss(2.0, 1.1))))) for _ in range(3000)]
    v3 = grade(ln_s, "synthetic lognormal", rng=random.Random(3))
    ok = v1[0] == "POWER-LAW" and v2[0] in ("THIN-TAILED",) and v3[0] != "POWER-LAW"
    print(f"SELF-TESTS: {'PASS' if ok else 'FAIL'} (PL->POWER-LAW: {v1[0]=='POWER-LAW'}, exp->THIN: {v2[0]=='THIN-TAILED'}, ln !-> PL: {v3[0]!='POWER-LAW'})")
    sys.exit(0 if ok else 1)

# real data: tail-analysis.py <burnlog.json> [<burnlog2.json> ...]
if __name__ == "__main__":
    for path in sys.argv[1:]:
        rec = json.load(open(path))
        burns = [b for b in rec["burns"] if b > 0]
        # transient exclusion per sealed rule (b): running-mean burn rate window 100
        # into +-10% of tail value (mean of last third)
        rates = rec["burns"]; W = 100
        tail_mean = sum(rates[-len(rates)//3:]) / (len(rates)//3)
        t_star = 0
        for t in range(W, len(rates)):
            rm = sum(rates[t-W:t]) / W
            if tail_mean > 0 and abs(rm - tail_mean) <= 0.10 * tail_mean:
                t_star = t; break
        burns_post = [b for b in rec["burns"][t_star:] if b > 0]
        print(f"\n{rec['label']}: transient t*={t_star}, {len(burns_post)} burns post-transient")
        grade(burns_post, f"  {rec['label']} tail")
