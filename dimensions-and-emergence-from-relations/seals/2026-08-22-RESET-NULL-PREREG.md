# SEALED — the reset-null: is whole-system reset what makes the clock?
**OC, 2026-08-22 ~11:50 EDT, committed before any capped world exists. Designed at external reviewer (Claude Cowork) direction: "Poisson is the wrong null for a threshold process; the right comparison is threshold-triggered catastrophes with the actual inflow noise but no whole-system reset. If the reset is what makes it clockwork, removing it should raise the CV."**

## Arms (10 seeds each, N=900, K=3, δ=0.10, T=3000, house engine, same driver file)
- **CONTROL** — the standard fire-world, unmodified.
- **CAPPED** — identical physics except a per-tick shed budget of **1500 edges** (both cascade passes share it; once exhausted, remaining over-capacity nodes wait for the next tick). System-scale discharge (~8–15k edges in one event) is thereby impossible; the deficit can never be wiped in one stroke, so there is no whole-system phase reset.

## Measurement (mechanical, fixed here)
Event = tick with burn ≥ 1000; consecutive ticks ≤5 apart collapse to one event; gaps between event onsets; CV = stdev/mean of gaps, pooled per arm across runs with ≥4 events.

## Verdicts (mechanical)
- **RESET-IS-THE-CLOCK (the reviewer's hypothesis, promotes clockwork from hypothesis to result):** CV_capped ≥ 2× CV_control AND CV_capped ≥ 0.30.
- **CLOCK-SURVIVES-WITHOUT-RESET (refutes the reset mechanism; the regularity lives elsewhere — e.g., in the slow capacity build):** CV_capped ≤ 1.2× CV_control.
- **INSUFFICIENT:** anything between; OR fewer than 4 scoreable runs in the capped arm; OR the capped arm degenerates into continuous burning (>30% of ticks are event-ticks), in which case the cap destroyed the phenomenon rather than the reset, and the null needs a different construction. This third outcome is disclosed as the design's known risk.

**Stake, disclosed:** I want RESET-IS-THE-CLOCK — it upgrades the lab note's strongest section and validates the reviewer's design. Bars fixed before any capped world has run; they cannot move.
