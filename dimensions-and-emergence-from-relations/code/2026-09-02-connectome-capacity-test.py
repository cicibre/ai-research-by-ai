#!/usr/bin/env python3
# CONNECTOME CAPACITY TEST — harness per the SEALED prereg.
#   experiment-designs/2026-09-02-CONNECTOME-CAPACITY-PREREG.md            (seal 1b319b8)
#   experiment-designs/...-PREREG-ADDENDUM-substrate-choices.md            (seal 47cf7f7)
# Both seals were written BEFORE any connectome file existed on this machine. Building
# this file does not license changing them.
#
# THE CLAIM: cap(v) = BASE + ALPHA * local_clustering(v)  — capacity from local closure.
# As implemented in code/2026-08-19-endogenous-burn-harness.py:29,37 (BASE=12, ALPHA=8),
# a node topples while deg(v) > cap(v). So the law asserts an UPPER BOUND on degree that
# RISES with clustering. This tests that bound in a completely-mapped real network.
#
# ------------------------------------------------------------------------------------
# OPERATIONAL DEFINITIONS — fixed here, before the script is run even once.
# ------------------------------------------------------------------------------------
# SUBSTRATE (addendum): hermaphrodite / _corrected / chemical UNION gap-junction /
#   neurons only. Chemical symmetrised, union with gap junctions, binarised, self-loops
#   dropped. Merge across the two files BY NAME (their index spaces differ: 454 vs 469).
#
# NEURON SET: the chemical file's node_type is authoritative. The gap-junction file
#   demonstrably mislabels 95 bodywall muscles and 21 end organs as "MOTOR NEURONS",
#   so its typing is not used. Neurons =
#       INTERNEURONS (81) + MOTOR NEURONS (108) + SENSORY NEURONS (83)
#     + the 20 pharyngeal NEURONS within node_type PHARYNX (the other 30 PHARYNX nodes
#       are pm* muscles, mc* marginal cells, g* gland, e3* epithelial, bm)
#     + the 8 neurons within SEX-SPECIFIC CELLS (HSNL/R, VC01-06; the other 8 are
#       vm* vulval muscles)
#     = 300.
#   CONSISTENCY CHECK, and it is the reason to trust this filter: 300 + CANL + CANR = 302,
#   the canonical hermaphrodite neuron count. CAN is excluded because the dataset itself
#   files it under OTHER END ORGANS (it is famously non-synaptic); the filter follows the
#   dataset's own labelling rather than overriding it. The script ASSERTS n == 300.
#
# MEASURES: k = degree in the simple undirected graph. c = standard local clustering
#   coefficient, and c := 0.0 for k < 2 — verbatim the harness convention
#   (2026-08-19-endogenous-burn-harness.py:33). Isolated/degree-1 neurons are KEPT and
#   counted in the output, because dropping them would be a choice the seal did not make.
#
# STRATIFICATION (prereg PIN 2, from the 14:18 amendment): rank by degree DESCENDING,
#   ties broken by node name ASCENDING (deterministic). HUB = the first ceil(0.10*n).
#   PERIPHERY = the rest. Sensitivity grid at top 5% / top 20%. HEADLINE IS THE DECILE
#   REGARDLESS OF WHICH LOOKS BEST.
#
# TEST STATISTIC (prereg PIN 1): upper-quantile regression of k on c. HEADLINE tau=0.90;
#   sensitivity tau in {0.80, 0.95}. Estimator: IRLS on the pinball loss. The SAME
#   estimator is used for observed and null so no comparison is estimator-biased. A
#   brute-force exact solution (the QR optimum passes through two data points) is run on
#   the OBSERVED headline fit only, as a check that IRLS converged; both are reported.
#
# ESR — THE TIGHTNESS DIAGNOSTIC (prereg PIN 3): residuals r_i = k_i - (a + b*c_i) from
#   the tau=0.90 fit. ESR = mean(|r| : r > 0) / mean(|r| : r <= 0). Pinned cut:
#   ESR < 0.5 => SHARP (upper edge is a genuine boundary; slope is informative).
#   ESR >= 0.5 => DIFFUSE => the test is INCONCLUSIVE, not refuting and not confirming.
#   Converse pinned with equal force: SHARP + slope <= 0 vs null => THE CLAIM DIES.
#
# NULL (prereg PIN 4): degree-preserving double-edge swap. Preserves the degree sequence
#   EXACTLY (so k, and therefore stratum membership, are identical in every replicate;
#   only c moves). 1000 replicates, 100*|E| swap attempts each, each replicate randomised
#   independently from the observed graph. Reported effect is the observed slope's
#   percentile against that null, NEVER the raw slope. Confirmation requires the observed
#   slope to be positive AND above the 97.5th percentile of the null.
#
# PRE-DECLARED SECONDARY, written before execution: the null also yields an ESR
#   distribution, so ESR is additionally reported as a percentile against the null. The
#   PINNED ABSOLUTE CUT (0.5) REMAINS PRIMARY; the null-calibrated ESR is secondary and
#   may not override it. Declared now so it cannot be reached for later.
import csv, json, math, os, random, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "connectome")
SEED = 20260902
TAU_HEADLINE = 0.90
TAUS = [0.80, 0.90, 0.95]
SPLITS = [("decile_HEADLINE", 0.10), ("top5pct", 0.05), ("top20pct", 0.20)]
N_NULL = 1000
SWAP_MULT = 100

