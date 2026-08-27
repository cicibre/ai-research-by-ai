# SEALED GRADING — fire-world (endogenous burns) cross-family replication by Kimi

**OC, 2026-08-21 ~16:05 EDT, committed BEFORE the handoff is sent. Never shown to the implementer. All analysis (transient rule, tail grading, correlations) is computed by US from their raw telemetry with the existing self-tested graders — they only implement the world and log series; no formula, expected shape, or direction appears in their document. Reference values from committed runs (`results/endogenous-burns/`, `2026-08-19-endogenous-burns-VERDICTS.md`, `2026-08-20-dream-seals-RAW.log`). Anchor rule from the last seal's amendment, obeyed this time: every reference below is a MEASURED value from committed raw data, not a proxy.**

**Runs requested:** MAIN (f0=0.65, K=3, T=4000) + K2 (K=2, T=3000) + K6 (K=6, T=3000). Transient computed by our sealed rule (first passage of 100-tick running-mean burn rate into ±10% of last-third mean).

## Gates (ours measured → their PASS band)
- **G1 conservation:** last-third edge drift — ours −0.8%; band **|drift| ≤ 10%**.
- **G2 burn rate (MAIN):** ours 0.78 burns/tick; band **0.50–0.95**.
- **G3 THE TAIL (primary):** our CSN grader (self-tests re-run first) on their post-transient MAIN burns. Ours: POWER-LAW (α=2.42, gof-p 0.99, beats both alternatives). **TAIL-REPRODUCED** = verdict class POWER-LAW; **PARTIAL** = HEAVY-TAILED-NOT-PL; **NOT** = THIN-TAILED. α reported with drive-dependence caveat, banded only loosely [1.5, 3.5] (informational, not pass/fail — our own α moves 1.76–2.42 with K).
- **G4 drive-invariance:** verdict class stable across K2/K6 (ours: POWER-LAW at both).
- **G5 survival-of-the-clothed:** their stationary mean C (last-third of C samples, MAIN) — ours 0.86; band **0.74–0.95** (their establish-C ran 0.705 vs our 0.712; band widened accordingly).
- **G6 the oracle:** Spearman(load gauge, next-10-tick burn total), post-transient, our computation, their series — ours **+0.968** vs shuffled-null 95th of +0.074. **ORACLE-REPRODUCED** if ≥ **+0.50** and above their own shuffled null (200 shuffles, our code).
- **G7 stationary ledger (the spiral stops):** Spearman(k_sd samples, cumulative burns), post-transient — ours **−0.35**. Band: **< +0.50** (i.e., no monotone tree-ring climb at stationarity).
- **G8 the gardener lights the fires (the unadvertised signature):** fraction of burns ≥30 edges occurring in the POST-SETTLE cascade of the tick — ours ≈100% (the drive-side count at that threshold was 0 in 2,700 instrumented ticks). Band: **≥ 80%**. This is the fragmentation-asymmetry-class test: an emergent property never stated in any prose they could see.

## Verdicts
- **FIRE-REPRODUCED:** G1, G2, G3=POWER-LAW, G5, G6, G8 all pass (G4, G7 reported; failures there scope, not sink).
- **PARTIAL:** G3=HEAVY-TAILED or one of G5/G6/G8 out of band — named per-gate, the rest stands.
- **NOT REPRODUCED:** G3=THIN or ≥3 core gates fail — reported as loudly as a confirmation; the endogenous results would then be scoped to our implementation.
- **SPEC-AMBIGUOUS:** G1 or G2 fail → stop, fix prose, re-run gates.

**Stake:** I want FIRE-REPRODUCED. Bands measured-and-fixed before their run exists; they cannot move. Clarifying answers route via Ciara and are appended here, dated.
