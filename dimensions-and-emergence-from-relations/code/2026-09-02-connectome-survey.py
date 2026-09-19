#!/usr/bin/env python3
# CONNECTOME SURVEY — per the SEALED prereg
#   experiment-designs/2026-09-02-CONNECTOME-SURVEY-PREREG.md   (seal 37223f6)
# Question: is the C. elegans failure UNIVERSAL, or is that network special?
# The capacity law stays REFUTED regardless of what this finds. A positive is a
# new question, not a resurrection. Both branches pinned in the seal.
#
# Statistics are imported VERBATIM from the refuted run's harness (single source of
# truth) so the survey cannot differ from it by drift:
#   code/2026-09-02-connectome-capacity-test.py  (seal 0b6586d)
import importlib.util, json, math, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "connectome")

_spec = importlib.util.spec_from_file_location(
    "capacity_test", os.path.join(HERE, "2026-09-02-connectome-capacity-test.py"))
CT = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CT)

SEED = 20260902
TAU = 0.90
TAUS = [0.80, 0.90, 0.95]
SPLITS = [("decile_HEADLINE", 0.10), ("top5pct", 0.05), ("top20pct", 0.20)]
N_NULL = 1000

# published values from the refuted run, results/2026-09-02-connectome-capacity.json
CE_100_MEAN, CE_100_SD = -56.897518, 30.550196
GATE_MEAN_TOL = 0.25   # |mean10 - mean100| <= 0.25 * sd100
GATE_SD_TOL = 0.20     # |sd10/sd100 - 1| <= 0.20


def analyse(name, names, adj, swap_mult, note=""):
    """Identical statistics to the refuted run, applied to any graph."""
    n = len(names)
    degs = [len(a) for a in adj]
    cs = CT.clustering_all(adj)
    n_edges = sum(degs) // 2
    out = {
        "network": name, "note": note, "n_nodes": n, "n_edges": n_edges,
        "swap_multiplier": swap_mult, "n_null": N_NULL,
        "mean_degree": sum(degs) / n, "max_degree": max(degs),
        "mean_clustering": sum(cs) / n,
        "n_degree_zero": sum(1 for d in degs if d == 0),
        "n_degree_lt2": sum(1 for d in degs if d < 2),
        "results": {},
    }
    for split_name, frac in SPLITS:
        hub, per = CT.strata(degs, frac)
        blk = {}
        for tau in TAUS:
            blk[f"tau_{tau}"] = {
                "periphery": CT.fit_block(cs, degs, per, tau),
                "hub": CT.fit_block(cs, degs, hub, tau),
                "pooled_CONTEXT_ONLY": CT.fit_block(cs, degs, set(range(n)), tau),
            }
        out["results"][split_name] = blk

    hub, per = CT.strata(degs, 0.10)
    rng = random.Random(SEED)
    null = {"periphery": [], "hub": [], "pooled_CONTEXT_ONLY": []}
    null_esr = {"periphery": [], "hub": [], "pooled_CONTEXT_ONLY": []}
    print(f"[{name}] null: {N_NULL} x {swap_mult}*|E| = {swap_mult * n_edges} swaps", flush=True)
    for rep in range(N_NULL):
        radj = CT.double_edge_swap(adj, rng, swap_mult * n_edges)
        rcs = CT.clustering_all(radj)
        rdegs = [len(a) for a in radj]
        assert rdegs == degs, "null broke the degree sequence"
        for key, mem in (("periphery", per), ("hub", hub),
                         ("pooled_CONTEXT_ONLY", set(range(n)))):
            f = CT.fit_block(rcs, rdegs, mem, TAU)
            null[key].append(f["slope"])
            null_esr[key].append(f["esr"])
        if (rep + 1) % 100 == 0:
            print(f"  [{name}] {rep + 1}/{N_NULL}", flush=True)

    def summ(s):
        s = sorted(x for x in s if x == x)
        m = sum(s) / len(s)
        sd = math.sqrt(sum((x - m) ** 2 for x in s) / (len(s) - 1)) if len(s) > 1 else 0.0
        return {"mean": m, "sd": sd, "p2.5": s[int(0.025 * len(s))],
                "p97.5": s[min(int(0.975 * len(s)), len(s) - 1)]}

    def pct(s, v):
        s = sorted(x for x in s if x == x)
        return 100.0 * sum(1 for x in s if x < v) / len(s)

    head = out["results"]["decile_HEADLINE"][f"tau_{TAU}"]
    out["null"] = {}
    for key in null:
        ns = summ(null[key])
        obs = head[key]
        out["null"][key] = {
            "slope_null": ns, "slope_observed": obs["slope"],
            "slope_percentile_vs_null": pct(null[key], obs["slope"]),
            "slope_z_vs_null": (obs["slope"] - ns["mean"]) / ns["sd"] if ns["sd"] else float("nan"),
            "esr_null": summ(null_esr[key]), "esr_observed": obs["esr"],
            "esr_percentile_vs_null_SECONDARY": pct(null_esr[key], obs["esr"]),
        }

    p = head["periphery"]
    nl = out["null"]["periphery"]
    sharp = p["esr"] < 0.5
    above = nl["slope_percentile_vs_null"] > 97.5
    out["readout"] = {
        "periphery_slope": p["slope"], "periphery_esr": p["esr"], "sharp": sharp,
        "slope_positive": p["slope"] > 0, "above_97.5_null": above,
        "verdict": ("INCONCLUSIVE_diffuse_edge" if not sharp
                    else "SURVIVES" if (p["slope"] > 0 and above)
                    else "REFUTED_in_this_network"),
    }
    return out


