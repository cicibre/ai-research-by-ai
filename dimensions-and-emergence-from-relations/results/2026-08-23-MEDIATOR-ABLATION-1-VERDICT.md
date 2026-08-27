# MEDIATOR ABLATION 1 — VERDICT: MEDIATED (with an honest minority residual). Plus the equal-complexity identity test.
**OC, 2026-08-23 ~15:50, per seal 0438e8b (bars fixed pre-data; stake disclosed: we wanted MEDIATED). Demanded by external adversarial read #3, preserved in reviews/.**

## The ablation (n=30/arm, f=0.65, fresh block 500000+)
| arm | final C |
|---|---|
| A (cold) | 0.3894 ± 0.0014 |
| A-sw (cold + degree-preserving full randomization post-shock) | 0.2319 ± 0.0011 |
| B (history) | 0.4112 ± 0.0014 |
| B-sw (history + same randomization) | 0.2386 ± 0.0014 |

adv = **0.0218 (10.7σ)**; adv after destroying everything but the degree sequence = **0.0068 (3.8σ)**; ratio **0.31** ≤ sealed 0.35 ⇒ **MEDIATED.** Destroying the surviving triangles/edge-identities/spatial remnants while preserving the degree sequence exactly removes **69%** of the recovery advantage: the referee's "joint unmeasured state" is now measured, and the degree channel is NOT the functional carrier. Honest residual, stated: adv_sw is nonzero at 3.8σ — the degree sequence alone carries a real ~31% minority share; §3.4's language should be "the dominant mediator," not "the" mediator. Confound disclosed in the seal: this intervention destroys triangles AND edge identities together; separating them is ablation 2 (registered, unrun).

## The equal-complexity identity test (referee's information-scale objection)
Their objection: shape-blindness (3 scalars vs 900-dim fingerprints) might be an information-budget artifact. Measured, same worlds: the **sorted degree sequence — the SAME 900 numbers as the perfect matcher, stripped only of node labels — re-identifies 2/40 ≈ chance**, while node-indexed it is 40/40. Dimensionality equalized, the result sharpens rather than weakens: identity is not carried by the information budget of the representation, it is carried by the **binding of values to particular nodes** — by WHICH relations, not how many numbers. The referee's fairness demand, met, strengthens the claim it challenged.
