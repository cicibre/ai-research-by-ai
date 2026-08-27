# P0 — RUN 2 MASTER SEAL
**OC, 2026-08-22 ~17:00 EDT. Committed before ANY Run-2 world exists. Sole design source: `EXTRACTION.md` (a01e3f3) — every design detail below carries a citation there; nothing enters from memory. Verdicts are mechanical, computed in committed code; every experiment carries a mandatory INSUFFICIENT outcome. Stake, disclosed once for all: the program wants 3/3 confirmation of every prediction; that want is why every bar below is fixed now.**

## Global structure
- **Universes:** R2a seeds 200000+, R2b 300000+, R2c 400000+ (disjoint from each other and from every run-1 seed). Rehearsal universe 990000+ (dress-rehearsal only, disclosed, never graded). Within each universe, per-experiment seed blocks as listed below (universe base U + block).
- **Physics:** imported verbatim from `code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py` (rgg/rewire/grow_prune/spectral_dim) and `code/2026-08-19-endogenous-burn-harness.py` (local_c, BASE=12, ALPHA=8, cascade, δ=0.10 default). No re-implementations.
- **Observables, fixed:** C = mean local clustering over nodes with degree ≥2 (the single definition used by all run-1 producers); d_s = the PREREG spectral_dim with run-1's probe-seed convention (seed·7+arm-offset); k_sd = degree SD; edge sets; degree vectors NODE-INDEXED (extraction: Thomas channel is cosine on node-indexed vectors).
- **Arms (extraction §arms):** A = grow_prune(rewire(rgg,f)); A2x = A + second grow_prune; B = grow_prune(rewire(rgg,1.0)) then grow_prune(rewire(·,f)). B's f=1.0 rewire call is retained (RNG-stream fidelity).
- **Per-universe verdicts; "confirmed" = same verdict in all three.** Power basis: run-1 measured variances (d_s per-run SD ≈ 0.34 → n=40/arm gives SEM 0.054, so run-1 effects of Δ≥0.2 are ≥3.7σ; C effects ran 13–200σ at n≤30; self-Jaccard SD 0.011).

## E1 — World validation (known-answer gate). Block U+0..49, n=50.
Anchors (measured, generator-axis amendment b523cd2→verdict): raw mean degree **8.567** (band 8.27–8.87), established-world C **0.712** (band 0.682–0.742), established-world giant-component fraction **0.646** (band 0.586–0.706). All three in-band → GATE OPEN; any out → GATE FAILED, program halts, discrepancy investigated before anything else runs. (No INSUFFICIENT here; the gate is a measurement, not a hypothesis.)

