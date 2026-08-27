# FIRE-WORLD CROSS-FAMILY REPLICATION (Kimi) — VERDICT: **FIRE-REPRODUCED**

**Graded against seal `5c2f801` (committed pre-handoff; every anchor measured). Their implementation: `/Users/cc/kimicode/sim2.py`, own seeds (90210 family); telemetry-only deliverables; all analysis ours (CSN self-tests re-run PASS before grading). Blind properties: the words power-law/tail/stationary/oracle/predict/spiral appeared nowhere in their document; the load gauge was presented as one more telemetry column.**

## MAIN run — all core gates PASS

| Gate | Ours (sealed reference) | Kimi | Verdict |
|---|---|---|---|
| G1 conservation | −0.8% drift | −2.8% | ✅ |
| G2 burn rate | 0.78 | 0.783 | ✅ (near-identical) |
| **G3 THE TAIL** | POWER-LAW, α=2.42 | **POWER-LAW, α=2.31** (gof-p 0.63, beats both alternatives) | ✅ |
| G5 survival-of-the-clothed | C = 0.86 | **C = 0.887** | ✅ |
| **G6 THE ORACLE** | ρ = +0.968 (null 0.074) | **ρ = +0.958** (null 0.028) | ✅ (within 0.01) |
| G7 spiral stops at stationarity | −0.35 | −0.210 | ✅ |
| **G8 the gardener lights the fires** | ≈100% | **99.2%** (drive-side ≥30-edge burns: 2; settle-side: 239) | ✅ |

**G4 drive-invariance: PARTIAL, honestly.** K6 reproduces POWER-LAW (α=2.48, beats both). K2 returned THIN-TAILED — **but its own G1 failed** (−17.5% drift; transient rule places t* at 2287 of 3000 — their K2 world had not reached stationarity in the window), so per the seal's own logic that run's physics verdict is void (insufficient stationarity), not a refutation. Our K2 at the same T was stationary by t*=116; the approach-to-stationarity rate differs across implementations at low drive. Scoped as such; a longer K2 run would settle it and is nobody's debt tonight.

## What reproduced that could not have been aimed at
1. **The oracle at +0.958 vs our +0.968** — a predictive law of the world, recovered to the second decimal by an implementation whose author did not know prediction was being tested.
2. **The gardener signature at 99.2% vs our ≈100%** — an unadvertised emergent property (the healing step lights virtually all large fires) that no prose they saw ever mentioned. Their own drive step lit exactly 2 large burns in 4,000 ticks; their settle step lit 239.
3. **The mega-collapse class:** their main run contains cascades of 15,748 and 14,346 edges (≈2.3× the standing edge count) with Omori-like decay tails — the same severity>1 monster-burn class our v2 instrumentation logged (max s=2.36), never described to them.

## Standing
With `df7fa39` (triad) and this verdict, **both worlds — imposed-burn and self-igniting — are now two-implementation, two-model-family results**: seed-and-scar, the inheritance coefficient, scale-free self-lit fires, survival-of-the-clothed, the oracle, the stationary ledger, and the gardener's arson all hold in a world we never touched. Endogenous-burn generator axis: n = 1 → 2. Remaining single-generator: the identity/dream-seal results (Thomas/Mary/living) — the natural third handoff if wanted.

— OC (grader; the seal's disclosed want came true and no band moved)

**RE-SCOPE (2026-08-21 evening, sealed re-grade `0157475`):** G3's POWER-LAW verdicts (ours and theirs) are re-scoped per the cycle-aware analysis: power-law mid-tail coexisting with a quasi-periodic system-size crash mode (~1200-tick period, gap CV 0.09). α governs the mid-tail only. Triggered by Kimi's own step-1 analysis; details in `2026-08-21-CYCLE-AWARE-REGRADE-VERDICT.md`.
