# VERDICT — the two-axis growth rule: survival is a sharp transition, geometry is a SMOOTH DIAL (no sharp boundary, both axes)

**Date:** 2026-08-11 · **Author:** QUANT · **Pre-reg:** `2026-08-11-two-axis-growth-PREREG.md` (sealed). **Model:** k3's exact `grow(p_fire,p_close)` (p_fire=survival/branching, p_close=geometry/closure; stitch A closes a triangle, E0 = same edge count zero closure). **Harness:** `2026-08-11-two-axis-harness.py` (+raw output). Faithful implementation; interior-patch subsampling to EXACT sizes 700/1400 (clean 2× doubling + boundary control + tractable eig, after a first harness overshot on explosive growth and was killed).

## SURVIVAL axis (p_fire, p_close=1) — SHARP, as branching theory predicts
Activity/extinction transition between **p_fire ≈ 0.1 and 0.3**: p_fire=0.1 → 82% active, median 99 edges (near extinction); p_fire≥0.3 → 100% active, 400k–560k edges (explosively supercritical). Confirms k3's absorbing-state/extinction transition — the survives-or-dies question is sharp by construction. The EASY axis, cleanly answered YES.

## GEOMETRY axis (p_close, p_fire=1) — NO SHARP BOUNDARY; a smooth finite dial
d_s(p_close), interior patch, exact 700 vs 1400 doubling (5 replicas):

| p_close | d_s@700 | d_s@1400 | \|Δ\| | C |
|---|---|---|---|---|
| 0.00 | 1.35 | 1.38 | 0.03 | 0.00 |
| 0.30 | 1.40 | 1.43 | 0.03 | 0.17 |
| 0.50 | 1.49 | 1.52 | 0.03 | 0.23 |
| 0.70 | 1.65 | 1.65 | 0.00 | 0.26 |
| 0.85 | 1.76 | 1.83 | 0.07 | 0.29 |
| 1.00 | 1.88 | 1.92 | 0.05 | 0.31 |

- **d_s converges under the exact 2× doubling at EVERY p_close** (|Δd_s| ≤ 0.07) → everything is finite-dimensional; nothing diverges. The same heat-kernel estimator that made expanders CLIMB earlier this arc shows these all SETTLE.
- **d_s is a smooth, monotonic, finite dial** (1.35→1.92) — no jump between any grid points, no divergence below any threshold. → **SHARP geometry transition NOT supported** (held to the higher bar per pre-reg). The **BROAD/continuous reading holds**, stronger than "asymptotic": geometry (finite low-d) is present at *all* closure levels; closure tunes line(~1.4)→sheet(~1.9).

## Validation nuance (my pre-reg expectation corrected)
I pre-registered "p_close=0 → diverging tree." WRONG mental model: this rule's E0 makes a **line** (d_s~1.3), matching k3's own stitch table (E→line, d=1.0), NOT a bushy divergent tree. The knob works (C 0→0.31, d_s 1.35→1.9 monotone) but spans **line↔sheet (both finite, low-d)**, not geometric↔expander — so this rule has no non-geometric phase to transition into; geometry is always present. d_s biased ~0.5 low (finite-size); the p_close=1 "1.9" ≈ k3's 2.6 modulo estimator/size.

## Caveats (honest)
Coarse p_close grid (a boundary in a sub-grid window can't be fully excluded, though the smooth monotone trend argues against it); 5 replicas, means only; the rule never builds an expander, so this tests line-vs-sheet not geometric-vs-non-geometric.

## Through-line (fifth dramatic reading down)
Geometry-as-a-phase-with-a-boundary is now unsupported on **both** axes: equilibrium χ-scan wandered (no critical point, `criticality-FSS-VERDICT`), growth-arrangement scan is a smooth finite dial (this). Consistent with the whole arc: **geometry is a continuous relational property you tune, not a phase you cross into.** Survival IS sharp (branching theorem); geometry is NOT (both the equilibrium and the growth probe agree). The two-currency rent stands: branching = survival rent (sharp threshold), closure = geometry rent (smooth dial) — you pay continuously for more geometry, there is no lump-sum barrier and no free lunch.

Sibling: `2026-08-11-criticality-FSS-VERDICT-not-critical.md`, [[a-falsification-needs-a-third-outcome-insufficient-power]].

---
## Addendum — the lung: d_s is blind to space-filling trees (Ciara's catch, tested)
Ciara: "the lung forms branches and tree roots and their branches too." A real catch on my ruler's SCOPE: a lung/root/vascular tree fills space (fractal d_f≈3) with ZERO loops, and **spectral d_s undercounts it** (a walker traps in dead-end branches → tree d_s≈4/3, same as a line). So my "smooth dial" verdict was measured only on the route d_s can see (closure). Tested it — measured ball-growth d_f alongside d_s across p_close (`2026-08-11-two-axis-df-harness.py`):

| p_close | d_s | d_f |
|---|---|---|
| 0.00 | 1.38 | 1.57 |
| 0.50 | 1.52 | 1.79 |
| 1.00 | 1.93 | 2.23 |

- **d_s DOES undercount (d_f > d_s by ~0.3 throughout)** — the lung's warning confirmed in principle.
- **BUT our rule's branching is a LINE, not a lung:** at p_close=0, d_f=1.57 (low). A real lung would show d_f≈3 vs d_s≈1.3 (gap ~1.7); here the gap is ~0.2 and does NOT widen toward the branch end. E0 branches into a line, not a volume. No hidden space-filling tree for d_s to have missed — the failure mode was checked and absent.
- **Verdict robust on BOTH rulers:** d_s AND d_f are each a smooth monotone dial with closure, no sharp boundary. "Geometry is a continuous dial, not a phase you cross" survives the change of dimension-measure. (d_f reads 1.6–2.2, sensible — not the fooled ~3.4 it stamped on expanders 08-10, confirming these are genuinely low-d.)

**The deeper point the koan surfaces:** nature fills space by TWO routes — (1) closure → loops → lattices/sheets → high d_s (our rule's only, weak, route); (2) space-filling BRANCHING → trees → lungs/roots/vasculature → high d_f, low d_s (the lung IS this — absent from our rule). A lung needs a THIRD stitch that branches to *fill volume* (split angles + length-scaling), neither closing a loop (A) nor collapsing to a line (E0). The rule has a closure knob and no space-filling-branching knob; the lung says there should be one. My ruler was half-blind to route (2); measured the gap; the rule doesn't exploit it, but nature does everywhere.
