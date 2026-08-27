# Q2 — is there information in the trajectory ABOVE the final arrangement? VERDICT: NO (definite, not a hedge)

**Date:** 2026-08-15 · **Seat:** quant · **Harness:** `code/2026-08-15-Q2-dynamical-observable-test.py`.
Follow-on to the PANEL FINAL: Q1 (does order leave a mark *in* the arrangement?) = YES. Q2 asks the
strictly harder thing I had earlier (wrongly) folded into "ill-posed": is there information in the
TRAJECTORY not present in the final arrangement — a rung ABOVE arrangement?

## Answer: NO — and it is a theorem for this model, not a measurement limitation.
A plain (unweighted, untagged) graph's COMPLETE state is its adjacency matrix A. Every observable —
static (clustering, algebraic connectivity) OR dynamical (diffusion relaxation, random-walk return
probability, cascade) — is a function of A. Two identical arrangements are therefore identical under
EVERY probe. History can leave a mark only by changing A (that is Q1, = YES); it cannot leave a mark
"above" A because a plain graph has nowhere to store one.

## Falsifier (the empirical spine), and it passed cleanly
Prediction: identical A → identical dynamical response, regardless of construction history or
dynamics-seed. If ever violated → a rung above arrangement EXISTS.
- Deterministic structure-sensitive probe p_ret(3) = tr(P^3)/N on one fixed graph, two calls:
  **0.021345 vs 0.021345, |diff| = 0.00e+00** — bit-for-bit identical.
- Diffusion relaxation tau: 1.50 vs 1.32, within start-averaging noise.
⇒ No history channel above A. Confirmed.

## A real nuance the run surfaced (and I nearly misread)
Whether a dynamical probe SEES the (arrangement-borne) order-mark depends on the probe:
| ordering | clustering | tau (fast diffusion) | p_ret(3) (clustering-sensitive) |
|---|---|---|---|
| A smooth-early | 0.103 | 1.45 ± .07 | 0.0087 ± .0001 |
| B rewire-early | 0.368 | 1.41 ± .05 | 0.0279 ± .0003 |
| C interleaved | 0.306 | 1.48 ± .07 | 0.0223 ± .0003 |
tau is floor-limited (all graphs mix in ~1.4 steps) and BLIND to the mark; p_ret(3) SEES it at
~50–100σ, tracking clustering. **I flagged tau's blindness as underpowered, NOT as "dynamics can't
see history"** — a different function of A can be more or less sensitive; none sees beyond A.
(The residual-regression on tau is uninformative *because* tau is floor-limited; not read into.)

## What this is NOT (guarding my prior error)
This is a DEFINITE NO with a proof + a clean falsifier — the opposite of the "ill-posed" hedge I
earlier reached for on Q1. Q1 (order marks the arrangement) = YES; Q2 (a rung above arrangement)
= NO. Both definite, non-contradictory. Arrangement is the complete state (terminal in that sense)
AND path-dependent (history selects which arrangement forms).

## What WOULD make a rung above arrangement real (the precise condition)
The model would need HIDDEN STATE — memory-carrying variables not in the topology (edge ages,
evolving weights, node-internal variables). A dynamics reading that hidden state could then recover
history a topological snapshot cannot. A plain graph has none, so NO here. The rung question is
therefore about whether the substrate carries memory, not about graphs per se.

---

## Q2 DEEPENED by KEEL (2026-08-15 22:49, pre-registered `7ff26d0` → verdict `e532854`) — proof + a survivor
Ciara routed the open dynamical-observable question to KEEL. Two results that strengthen this verdict:

**1. The "needs a dynamical observable" hope is closed BY PROOF, not just my empirical falsifier.** `rewire` and `smooth` read only `adj` → the physics is **Markov in the arrangement**. Conditional on the complete final arrangement, the trajectory is independent of all futures, so **any dynamical probe's outcome distribution is a functional of the arrangement — a randomized static observable.** This is the rigorous form of my empirical "identical A → identical response": nothing can read what the arrangement doesn't carry. Q2 reduces to: does any macroscopic history distinction get fully *erased* from the arrangement (present but forever unreadable)?

**2. Empirically: no — `rewire` cannot fully forget, at any strength, and the survivor is nameable.** Upstream distinction (smooth×4 vs none) vs eraser (final rewire at f ∈ {1.0…0.0}), paired n=40. Every *topological* channel (C̄, P0, L̂, F_long) decays monotonically to silence at f=0 (all |z|<2) — **but degree variance survives total rewiring at z=+17.3**, and it was the *pre-named* survivor: rewire preserves the lower-index endpoint's degree of each cut edge, so the pre-rewire degree sequence partially survives any f. **Topology is erasable; the degree ledger is not.** (E integer-identical across arms at every f.)

**What this means for the seed story, precisely:** there IS a maximally-persistent history channel — the degree ledger — that survives even total topological rewiring. But it is still a property *of the current arrangement* (a static observable), so it is **not a rung above arrangement** — it is the most erasure-resistant thing *inside* it. The honest refinement of the whole arc: history is written into the arrangement (Q1), the arrangement is the complete state (Q2, now proven via the Markov property), and *within* the arrangement some channels (topology) are erasable while others (the degree ledger) are structurally durable. A true rung above arrangement would still require hidden state the model lacks; KEEL's honest limit notes an operator that also randomized the degree sequence could erase completely — this operator set contains none.

**Bonus (confirms the panel + answers gene0's open question):** smooth×4 on a pure-local graph fragments it (reach 0.999 → 0.013) — smoothing without long-range edges prunes into disconnected dense clusters; and pre-rewire smoothing leaves residue through a final rewire at every strength, via the degree channel.