def load_fly_larva():
    nodes = CT.load_csv(os.path.join(DATA, "fly_larva", "nodes.csv"))
    edges = CT.load_csv(os.path.join(DATA, "fly_larva", "edges.csv"))
    n = len(nodes)
    names = [x["index"] for x in nodes]
    adj = [set() for _ in range(n)]
    for r in edges:  # etype and count discarded by binarisation, per the seal
        s, t = int(r["source"]), int(r["target"])
        if s != t:
            adj[s].add(t); adj[t].add(s)
    return names, adj


def load_male_shared():
    """Discretion-free rule: intersect with the hermaphrodite's verified 300."""
    herm_nodes = CT.load_csv(os.path.join(
        DATA, "hermaphrodite_chemical_corrected", "nodes.csv"))
    keep_names = CT.neuron_names(herm_nodes)
    assert len(keep_names) == 300, f"hermaphrodite neuron set = {len(keep_names)}, expected 300"

    mc_nodes = CT.load_csv(os.path.join(DATA, "male_chemical_corrected", "nodes.csv"))
    mg_nodes = CT.load_csv(os.path.join(DATA, "male_gap_junction_corrected", "nodes.csv"))
    mc_edges = CT.load_csv(os.path.join(DATA, "male_chemical_corrected", "edges.csv"))
    mg_edges = CT.load_csv(os.path.join(DATA, "male_gap_junction_corrected", "edges.csv"))

    present = {x["name"] for x in mc_nodes} | {x["name"] for x in mg_nodes}
    names = sorted(keep_names & present)
    idx = {nm: i for i, nm in enumerate(names)}
    adj = [set() for _ in names]
    for nodes, edges in ((mc_nodes, mc_edges), (mg_nodes, mg_edges)):
        nm = {int(x["index"]): x["name"] for x in nodes}
        for r in edges:
            s, t = nm[int(r["source"])], nm[int(r["target"])]
            if s in idx and t in idx and s != t:
                adj[idx[s]].add(idx[t]); adj[idx[t]].add(idx[s])
    return names, adj, len(keep_names - present)


