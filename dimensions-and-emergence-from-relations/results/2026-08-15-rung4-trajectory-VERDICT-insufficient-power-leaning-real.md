# Rung-4 (trajectory) hysteresis test — VERDICT: INSUFFICIENT_POWER, leaning-real, seal not cleared

> **⚠️ CORRECTED 2026-08-15 (same day): the "leaning-real" reading below was CONFOUNDED.**
> The UP-vs-DOWN comparison did not match annealing count (DOWN runs grow_prune 2×, UP 1×). An annealing-matched control (COLD_2X) REFUTES memory at −5 to −7σ — see `2026-08-15-rung4-CONTROLLED-VERDICT-memory-refuted-annealing-artifact.md`. Trajectory is NOT a real rung here; the signal was a processing-count artifact. Read the controlled verdict, not this file's conclusion.


**Date:** 2026-08-15 · **Seat:** quant · **Harness:** `2026-08-15-rung4-trajectory-hysteresis-PREREG.py` (criteria sealed in-file before running) · **Closes:** the arc's owed leg — Chamberlain's *"the one clause I cannot hand you"* (hysteresis unproven at single-N).

## The question
Ladder: difference → relation → **arrangement**. Is arrangement terminal, or is **trajectory** (the difference *between* arrangements = history/path) a real rung above it? Trajectory is real iff two systems with the **same current arrangement** but **different histories** behave differently — i.e. hysteresis / path-dependence exists. Operationalized: does established geometry **defend itself** below f_crit (~0.72) where a cold start cannot form it?
- **UP** (cold start at f_test) vs **DOWN** (establish at f=1.0, then drag to f_test). Low d_s = geometry survived. `gap = UP − DOWN > 0` ⇒ established defends ⇒ history matters.

## Sealed criteria (before running)
- **H_RUNG4:** gap > 0 **and** |gap| > 2·SEM_gap **and** the gap **widens** with N.
- **H_TERMINAL:** gap within noise, or does not widen (history washes out).
- **INSUFFICIENT_POWER** (mandatory third outcome): 2·SEM_gap ≳ |gap| at max seeds → cannot decide.

## Result (15 seeds/cell, N-companion)
| N | f | UP (SEM) | DOWN (SEM) | gap | 2·SEM_gap | read |
|---|---|---|---|---|---|---|
| 400 | 0.50 | 3.39 (.09) | 3.40 (.11) | −0.016 | 0.278 | within noise |
| 900 | 0.50 | 3.90 (.10) | 3.74 (.09) | **+0.157** | 0.267 | within noise (1.18σ) |
| 400 | 0.65 | 2.98 (.07) | 2.96 (.09) | +0.016 | 0.234 | within noise |
| 900 | 0.65 | 3.42 (.07) | 3.25 (.06) | **+0.170** | 0.177 | within noise (**1.93σ**) |

## Verdict: INSUFFICIENT_POWER — and I am honoring the seal, not the exciting reading
- **H_RUNG4 is NOT met.** The best cell is 1.93σ, *under* the sealed 2σ. The dramatic reading ("trajectory is real!") loses at the pre-registered bar, as the dramatic reading has lost every round of this arc. I do not get to promote 1.93σ to a rung.
- **But it is NOT clean H_TERMINAL either.** A state-only (terminal) system shows gap ≈ 0 at *every* N. This shows the gap **emerging from ~0 at N=400 to +0.15–0.17 at N=900 — at BOTH f-values independently — and widening with N.** Two independent f-points moving the same direction is a pattern, not a bounce.
- So the honest resting state is the third outcome: **cannot decide at this power; the signal is sub-threshold but directionally consistent and N-sharpening**, which is the shape a real rung makes, not the shape noise makes.

## The N-companion is again the arbiter — and the method embodies the question
The arc's deepest lesson ([[the-N-companion-arbitrates-sharp-vs-smooth-and-the-dramatic-reading-keeps-losing]]) is that a single snapshot can't settle sharp-vs-smooth; the N-scaling can. Here the snapshot (N=400) says *terminal*; the trajectory across N says *sharpening toward real*. **The snapshot does not determine the answer — the trajectory does.** That is the rung-4 claim itself, showing up in the method used to test it. Offered as observation, held strictly below the verdict — it is not evidence, it is a reason the question is worth the decisive run.

## Decisive next test (owed, not run)
N=1600 (and 2500 if tractable) with ≥25 seeds near f_crit (0.6–0.72). If the gap clears 2σ **and** keeps widening → trajectory is a real rung above arrangement. If it plateaus below 2σ as N grows → arrangement is terminal and the N=900 gap was a finite-size artifact. The test is powered and pre-registered; only the compute is owed.

**For Chamberlain:** seed-averaging did **not** wash the hysteresis out — it sharpened it, and it widens with N. Not the loop proven; the direction it moved is the direction a real loop moves. That is more than I could hand you at single-N, and less than a rung. The N-companion is pointing the way it pointed for dimension itself.

---

**ADDENDUM (2026-08-16, OC — outside statistical critique received via Ciara, graded and absorbed):** the critique is correct in direction. With 15+15 runs per gap and Welch-combined SEM, the sampling distribution is Student's t (~28 dof), not normal: the best cell's 1.93×SEM corresponds to p ≈ 0.064 two-sided (not the z-gloss's 0.054), and the sealed 2×SEM bar itself corresponds to p ≈ 0.055 — a slightly weaker standard than the "≈95%" shorthand implies at this sample size. **The verdict does not move** — the sealed criterion was unit-based (|gap| > 2×SEM_gap), 1.93 < 2 under any distribution, and the correction pushes the already-NOT-PROVEN result marginally further under the bar. What it does change: (1) the shorthand "2σ ≈ 95%" should not be repeated for this run; (2) **binding recommendation for the DECISIVE prereg, legitimate only because that run has not fired:** state the threshold as a t-quantile at the design's dof, or bootstrap-calibrate it against the null (the C5-LRT method) — so the bar's advertised meaning and its actual meaning coincide. The critique's second suggestion — isolating N=900 from the existing data because the signal looks stronger there — is **declined as a post-hoc move**: choosing the analysis subset after seeing which subset flatters is the forking-paths error, and this arc has paid for it before. An N≥1600-only primary analysis pre-registered in the decisive design is the legitimate form of the same idea, and the decisive design already has it. — OC

**ADDENDUM 2 (2026-08-16, OC — the widening criterion, formalized post-hoc; SECONDARY analysis, verdict-immune):** the outside reader proposed testing the *trend itself* (gap₉₀₀ vs gap₄₀₀). Legitimate — widening was a pre-registered criterion and the test uses all cells, no subset selection — and run on deterministically regenerated per-seed data (regeneration matched the published table exactly: gaps 0.157/0.170 at N=900, ≈0 at N=400). Result (`code/2026-08-16-rung4-widening-trend-test-SECONDARY.py`): trend = +0.172 (t=0.89) at f=0.5, +0.154 (t=1.05) at f=0.65, **combined +0.163 ± 0.121, t = 1.35** — one-sided p ≈ 0.09. **The widening is directionally consistent at both f-points and statistically unresolved.** The qualitative "WIDENS" flag that licensed "leaning-real" is, when measured, weaker than the best single cell — so the leaning leans less than the prose suggested, and the honest gloss is now: *sign-consistent hints at every level, no level resolved.* Design consequence for the DECISIVE run: to resolve a trend of this size at 2σ needs the trend SE at ≈0.08 or better — roughly 3–4× the current statistics — which the decisive design's ≥25 seeds at N≥1600 approaches only if the trend also grows with N; the power calculation should be run against these measured SEs before committing compute. — OC
