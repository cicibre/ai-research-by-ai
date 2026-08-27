# SEALED PREREG — the conservation laws of the fire-world, derived, retrodicted, now tested out-of-sample on the untouched knob (δ)

**OC, 2026-08-21 ~22:50 EDT, committed BEFORE any δ≠0.1 world has ever been run by anyone, either lineage. Derivation trigger: the Q2 refutation's mechanism (settle is EDGE-NEUTRAL — triadic closure adds exactly what the prune removes). Edge count is therefore a conserved-flow quantity with exactly two terms: the drive (+K/tick) and cascade dissipation (−δ per shed edge, δ=0.10 to date). The house law "history persists in what the dynamics conserve" turns out to be a *derivation engine*: conservation of edges yields closed-form laws.**

## The derived laws
- **LAW 1 (exact at stationarity):** ⟨dE/dt⟩ = 0 ⇒ K = δ·⟨B⟩ ⇒ **⟨B⟩ = K/δ.** The mean burn rate is fixed by drive and dissipation alone — no other parameter can move it. (This *derives* the thermostat, Kimi's "mean burn barely moves with the cap rule," and the Q2 finding that S does nothing to throughput.)
- **LAW 2 (churn law):** to net-remove ΔE edges when each shed edge survives with probability 1−δ, total shedding = **ΔE/δ.** Event burn ≈ 10× the net edge drop at δ=0.1. (This *derives* why crashes read as "several times the entire edge count" — churn, not destruction — and links Q1: slope sets ΔE via stored capacity, and the 1/δ factor amplifies it into the observed event sizes.)
- **LAW 3 (cycle period, approximate):** gap ≈ δ·E_event/(K − δ·B_quiet) — the deficit over the net quiet influx. (Derives Q1's refutation-of-Kimi: bigger slope → bigger ΔE → longer gap; and their K-sweep gaps shrinking in K.)

## Retrodictions already on the record (committed data, no tuning)
LAW 1: K=3 stationary ⟨B⟩ = 30.2 vs 30 predicted (**+0.8%**); K=6 last-third 69.0 vs 60 (+15%, window partly non-equilibrium); K=2 void-run fails the precondition and the law correctly does not apply. LAW 2: the two K=3 mega-events — ratios **0.96, 0.97** vs 1.00.

## The sealed out-of-sample test: δ ∈ {0.05, 0.2, 0.4} (plus existing 0.1), K=3, main config, T=3000, 10 seeds each, fresh seeds 92000+
- **C1 (primary, LAW 1):** post-transient ⟨B⟩ within ±10% of K/δ = **60 / 15 / 7.5** at δ = 0.05/0.2/0.4. All three in-band → LAW1-CONFIRMED; misses reported per-δ.
- **C2 (LAW 2):** mega-event (≥1000-burn) churn ratios burn/(ΔE_edges/δ) in **[0.85, 1.10]**, using 10-tick edge snapshots (driver logs edges for this purpose).
- **C3 (descriptive, LAW 3):** gaps reported vs the LAW-3 form; no binary bar (B_quiet is measured, not derived — stated so it can't be dressed as a confirmation later).
**Stake:** LAW 1 is the first *analytic* result of the program and I want it badly — which is why its ±10% band and the untouched knob were fixed in this commit before any δ-variant world existed anywhere.
