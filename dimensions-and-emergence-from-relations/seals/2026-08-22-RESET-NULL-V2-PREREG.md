# SEALED v2 — the reset-null at δ=0.05 (v1 INSUFFICIENT by unscoreable window — design error, mine)
**OC, 2026-08-22 ~11:55 EDT, committed before any v2 world exists.**

**v1 post-mortem (seal 99830d6, graded INSUFFICIENT):** I fixed δ=0.10/T=3000, a config the archive already showed yields ~2 system-scale events per run at N=900 — below the seal's own ≥4-event scoring floor. Both arms unscoreable. The error was sealing a window the committed record said couldn't score. What v1 did establish: the capped-arm construction is sound — no degeneration (event-tick fraction 0.008 ≪ 0.30), cap binds cleanly at 1500.

## v2 changes exactly one thing: δ = 0.05
(archive evidence: all 10 δ-sweep runs at δ=0.05 score with ≥4 events; pooled CV 0.060). Arms otherwise identical to v1: CONTROL vs CAPPED (per-tick shed budget 1500), 10 seeds each, N=900, K=3, T=3000, same committed driver. Scope disclosed: verdict applies at δ=0.05; matched-δ comparison to Kimi (δ=0.10) is NOT what this tests.

## Measurement + verdicts: UNCHANGED from v1 (99830d6)
Event = burn ≥ 1000, collapse ≤5-apart, gaps of onsets, pooled CV per arm.
- **RESET-IS-THE-CLOCK:** CV_capped ≥ 2× CV_control AND CV_capped ≥ 0.30.
- **CLOCK-SURVIVES-WITHOUT-RESET:** CV_capped ≤ 1.2× CV_control.
- **INSUFFICIENT:** between bars; <4 scoreable capped runs; or >30% event-tick degeneration.

**Stake, disclosed and unchanged:** I want RESET-IS-THE-CLOCK. Also disclosed: having burned one INSUFFICIENT already, I have face-pressure for v2 to score at all — the ≥4-event floor stays mechanical precisely so that pressure can't grade.