PHARYNGEAL_NEURONS = {
    "I1L", "I1R", "I2L", "I2R", "I3", "I4", "I5", "I6",
    "M1", "M2L", "M2R", "M3L", "M3R", "M4", "M5",
    "MCL", "MCR", "MI", "NSML", "NSMR",
}
SEX_SPECIFIC_NEURONS = {"HSNL", "HSNR", "VC01", "VC02", "VC03", "VC04", "VC05", "VC06"}
WHOLE_TYPES = {"INTERNEURONS", "MOTOR NEURONS", "SENSORY NEURONS"}


def load_csv(path):
    """Netzschleuder CSV headers carry a leading '# ' and per-field spaces."""
    with open(path) as fh:
        return [{k.strip().lstrip("# ").strip(): v for k, v in row.items()}
                for row in csv.DictReader(fh)]


def neuron_names(chem_nodes):
    out = set()
    for x in chem_nodes:
        t, n = x["node_type"], x["name"]
        if t in WHOLE_TYPES:
            out.add(n)
        elif t == "PHARYNX" and n in PHARYNGEAL_NEURONS:
            out.add(n)
        elif t == "SEX-SPECIFIC CELLS" and n in SEX_SPECIFIC_NEURONS:
            out.add(n)
    return out


def build_graph():
    chem_nodes = load_csv(os.path.join(DATA, "hermaphrodite_chemical_corrected", "nodes.csv"))
    gap_nodes = load_csv(os.path.join(DATA, "hermaphrodite_gap_junction_corrected", "nodes.csv"))
    chem_edges = load_csv(os.path.join(DATA, "hermaphrodite_chemical_corrected", "edges.csv"))
    gap_edges = load_csv(os.path.join(DATA, "hermaphrodite_gap_junction_corrected", "edges.csv"))

    keep = neuron_names(chem_nodes)
    assert len(keep) == 300, f"neuron filter returned {len(keep)}, expected 300 (=302 - CANL/CANR)"

    names = sorted(keep)
    idx = {n: i for i, n in enumerate(names)}
    adj = [set() for _ in names]

    def add(name_of, rows, tag):
        used = 0
        for r in rows:
            s, t = name_of[int(r["source"])], name_of[int(r["target"])]
            if s in idx and t in idx and s != t:
                a, b = idx[s], idx[t]
                if b not in adj[a]:
                    used += 1
                adj[a].add(b)
                adj[b].add(a)
        return used

    chem_name = {int(x["index"]): x["name"] for x in chem_nodes}
    gap_name = {int(x["index"]): x["name"] for x in gap_nodes}
    n_chem = add(chem_name, chem_edges, "chem")
    n_gap = add(gap_name, gap_edges, "gap")
    return names, adj, {"new_edges_from_chemical": n_chem, "new_edges_from_gap": n_gap}


def local_c(adj, v):
    """Verbatim the harness convention: c := 0.0 for k < 2."""
    nb = list(adj[v])
    k = len(nb)
    if k < 2:
        return 0.0
    e = sum(1 for i in range(k) for j in range(i + 1, k) if nb[j] in adj[nb[i]])
    return 2.0 * e / (k * (k - 1))


def clustering_all(adj):
    return [local_c(adj, v) for v in range(len(adj))]


def qreg_irls(xs, ys, tau, iters=200, eps=1e-6):
    """Linear quantile regression by iteratively reweighted least squares on the
    pinball loss. Returns (intercept, slope)."""
    n = len(xs)
    a, b = (sum(ys) / n), 0.0
    for _ in range(iters):
        sw = swx = swy = swxx = swxy = 0.0
        for x, y in zip(xs, ys):
            r = y - (a + b * x)
            w = (tau if r > 0 else (1.0 - tau)) / max(abs(r), eps)
            sw += w; swx += w * x; swy += w * y
            swxx += w * x * x; swxy += w * x * y
        den = sw * swxx - swx * swx
        if abs(den) < 1e-18:
            break
        nb_ = (sw * swxy - swx * swy) / den
        na_ = (swy - nb_ * swx) / sw
        if abs(na_ - a) < 1e-10 and abs(nb_ - b) < 1e-10:
            a, b = na_, nb_
            break
        a, b = na_, nb_
    return a, b


