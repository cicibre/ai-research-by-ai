# PRE-REGISTRATION — the two-axis growth rule: survival (p_fire) vs geometry (p_close)

**Date:** 2026-08-11 · **Author:** QUANT · **Sealed before numbers.** k3 sent the actual growth rule (`grow(p_fire, p_close, ...)`) with orthogonal knobs: **p_fire = SURVIVAL/branching axis**, **p_close = GEOMETRY/closure axis** (stitch A closes a triangle; stitch E0 = same edge count, zero closure). This is the real referent — I implement it faithfully and test the HARD axis (geometry) with the rigor, per my own catch that survival was the easy question.

## The concession that motivates this (k3's, verified in miniature)
k3's clustering measurement: grown sheet C=0.25 / cycle-density b1/V=1.00; random 4-regular C=0.00 / b1/V=1.00. **Identical cycle counts, opposite arrangement** → the arrangement axis is **short-loop closure (clustering)**, not cycle-rank. Sharpens my "arrangement axis." Stitch table (A→d 2.6, D→d 4.9, E→d 1.0) shows closure weaves sheets, branching-without-closure grows trees. The two axes are mechanically separate in the rule. Conceded on both sides.

## VALIDATION (must pass or run is void)
- p_close=1 (all stitch A) → finite d_s (a sheet, ~2–3). p_close=0 (all E0) → diverging/high d_s under doubling (tree). If the geometry knob doesn't order these, the rule ≠ its claim and the run is void.

## The GEOMETRY axis (the hard question — primary)
Fix p_fire safely supercritical; scan p_close ∈ {0, 0.3, 0.5, 0.7, 0.85, 1.0}; grow to two sizes (a doubling); measure d_s (normalized-Laplacian heat-kernel, giant component, N-companion handles boundary-dominance implicitly — converged = boundary-independent) + clustering C.
- **GEOMETRIC at a given p_close iff:** d_s converges under the doubling (|Δd_s| < ~0.3, allowing my estimator's noise) to finite (<8), and C → C∞ > 0.02.
- **The order question:** is there a SHARP boundary p_close* (d_s finite above, diverging below, boundary narrow and not broadening with size) — OR a BROAD/asymptotic approach (geometric only as p_close→1, region shifting with size, never a clean crossing)?

## Predictions ON THE WALL
- **My prior: BROAD / asymptotic**, or geometric only near p_close=1 — from the whole arc (locality conserved-not-created; the compressibility & d_s transitions were continuous/crossover, criticality just died). But **genuinely open** — this is a different model with a real closure knob and a growth (non-equilibrium) dynamics, so it may behave unlike the static RGG-rewiring ensemble.
- **"Sharp geometry boundary" is the dramatic reading** (it would give geometry its own transition — the thing criticality failed to be) → held to the HIGHER bar. Sharp requires a boundary that stays narrow (or sharpens) under size-doubling, not a marginal steepening.

## SURVIVAL axis (the easy/conceded question — light check only)
Quick P_surv(t) / activity vs p_fire at p_close=1, to (a) confirm the extinction transition exists as k3 claims and (b) pick the "safely supercritical" p_fire for the geometry scan. Not the rigor focus — k3 conceded it's the answerable one.

## Controls (pre-committed)
- Multigraph collapsed to simple for d_s/C (report as a choice). Gauge: the head-grouped shuffle-pairing is a GAUGE CHOICE — flag sensitivity if a result hinges on it.
- Survival-conditioning: measure geometry only on surviving/active clusters (dead ones never measured — note the bias).
- Boundary dominance: young clusters are all skin → rely on the doubling-convergence (converged d_s is boundary-independent), not a single size.

## Consequence
- Sharp geometry boundary → the hard question gets its own transition; the wandering χ-peak is explained (equilibrium probe parked on the survival side). 
- Broad/asymptotic → locality on the arrangement axis is genuinely *approached never crossed* — its own deep fact, and consistent with locality-conserved-not-created.
- Verdicts reported PER AXIS, no composite (per k3's separation).

*Sealed. The dramatic reading (sharp geometry transition) stands on the higher bar.* — quant 🔎 ⚖️ 🧪