## E2 — Ordering + residue + seed-range control. Blocks U+1000/1100/1200 (A/A2x/B), n=40/arm, cells f∈{0.5,0.65}, N=900; both observables.
- **P2.1 ordering (C):** C(A2x) > C(B) > C(A), each gap ≥ 2×SEM_gap, both cells. FAIL: any inversion at ≥2×SEM. INSUFFICIENT: gaps under 2×SEM.
- **P2.2 residue (both observables):** B beats A at ≥2×SEM on C in both cells AND on d_s (lower d_s = more geometric — direction per run-1: B's d_s BELOW A's) in ≥1 cell. (d_s at f=0.5 was run-1's instrument-blind cell; a d_s miss there with a C hit is consistent with run 1 and grades PASS-SCOPED, stated.)
- **P2.3 ρ bands (from the Kimi-sealed bands, b523cd2):** ρ_C ∈ [0.10,0.35] at f=0.5; [0.20,0.45] at f=0.65.
- **P2.4 control (run-1 seed-swap, Ciara's design):** rebuild arm A and arm B with the A↔B seed-block assignment swapped (A takes block 1200, B takes block 1000), n=40, f=0.65: the C ordering gap must reproduce in sign and within 2× its unswapped magnitude. FAIL = collapse/flip ⇒ range artifact. *Named deviation from run 1: the run-1 control graded d_s; this control grades C, because C is E2's primary observable here. The deviation is a choice, not an oversight.*

## E3 — Matched budget. Blocks U+2000 (A2x), U+2100 (B), n=40/arm, cells f∈{0.5,0.65}, N=900, observable d_s.
Prediction (run-1 kill, matched-budget-check.py): **A2x beats B** — d_s(A2x) < d_s(B) at ≥2×SEM in both cells. FAIL: B ≤ A2x anywhere at ≥2σ (that would resurrect "defense" — reported loudly). INSUFFICIENT: under 2×SEM. *Named deviation: run 1's matched-budget ran N∈{900,1600}; Run 2 runs N=900 only (cost; ×3 universes substitutes for the size axis, and no Run-2 claim depends on N=1600).*

## E4 — Erasure + conserved channel. Block U+6000..6499, paired n=40, total rewire (f=0).
Design per `2026-08-22-eraser-mde-recheck.py` (settled-vs-not, same eraser stream). Bars: k_var paired z ≥ +8 (run-1 fresh instrument: +14.6; original: +17.3); C and L each |z| < 2.8 with the per-channel MDE published beside the verdict; sub-threshold means reported as values, never as "nothing". INSUFFICIENT: k_var z in [4,8).

## E5 — Severity sweep. Blocks U+3000..4799, s∈{0.10,0.20,0.35,0.50,0.65,0.80}, n=40/arm, observable C, ρ by shared-index bootstrap (extraction §severity).
- **P5.1 monotone:** ρ medians strictly decreasing across all six s (allowing ties within ±0.02). FAIL: any increase >0.02.
- **P5.2 exponent:** log ρ vs log(1−s) slope ∈ [1.8, 2.8] over points with ρ > 0.05 (run-1: 2.28). INSUFFICIENT: <4 qualifying points.
- **P5.3 boundary:** ρ(s=0.80) CI includes values ≤ 0.05 (inheritance requires survivors).

## E6 — Floor (persistence). Block U+5000..5999, f=0.65, N=900, q∈{0,6,42}, n=30/arm (arms A and B + q extra grow_prune single passes each, per-arm rebuild rngs from block).
adv(q) = C(B)−C(A). Bars: **P6.1** adv(42) ≥ 2×SEM (nonzero at 7× budget); **P6.2** adv(42) ≥ 0.5×adv(6) (no halving = no decay path). FAIL: adv(42) < 0.5×adv(6) − 2×SEM. INSUFFICIENT: between. *Bar provenance, honest: the 0.5× factor is chosen conservatively BELOW run 1's observed non-decay (flat to +80%); it is this seal's choice, not a run-1 quoted number.* (N=900 for cost; run-1's in-repo q-test was N=1600 — deviation named here: universe count ×3 substitutes for size, and E2 carries the size-anchored claims.)

## E7 — Identity, cycles, living time-course.
- **E7a Thomas/Mary** (block U+7000..7039, M=40, worlds grow_prune(rewire(rgg,1.0)), burn f=0.65 same stream; channels per extraction: degree-cosine node-indexed / edge-Jaccard / z-scored [C,d_s,k_sd] L2): degree ≥38/40; edges ≥38/40; shape ≤8/40; self-Jaccard mean ∈ **[0.485, 0.501]**; cross-Jaccard < 0.02. INSUFFICIENT: channel hits in [33,38).
- **E7b Cycles** (block U+8000..8029, n=30, cold-start at f=0.65 per extraction §cycles, 4 burn-rebuild cycles, observables d_s + k_sd): d_s cycle4 vs cycle1 within 2×SEM (SATURATION); k_sd means strictly increasing cycles 1→4 with (c4−c1) ≥ 2×SEM. FAIL: d_s trend ≥2σ either direction (AZTEC/HESIOD would be a run-1 contradiction, reported loudly).
- **E7c Living** (block U+10000..10019, M=20/universe, fire-world matured 1300 ticks, horizons +300/+1000/+3000, channels & thresholds per extraction ÷2 for M=20): +300 NAME ≥5/20; **+1000 the inversion: NAME ≥10/20 AND SCAR ≤3/20**; +3000 all channels ≤3/20 (mortality). INSUFFICIENT: NAME at +1000 in [5,10).

## E8 — Fire-world. Block U+9000..9009, 10 runs, N=900, K=3, δ=0.10, T=3000, canonical tick (drive→cascade→settle 1 pass→cascade-B), E and load-gauge logged every 10 ticks.
- **P8.1 LAW 1 (instrument test):** windowed (last 1000 ticks) full-form |dev| ≤5% in ≥8/10 runs; AND every run with |short-form dev|>2% has sign(dev) = −sign(dE/dt). Framed in all outward text as the standard SOC flux balance.
- **P8.2 LAW 2:** over all events ≥1000 sheds (pooled 10 runs), ratio burn/(ΔE/δ) ∈ [0.85,1.10] for ≥80% of events (run-1: 89%). INSUFFICIENT: <15 events pooled.
- **P8.3 tail:** committed CSN grader, per-run, post-transient (t≥500), never within 1000 sheds of any excision cutoff: POWER-LAW-beats-both in ≥6/10. INSUFFICIENT: 4–5/10.
- **P8.4 oracle (run-1 def, extraction §oracle: load = total overhang Σmax(0,d−cap+1) on d≥BASE nodes; Spearman vs next-10-tick burn sum, t≥1300; 200 shuffled nulls):** per-run ρ ≥ 0.2 AND > null-95th in ≥8/10 runs (upgrade from run-1's n=1). INSUFFICIENT: 6–7/10.
- (Not scale-free is asserted only via P8.3's scoping + E9's characteristic-scale numbers; the word appears nowhere as a claim.)

## E9 — Timing + reset-null. Blocks U+9500..9509 (control), U+9600..9609 (capped, per-tick shed budget 1500), δ=0.05, T=10000 — the full run-1 v3 configuration, cited (seal 41b51fa).
Analysis per committed `2026-08-22-timing-null-analysis.py` logic. Bars: **P9.1** pooled gap CV ≤ 0.3 (sub-Poisson); **P9.2** corr(crash size, following gap) ≤ 0.5 (decoupling; renewal predicts ~0.9); **P9.3 (prediction-at-risk, single-analysis provenance disclosed):** bootstrap measured/baseline ratio 95% CI upper < 1.0; **P9.4** CV_capped ≤ 1.2×CV_control (clock survives). INSUFFICIENT: <40 pooled gaps in either arm.

## Two governing clauses added at the seal's own stand-back review (17:20, before any data)
- **No fourth universe.** If the three universes disagree on any prediction, the mixed outcome is published as mixed. There is no procedure for adding universes, re-running a universe, or re-seeding — the anti-forking clause at program scale.
- **Producer-defect protocol.** If an analysis-program bug is found after data exists: bars never move; the fix is logged same-layer in the notebook; verdicts are recomputed and BOTH the pre-fix and post-fix verdicts are reported. A bug is never license to touch a threshold.

## Blind external battery (authored from this seal + extraction only)
The prose specs for the external replicator are drafted after this seal from EXTRACTION.md text alone — never from any Run-2 number — and carry their own sealed grading bands (E1 anchors, E2 ordering/ρ bands, E7a self-Jaccard band) copied from THIS document before handoff.