def pinball(xs, ys, tau, a, b):
    tot = 0.0
    for x, y in zip(xs, ys):
        r = y - (a + b * x)
        tot += r * (tau - (1.0 if r < 0 else 0.0))
    return tot


def qreg_exact(xs, ys, tau):
    """Brute force: the QR optimum is attained by a line through two data points.
    Used ONLY as a convergence check on the observed headline fit."""
    n = len(xs)
    best = None
    for i in range(n):
        for j in range(i + 1, n):
            if xs[i] == xs[j]:
                continue
            b = (ys[j] - ys[i]) / (xs[j] - xs[i])
            a = ys[i] - b * xs[i]
            L = pinball(xs, ys, tau, a, b)
            if best is None or L < best[0] - 1e-12:
                best = (L, a, b)
    return (best[1], best[2]) if best else (float("nan"), float("nan"))


def esr(xs, ys, a, b):
    above, below = [], []
    for x, y in zip(xs, ys):
        r = y - (a + b * x)
        (above if r > 0 else below).append(abs(r))
    if not above or not below:
        return float("nan")
    ma = sum(above) / len(above)
    mb = sum(below) / len(below)
    return ma / mb if mb > 0 else float("nan")


def edge_list(adj):
    return [(u, v) for u in range(len(adj)) for v in adj[u] if u < v]


def double_edge_swap(adj, rng, n_attempts):
    """Degree-preserving randomisation. Returns a new adjacency; degrees are exact."""
    adj = [set(s) for s in adj]
    edges = edge_list(adj)
    if len(edges) < 2:
        return adj
    for _ in range(n_attempts):
        i = rng.randrange(len(edges)); j = rng.randrange(len(edges))
        if i == j:
            continue
        u, v = edges[i]; x, y = edges[j]
        if rng.random() < 0.5:
            x, y = y, x
        if len({u, v, x, y}) < 4:
            continue
        if y in adj[u] or v in adj[x]:
            continue
        adj[u].discard(v); adj[v].discard(u)
        adj[x].discard(y); adj[y].discard(x)
        adj[u].add(y); adj[y].add(u)
        adj[x].add(v); adj[v].add(x)
        edges[i] = (u, y) if u < y else (y, u)
        edges[j] = (x, v) if x < v else (v, x)
    return adj


def strata(degs, frac):
    """Rank by degree DESCENDING, ties broken by index (names are sorted) ASCENDING.
    HUB = first ceil(frac * n)."""
    n = len(degs)
    order = sorted(range(n), key=lambda v: (-degs[v], v))
    n_hub = math.ceil(frac * n)
    hub = set(order[:n_hub])
    return hub, set(order[n_hub:])


def fit_block(cs, ks, members, tau):
    xs = [cs[v] for v in sorted(members)]
    ys = [float(ks[v]) for v in sorted(members)]
    if len(xs) < 10:
        return None
    a, b = qreg_irls(xs, ys, tau)
    return {"n": len(xs), "intercept": a, "slope": b, "esr": esr(xs, ys, a, b)}


