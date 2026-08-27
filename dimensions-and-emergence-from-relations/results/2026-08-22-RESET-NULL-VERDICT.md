# RESET-NULL VERDICT: CLOCK-SURVIVES-WITHOUT-RESET — the whole-system reset is NOT what makes the clock
**OC, 2026-08-22 ~12:20 EDT. Per seal v3 (41b51fa); bars unchanged from v1 (99830d6). Graded mechanically. My sealed stake wanted the opposite outcome and is hereby reported against.**

## The run (v3: 10 seeds/arm, N=900, K=3, δ=0.05, T=10000)
| arm | scoreable | events/run | mean period | pooled gap CV |
|---|---|---|---|---|
| CONTROL (full discharge, max burn ~33k) | 10/10 | 9–10 | ~1000 ticks | **0.070** |
| CAPPED (shed budget 1500/tick — system-scale discharge impossible) | 10/10 | 9–10 | ~1000 ticks | **0.068** |

Ratio 0.96× — statistically indistinguishable. Sealed bar for CLOCK-SURVIVES: ratio ≤ 1.2×. **Met decisively.** No degeneration (capped event-tick fraction 2.2% vs the 30% tripwire).

## What it means
Capping the discharge at 1500 sheds/tick abolishes the single-stroke system reset — the capped arm's crashes are ~25-tick plateaus instead of one-tick spikes — yet **period AND regularity are unchanged to two decimal places.** The whole-system phase reset was never the clock. The discharge's *shape* is irrelevant; only its *budget* matters: each event still settles the same edge account (LAW 2's ΔE/δ, spread over a plateau), and the refill time of that account (K − δ·B_quiet, per LAW 3) is untouched by the cap. **What is ruled out: the whole-system reset as the clock. What is left standing — the surviving hypothesis, NOT a proven mechanism: the charging circuit** (the deficit integrates low-variance inflow, so the threshold-crossing time concentrates — a budget consequence). *Same-layer amendment, ~12:25, at the external reviewer's caution: the original sentence here asserted the charging-circuit account declaratively; it has exactly the epistemic status reset-synchronization had yesterday — the survivor of one ablation at one δ and one cap. Stated as hypothesis so row 9 doesn't write itself.* "History persists in what the dynamics conserve" — and so, it turns out, does rhythm.

Consequence for the lab note: the clockwork section's mechanism sentence flips — not "whole-system reset wiping the phase" (that guess is now dead) but "reset ruled out; budget integration is the account left standing." Arguably a STRONGER lead than the confirmed version would have been: the model's most striking phenomenology (near-deterministic rhythm) is derivable from the budget and survives ablation of its most conspicuous feature.

## The road here — two INSUFFICIENTs, on the record
- **v1 (99830d6): INSUFFICIENT** — sealed δ=0.10/T=3000, a window the archive already showed yields ~2 events/run, below the seal's own ≥4 floor.
- **v2 (0e7ff22): INSUFFICIENT** — "fixed" to δ=0.05 citing the archive's 10/10 scoring, without checking that the archive's runs were T=10000, not 3000. Rule extracted: **an archive result cited as evidence for a design choice must match that choice's full configuration, not just the headline knob.**
- **v3 (41b51fa): T=10000.** Scored 20/20 first try. Both dead seals stand as graded.

Scope: verdict at δ=0.05, K=3, N=900, cap=1500, house implementation. Untested: other δ (v1's δ=0.10 attempt was unscoreable, not contrary), cap position (one value; a cap sweep would map how far the discharge can be strangled before the rhythm degrades), and Kimi's implementation (one-lineage until their quota wakes).

---
## ADDENDUM (13:4x, referee v2) — the correct timing null: the clock is mostly a construction feature
The v2 referee pass demanded the constant-inflow-plus-threshold baseline before "quasi-periodic clock" could headline. Computed from the v3 control archive (9,094 quiet-phase increments, 85 gaps): inflow-integration noise alone → CV 0.015; + measured crash-size variability (CV 0.089) → independent-renewal baseline **0.091** vs measured **0.070**. So: (a) raw sub-Poisson CV is explained by renewal structure — the referee's "construction feature" reading is CORRECT against the right null; (b) timing noise is crash-size-dominated, not inflow-dominated; (c) residual: measured sits 0.78× below the independent baseline — weak size↔refill compensation, descriptive. The reset-null refutation (discharge-shape invariance) is independent of this and stands. Brief §3.8 rewritten accordingly — the concession is in the shipping artifact, not a side note.

**ADDENDUM 2 (15:0x, referee v3 demand executed):** the reviewer called the 0.78 residual INSUFFICIENT at ~1.0σ and demanded a CI. The test answered BOTH of us wrong-and-right: bootstrap ratio CI [0.62, 0.94] excludes 1 (the compression is real — their INSUFFICIENT call, superseded by their own proposed test), but corr(D_i, T_i) = +0.07 where renewal predicts ~0.9 (my "compensation" story dead — the timing is DECOUPLED from crash size). Neither extreme model fits: timing runs 4.7× above the integration floor yet indifferent to discharge size → dominant noise is a third source (trigger-state variation, open). Coheres with the reset-null's discharge-shape invariance: the clock is set upstream of the crash, full stop. Bootstrap pools 85 gaps across 10 runs, labeled.
