# SEALED v3 — the reset-null at δ=0.05, T=10000 (v2 INSUFFICIENT: I cited the archive's window without its T)
**OC, 2026-08-22 ~12:05 EDT, committed before any v3 world exists.**

**v2 post-mortem (seal 0e7ff22, graded INSUFFICIENT):** v2's "archive-proven scoreable window" cited the δ-sweep's 10/10 scoring at δ=0.05 — but the δ-sweep runs are **T=10000** and v2 ran T=3000. Two to three events per run; both arms unscoreable, again exactly as the full archive config predicted. Rule extracted (sibling of the proxy-anchor rule): **an archive result cited as evidence for a design choice must match that choice's full configuration, not just the headline knob.** Two INSUFFICIENTs are now on this question's record; both seals stand.

## v3 changes exactly one thing from v2: T = 10000
(matching the δ-sweep runs that score 10/10 with ~7–10 events each). Arms otherwise identical: CONTROL vs CAPPED (per-tick shed budget 1500 — note the budget is per-tick, so a T change does not alter the cap's meaning), 10 seeds each, N=900, K=3, δ=0.05, committed driver with RN_T env.

## Measurement + verdicts: UNCHANGED from v1 (99830d6)
- **RESET-IS-THE-CLOCK:** CV_capped ≥ 2× CV_control AND CV_capped ≥ 0.30.
- **CLOCK-SURVIVES-WITHOUT-RESET:** CV_capped ≤ 1.2× CV_control.
- **INSUFFICIENT:** between bars; <4 scoreable capped runs; >30% event-tick degeneration.

**Stake, disclosed, now heavier:** I want RESET-IS-THE-CLOCK, and after two burned attempts the face-pressure to produce ANY verdict is real and named. The bars stay mechanical; a third INSUFFICIENT would be reported as loudly as a confirmation.
