# SEALED — Mediator ablation 1: does the recovery advantage survive destruction of everything except the degree sequence?
**OC, 2026-08-23 ~15:40, committed before any ablation world exists. Demanded by external adversarial read #3 (their "decisive control" table, row 1): §3.4's causal claim — triangle-embedded residue POWERS the B>A recovery advantage — is association, not decomposition, until an intervention selectively removes the candidate mediator.**

## Design (N=900, f=0.65, n=30/arm, fresh seed block 500000+, disjoint from all prior)
Intervention point: post-shock, pre-recovery. Arms:
- **A** = rewire(rgg, 0.65) → grow_prune (standard cold build).
- **A-sw** = rewire(rgg, 0.65) → **full degree-preserving randomization** (10×E double-edge swaps, uniform pairs, reject self/multi-edges) → grow_prune.
- **B** = establish (rewire 1.0 + grow_prune) → rewire(0.65) → grow_prune (standard history arm).
- **B-sw** = establish → rewire(0.65) → **same swap protocol** → grow_prune.
Swaps preserve the degree sequence EXACTLY and destroy triangles, specific edge identities, and spatial remnants together — disclosed: this tests "degree state alone vs everything-else-history-left"; separating triangle-count from edge-identity is ablation 2, future. Outcome: final mean local clustering (deg≥2 definition). adv = C(B)−C(A); adv_sw = C(B-sw)−C(A-sw).

## Verdicts (mechanical)
- SANITY: adv ≥ 2×SEM_adv, else INSUFFICIENT (the effect must exist before its mediator can be tested).
- **MEDIATED** (triangle/identity residue is the carrier): adv_sw ≤ 0.35×adv.
- **NOT-MEDIATED** (degree sequence alone suffices — §3.4's story dies, reported loudly): adv_sw ≥ 0.65×adv AND adv_sw ≥ 2×SEM.
- **PARTIAL/INSUFFICIENT**: between, or sanity fails.

**Stake, disclosed: the triangle-mediation story is OURS (§3.4, blind-replicated as association) — we want MEDIATED. The referee suspects the joint unmeasured state. Bars fixed before any swap world exists.**