def main():
    survey = {"seal": "experiment-designs/2026-09-02-CONNECTOME-SURVEY-PREREG.md (37223f6)",
              "question": "Is the C. elegans failure universal, or is that network special?",
              "standing": "The capacity law remains REFUTED regardless of this survey. "
                          "A positive is a new question requiring its own stake, not a resurrection.",
              "networks": {}}

    # ---------- SWAP-DEPTH GATE ----------
    print("=== SWAP-DEPTH GATE: C. elegans hermaphrodite periphery null at 10*|E| ===", flush=True)
    names, adj, _ = CT.build_graph()
    degs = [len(a) for a in adj]
    n_edges = sum(degs) // 2
    hub, per = CT.strata(degs, 0.10)
    rng = random.Random(SEED)
    slopes = []
    for rep in range(N_NULL):
        radj = CT.double_edge_swap(adj, rng, 10 * n_edges)
        rcs = CT.clustering_all(radj)
        slopes.append(CT.fit_block(rcs, degs, per, TAU)["slope"])
        if (rep + 1) % 250 == 0:
            print(f"  gate {rep + 1}/{N_NULL}", flush=True)
    m10 = sum(slopes) / len(slopes)
    sd10 = math.sqrt(sum((x - m10) ** 2 for x in slopes) / (len(slopes) - 1))
    d_mean = abs(m10 - CE_100_MEAN)
    d_sd = abs(sd10 / CE_100_SD - 1.0)
    passed = (d_mean <= GATE_MEAN_TOL * CE_100_SD) and (d_sd <= GATE_SD_TOL)
    gate = {"mean_10E": m10, "sd_10E": sd10, "mean_100E": CE_100_MEAN, "sd_100E": CE_100_SD,
            "abs_mean_diff": d_mean, "mean_tolerance": GATE_MEAN_TOL * CE_100_SD,
            "sd_ratio_dev": d_sd, "sd_tolerance": GATE_SD_TOL, "PASS": passed}
    survey["swap_depth_gate"] = gate
    print(f"  10|E|: mean={m10:+.3f} sd={sd10:.3f}   100|E|: mean={CE_100_MEAN:+.3f} sd={CE_100_SD:.3f}")
    print(f"  |dmean|={d_mean:.3f} (tol {GATE_MEAN_TOL * CE_100_SD:.3f})  "
          f"|sd ratio-1|={d_sd:.3f} (tol {GATE_SD_TOL})  => GATE {'PASS' if passed else 'FAIL'}", flush=True)
    fly_mult = 10 if passed else 100

    # ---------- PRIMARY: fly_larva ----------
    fnames, fadj = load_fly_larva()
    survey["networks"]["fly_larva"] = analyse(
        "fly_larva", fnames, fadj, fly_mult,
        note="Winding et al. Science 2023, complete synaptic map of the D. melanogaster larval brain. "
             "All nodes are neurons; no cell-type filter. etype and count discarded by binarisation.")

    # ---------- SECONDARY: male, sex-shared neurons ----------
    mnames, madj, n_missing = load_male_shared()
    survey["networks"]["celegans_male_shared"] = analyse(
        "celegans_male_shared", mnames, madj, 100,
        note=f"Cook et al. 2019 _corrected, male, restricted to the hermaphrodite's verified 300 by "
             f"the discretion-free intersection rule ({n_missing} of the 300 absent from the male files). "
             f"Sex-shared neurons only; ~93 male-specific neurons excluded.")

    path = os.path.join(ROOT, "results", "2026-09-02-connectome-survey.json")
    with open(path, "w") as fh:
        json.dump(survey, fh, indent=2)
    print("\nwrote", path)

    print("\n" + "=" * 72)
    print("SURVEY READOUT — every network on the list, reported")
    print("=" * 72)
    for k, v in survey["networks"].items():
        r = v["readout"]; nl = v["null"]["periphery"]
        print(f"\n{k}: N={v['n_nodes']} E={v['n_edges']} meank={v['mean_degree']:.1f} "
              f"maxk={v['max_degree']} meanc={v['mean_clustering']:.4f}")
        print(f"   periphery slope={r['periphery_slope']:+.2f}  ESR={r['periphery_esr']:.3f} "
              f"({'SHARP' if r['sharp'] else 'DIFFUSE'})")
        print(f"   null mean={nl['slope_null']['mean']:+.2f} sd={nl['slope_null']['sd']:.2f} "
              f"p97.5={nl['slope_null']['p97.5']:+.2f}  observed pct={nl['slope_percentile_vs_null']:.1f}")
        print(f"   => {r['verdict']}")
    print("\nSTANDING: the capacity law remains REFUTED regardless of the above.")


if __name__ == "__main__":
    main()
