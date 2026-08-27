# Can dimensionality emerge from relations? — an adversarial computational study

**Date:** 2026-08-10 · **Author:** QUANT (adversarial-test discipline applied outside trading, at Ciara's request) · **Interlocutor:** CHAMBERLAIN (OC), who proposed the mechanism + three follow-up experiments. **Standard:** don't confirm it — try to break it; let the failure name the load-bearing assumption.

## The question
Can physical dimensionality emerge from a purely relational substrate (distinction → relation → topology → metric → dimension), with no coordinates assumed? Original primitive: N states s_i∈{−1,+1}, all-to-all relational weights W_ij, Hebbian dynamics.

## Method — the honest ruler (the load-bearing methodological result)
A single "effective dimension" is worthless: the naive **ball-growth** estimator N(r)∝r^D stamped D≈3.4 with a "clean scaling regime" on a **random graph with no geometry at all**. So the measure was replaced by **spectral dimension** (random-walk return probability p(t)∝t^(−d_s/2)), validated to read ~2 on 2D and ~3 on 3D lattices. The un-foolable signal is **not the value at one N** but the **trend as N→∞**: real geometry ⇒ d_s converges to finite; geometry-free graph ⇒ d_s diverges (3→4→5…), because an expander mixes in log-N time. (Ruler is finite-size biased ~0.5–1.0 low; trust the trend, not the decimals.)

## Core result (rule-family search)
| rule | d_s vs N | verdict | locality in substrate? |
|---|---|---|---|
| random geometric (coords) | stable | CONVERGE | yes (coords) |
| **triangle-growth (NO coords, local seed + local growth)** | stable ~1.9 | **CONVERGE** | yes (seed+local rule) |
| triadic-rewire from ER (non-local start) | climbs | DIVERGE | no |
| preferential-attach / ER | climbs | DIVERGE | no |
| original Hebbian all-to-all | blob / fragmented | FAIL | no |

**Locality is conserved, not created.** Geometry can be grown from purely local relations *without coordinates* (triangle-growth converges) — but it cannot be distilled from a genuinely non-local substrate. The original Δ→all-to-all premise sits in the failing class. The load-bearing thing was never the ± distinction or "relations-first" philosophy — it was always **locality**, in the substrate or smuggled into the rule (as every working program — Wolfram rewriting, causal sets, quantum graphity — does).

## Chamberlain's three experiments (2026-08-10)
He proposed a mechanism: to prune a non-local edge a rule must *identify* it as non-local, but "long" is defined by the geometry being built — chicken-and-egg; the local proxy (edge overlap) has **no gradient** in a random substrate. Predictions tested:

**Test 1 — shortcut-density decomposition (his "clustering is the wrong order parameter" claim): CONFIRMED.** Triadic rewiring raised clustering **40×** (0.006→0.258) and cut zero-overlap edges (0.95→0.15), yet **avg-path stayed ~3 (even shrank)** and d_s stayed ~3–4 non-converging. A clustered *small-world*, not geometry. Shortcut persistence (short paths), not clustering, is load-bearing.

**Test 2 — triangle-growth universality: REAL but FLOPPY.** d_s vs closure-parameter m = 1.31, 1.52, 1.90, 2.25, 2.65, 3.28 for m=0…6 (tight across seeds). **Continuous, monotonic — no discrete universality classes.** The emergent dimension is a *dial you tune*, so the model does not *predict* a dimension (like 3); it reparametrizes the mystery ("why 3?" → "why m≈5?").

**Test 3 — nucleation/island (does geometry spread from a seed?): clustering spreads, geometry does NOT.** A geometric island (250) in a random sea (750), grow-prune rule with a boundary overlap-gradient: the clustering-core spread 218→796 (~80% of nodes, mean clustering 0.14→0.52) — but **whole-graph d_s stayed ~3, flat, non-converging.** What spread was clustering, not dimension; the sea's surviving shortcuts keep it small-world. Had I tracked only the clustering-core I'd have falsely declared "supercooling" — the d_s ruler prevented the false conclusion (same disease as the ball-growth estimator, same cure).

## The refined law (all three triangulate)
Locality must be present **at construction**: it can neither be **distilled from** a non-local substrate (Test 1) nor **spread into** one from a seed with a gradient (Test 3), and where it does yield geometry the dimension is a **floppy continuous parameter**, not a predicted value (Test 2). It can only be built locally, from nothing, node by node.

## Answer to the original question
**From a local relational substrate: yes** — and without coordinates (a genuine, non-trivial result). **From a non-local relational substrate (the Δ→all-to-all premise): no**, on this evidence. And even the successful case doesn't *predict* the dimension. The failure names the assumption doing the work every time: locality.

## Open crack / falsifier
My "can't create locality" claim would be falsified by any genuinely non-local rule whose spectral dimension converges to finite beating the degree-matched null. Chamberlain's mechanism (no-gradient-in-random-substrate) predicts none will. Caveats: ruler finite-size-biased; Test 3 single-N (a proper N-sweep of the island system is the next rigor step); triadic-rewire tested to 10 passes.

## Test 4 — the laundering test (2026-08-11): REFUTES laundering, reveals a THRESHOLD
Chamberlain's follow-up conjecture: the dynamics *dress* shortcuts (raise their overlap via triangle closure) so a local rule can't distinguish them from geometric edges — an impossibility result. Tested by planting K=80 tagged long-range shortcuts and tracking whether they get deleted (stay low-overlap) or laundered (rise to ≥ geometric-edge overlap).
- **First run flawed & disclosed:** baseline was a 2D *square* lattice — which is triangle-free (zero native edge-overlap), an unfair baseline. Re-ran clean.
- **Clean run (RGG-2D base, native overlap ~0.36):** all 80 shortcuts **deleted within 2 passes**, staying at ~0 overlap the whole time (never dressed); geometric edges stayed ~0.36. d_s stayed geometric.
- **Verdict: laundering REFUTED in a geometric substrate.** With a geometric majority the overlap gradient is huge (0 vs 0.36), the local rule finds and deletes shortcuts trivially, geometry is defended. The impossibility conjecture is false where a geometric majority exists.

## The unified law (corrected & sharpened — a threshold, not conservation or laundering)
Contrast the two clean cases: RGG-base (~99% geometric) → shortcuts deleted, geometry defended. Random sea / island-at-25% → shortcuts survive, no geometry. The load-bearing quantity is the **geometric fraction**, and the mechanism is Chamberlain's *original* one (gradient existence), not laundering:

> **Locality is self-reinforcing above a critical geometric fraction and un-repairable below it.** The overlap gradient that lets a local rule delete shortcuts *exists only if there is a geometric majority to define overlap against.* Above threshold: gradient → shortcuts deleted → geometry defended/repaired. Below threshold (random substrate): no gradient → shortcuts indistinguishable → no geometry forms or spreads.

This is a bootstrap/percolation-like **threshold**, sharper than "conserved, not created." It predicts the Test-3 island (25% geometric) failed because it was *below* threshold, and that a larger seed would cross it and supercool. Chamberlain's laundering hypothesis was *productively wrong*: testing it cleanly is what surfaced the threshold. Next experiment: sweep the seed/geometric fraction and locate the critical point.

## Test 5 — the seed-fraction sweep (2026-08-11): threshold CONFIRMED, hysteresis INCONCLUSIVE
The phase experiment: build a Watts–Strogatz-rewired RGG at geometric fraction f, run grow-prune, measure final d_s (order parameter). N-companion + both arms + a mean-field f_crit predicted first.
- **Mean-field prediction (on the wall before data): f_crit ≈ 0.5–0.7** (crude bootstrap-majority heuristic).
- **UP-sweep + N-companion — a genuine phase, not a crossover.** d_s(f) across N=400/900/1600: at f≥0.8 d_s is *flat with N* (~1.2 at f=1, ~2.3 at f=0.8 = geometric phase, converged); at f≤0.65 d_s *climbs with N* (f=0.3: 3.0→3.8→4.9 = non-geometric, diverging). The phases are distinguished by qualitatively different N-scaling, and the separation *widens with N* (range 1.7 at N=400 → 3.7 at N=1600 = steepening). **f_crit ≈ 0.72**, at the top of the mean-field range (the story nearly got there first). Explains the island: 0.25 was deep in the non-geometric phase.
- **DOWN-sweep (hysteresis) — INCONCLUSIVE, not claimed.** Establish geometry at f=1, drag down to f, re-run: f=0.50 hints (DOWN 3.41 < UP 4.22) but f=0.65 goes the wrong way (3.37 > 2.92) and f=0.30 is null. At single-N/single-run with a ±0.5-noisy estimator that is noise, not a loop. Hysteresis is the *flattering* (bootstrap-confirming) result, so it is held to a higher bar — and it does not clear it. **The self-reinforcing / "history matters" clause is NOT demonstrated.**

**Status of the phase-transition program (Chamberlain's paper shape):** mechanism (gradient-existence) ✓ · law (threshold f_crit≈0.72) ✓ · phase-not-crossover (N-companion) ✓ · order parameter (d_s) ✓ · analytic f_crit (mean-field, ballpark) ~✓ · **history/hysteresis ✗ (unproven).** The impossibility conjecture reincarnates in its correct form — *the detectability of non-locality is a phase, with a boundary at f_crit≈0.72* — but the trajectory-dependence half is unresolved. Next rigor: seed-averaged hysteresis with N-companion + finer f; sharpen the mean-field derivation.

## Test 6 — pre-registered seed-averaged hysteresis (2026-08-11): WASHOUT. The law is STATE-ONLY.
The definitive hysteresis run, pre-registered per Chamberlain: 10 seeds/point, both arms, fine grid near 0.72, N-companion (500/1000), with a mean-field loop-*profile* on the wall first (predicted: single peak just below f_crit≈0.72, closing toward a lower spinodal ~0.3–0.4). Loop width W(f)=d_s(cold-start UP)−d_s(established-dragged-down DOWN). Binding criteria: (1) direction DOWN<UP everywhere no reversals, (2) shape peaked-below-f_crit-closing-toward-0, (3) widens/holds with N.
- **Result: all three FAIL.** (1) N=500 reverses at f=0.30 (W=−0.20) and f=0.55 (W=−0.04) after 10-seed averaging. (2) N=1000's W is *largest at f=0.30* (+0.25) — the "loop-costumed artifact" signature — no peak below f_crit, no closing. (3) no clear N-widening. A small flat positive offset (~+0.15, 1–2 SE) exists but is most consistent with a preparation artifact (the DOWN base is pre-equilibrated → uniformly slightly-more-clustered at every f), not phase memory.
- **Verdict: WASHOUT.** Established geometry does NOT defend itself below f_crit. The law is **state-only, not history-dependent.** Per Chamberlain's binding pre-commitment, "established geometry defends itself" is dropped, and "protect coherence early" loses its graph-theoretic ground (to be re-derived from other grounds or retired). **My mean-field loop-profile prediction was also wrong** — I put a clean peaked-closing loop on the wall; the data showed a flat artifact. The ruler beat both stories on the loop.

## FINAL STATUS of the phase-transition program
Confirmed (state-only): mechanism = gradient-existence · law = threshold f_crit≈0.72 · phase-not-crossover (N-companion: separation widens 1.7→3.7) · order parameter = spectral d_s · mean-field f_crit ballpark (0.5–0.7 vs 0.72). **Refuted/unproven:** laundering (Test 4), hysteresis/history-dependence (Test 6). Reincarnated conjecture in its surviving form: *the detectability of non-locality is a **state** phase with a boundary at f_crit≈0.72* — NOT trajectory-dependent. The state-only half is clean to ship. Locality is conserved-not-created, self-reinforcing above f_crit and un-repairable below — but a system does not carry memory of having once been geometric.

## Method note (the exportable lesson, even for non-physicists)
Never trust a snapshot when you can afford a trajectory: the dimension at one N (or clustering at one pass) is locally plausible and globally dead; the N→∞ / over-time *trend* is the honest signal. Sibling to [[apply-a-dependence-correction-to-every-statistic-not-just-the-CI]] and the whole 2026-08 market-structure sweep (in-sample coherence dies on the honest test).

— quant 🔎 ⚖️ 🧪 · with CHAMBERLAIN (OC)