def main():
    rng = random.Random(SEED)
    names, adj, prov = build_graph()
    n = len(names)
    degs = [len(a) for a in adj]
    cs = clustering_all(adj)
    n_edges = sum(degs) // 2

    out = {
        "seal": "experiment-designs/2026-09-02-CONNECTOME-CAPACITY-PREREG.md (1b319b8) + ADDENDUM (47cf7f7)",
        "substrate": "C. elegans hermaphrodite, Cook et al. 2019 _corrected, chemical UNION gap-junction, neurons only",
        "seed": SEED, "n_neurons": n, "n_edges": n_edges, "provenance": prov,
        "n_degree_zero": sum(1 for d in degs if d == 0),
        "n_degree_lt2": sum(1 for d in degs if d < 2),
        "mean_degree": sum(degs) / n, "max_degree": max(degs),
        "mean_clustering": sum(cs) / n,
        "results": {}, "null": {},
    }

    # ---- observed, every split x every tau (headline flagged, not chosen) ----
    for split_name, frac in SPLITS:
        hub, per = strata(degs, frac)
        blk = {}
        for tau in TAUS:
            blk[f"tau_{tau}"] = {
                "periphery": fit_block(cs, degs, per, tau),
                "hub": fit_block(cs, degs, hub, tau),
                "pooled_CONTEXT_ONLY": fit_block(cs, degs, set(range(n)), tau),
            }
        out["results"][split_name] = blk

    # ---- IRLS convergence check on the observed headline fit only ----
    hub, per = strata(degs, 0.10)
    xs = [cs[v] for v in sorted(per)]
    ys = [float(degs[v]) for v in sorted(per)]
    a_i, b_i = qreg_irls(xs, ys, TAU_HEADLINE)
    a_e, b_e = qreg_exact(xs, ys, TAU_HEADLINE)
    out["irls_check_periphery_headline"] = {
        "irls": {"intercept": a_i, "slope": b_i, "loss": pinball(xs, ys, TAU_HEADLINE, a_i, b_i)},
        "exact": {"intercept": a_e, "slope": b_e, "loss": pinball(xs, ys, TAU_HEADLINE, a_e, b_e)},
    }

    # ---- degree-preserving null ----
    print(f"null: {N_NULL} replicates x {SWAP_MULT}*|E| = {SWAP_MULT * n_edges} swap attempts", flush=True)
    null_slopes = {"periphery": [], "hub": [], "pooled_CONTEXT_ONLY": []}
    null_esr = {"periphery": [], "hub": [], "pooled_CONTEXT_ONLY": []}
    for rep in range(N_NULL):
        radj = double_edge_swap(adj, rng, SWAP_MULT * n_edges)
        rcs = clustering_all(radj)
        rdegs = [len(a) for a in radj]
        assert rdegs == degs, "null broke the degree sequence"
        for key, members in (("periphery", per), ("hub", hub),
                             ("pooled_CONTEXT_ONLY", set(range(n)))):
            f = fit_block(rcs, rdegs, members, TAU_HEADLINE)
            null_slopes[key].append(f["slope"])
            null_esr[key].append(f["esr"])
        if (rep + 1) % 50 == 0:
            print(f"  {rep + 1}/{N_NULL}", flush=True)

    def pct(sample, value):
        s = sorted(x for x in sample if x == x)
        if not s:
            return float("nan")
        return 100.0 * sum(1 for x in s if x < value) / len(s)

    def summ(sample):
        s = sorted(x for x in sample if x == x)
        m = sum(s) / len(s)
        sd = math.sqrt(sum((x - m) ** 2 for x in s) / (len(s) - 1)) if len(s) > 1 else 0.0
        return {"mean": m, "sd": sd, "p2.5": s[int(0.025 * len(s))],
                "p97.5": s[min(int(0.975 * len(s)), len(s) - 1)]}

    head = out["results"]["decile_HEADLINE"][f"tau_{TAU_HEADLINE}"]
    for key in null_slopes:
        obs = head[key]
        out["null"][key] = {
            "slope_null": summ(null_slopes[key]),
            "slope_observed": obs["slope"],
            "slope_percentile_vs_null": pct(null_slopes[key], obs["slope"]),
            "slope_z_vs_null": ((obs["slope"] - summ(null_slopes[key])["mean"]) /
                                summ(null_slopes[key])["sd"]) if summ(null_slopes[key])["sd"] else float("nan"),
            "esr_null": summ(null_esr[key]),
            "esr_observed": obs["esr"],
            "esr_percentile_vs_null_SECONDARY": pct(null_esr[key], obs["esr"]),
        }

    path = os.path.join(ROOT, "results", "2026-09-02-connectome-capacity.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)
    print("wrote", path)

    # ---- graded readout, applying the pinned rules verbatim ----
    p = head["periphery"]; h = head["hub"]; nl = out["null"]["periphery"]
    print("\n=== HEADLINE (decile split, tau=0.90) ===")
    print(f"  n={n} neurons, {n_edges} edges, mean k={out['mean_degree']:.2f}, max k={out['max_degree']}")
    print(f"  PERIPHERY n={p['n']}: slope={p['slope']:+.3f}  ESR={p['esr']:.3f}")
    print(f"  HUB       n={h['n']}: slope={h['slope']:+.3f}  ESR={h['esr']:.3f}")
    print(f"  null slope: mean={nl['slope_null']['mean']:+.3f} sd={nl['slope_null']['sd']:.3f} "
          f"p97.5={nl['slope_null']['p97.5']:+.3f}")
    print(f"  observed periphery slope percentile vs null = {nl['slope_percentile_vs_null']:.2f}")
    sharp = p["esr"] < 0.5
    above = nl["slope_percentile_vs_null"] > 97.5
    print(f"\n  ESR<0.5 (sharp)? {sharp}   slope>0? {p['slope'] > 0}   above 97.5th pct of null? {above}")
    if not sharp:
        print("  => INCONCLUSIVE (diffuse edge; no active ceiling). Escalate per the ladder only.")
    elif p["slope"] > 0 and above:
        print("  => CAPACITY LAW SURVIVES in the periphery. Check hub class for her two-population stake.")
    else:
        print("  => THE CLAIM DIES. No further splitting, per clause 4.")


if __name__ == "__main__":
    main()
