# Rung-4 (trajectory vs arrangement) — SYNTHESIS after blind review: the question was ill-posed for the measurement

> **⚠️ SUPERSEDED 2026-08-15 by the blind PANEL (gene0 + keel) — read `…-PANEL-FINAL-order-leaves-a-mark-YES…md`.**
> Two independent seats, blind, using clustering (not d_s), returned YES-with-direction at 200σ+, density-pinned.
> This file's 'ill-posed' verdict was WRONG: it moved the goalpost from the posed question (does order leave a
> mark? — YES) to a harder one (a mark BEYOND the arrangement?) and called the whole thing unanswerable. The
> posed question is cleanly YES. Only the Q2 point (info strictly above arrangement needs a dynamical observable)
> survives, as a SEPARATE untested question. See the panel final.


**Date:** 2026-08-15 · **Seat:** quant · **Supersedes the verdicts in** both `…-VERDICT-insufficient-power-leaning-real.md` (confounded) **and** `…-CONTROLLED-VERDICT-memory-refuted-annealing-artifact.md` (mislabeled). **Prompted by Ciara:** "hand it to someone blind, attention-to-detail heavy — the observer affects the experiment." **Blind reviewer:** a fresh agent given neutral A/B/C protocols, the bare question, and no access to any prior conclusion; it generated its own data.

## What the blind review did
Independently — never seeing my numbers or verdict — the reviewer:
- reached the **same fair comparison** I used (B vs C: matched on operation count, differing only in the *order* of a smoothing pass relative to the drop to fraction f). The design is not my bias.
- reproduced the **same raw phenomenon**: B (smoothing before the drop) ends up **less geometric** than C (both after) — same sign, 5–7σ across all (N,f) cells, 18σ paired at N=900/f=0.6, and it survives matching realized locality (+0.170, 7.8σ).
- added mechanism I did not have: `grow_prune` preferentially destroys long-range (zero-overlap) edges; before the drop there are none to destroy, so a pre-drop smoothing pass is ~80% wasted for geometry. Two-effect additive law: β_pre = −0.079/pass, β_post = −0.411/pass.

## The finding is the DISAGREEMENT, not either verdict
From **identical numbers**, the reviewer labeled it **"YES — history/order leaves a mark"** and I had labeled it **"memory refuted."** Two careful observers, same data, opposite top-line verdicts. That is the signature of an **ill-posed measurement**, and it is exactly what a blind second observer exists to surface.

## Why the measurement cannot answer the question (the load-bearing logic)
d_s is the heat-kernel return probability of the **current adjacency matrix** — a pure function of the current arrangement, with zero dependence on history except through current wiring. Therefore:
- Two graphs with different d_s **have different arrangements**, by definition of d_s.
- To see any "history effect" in d_s you must change the arrangement (B and C differ in d_s ⇒ differ in arrangement). Hold the arrangement fixed ⇒ d_s fixed ⇒ no history effect, trivially.

⇒ **A static structural observable like d_s can NEVER distinguish "trajectory as information above arrangement" from "a different history selected a different arrangement."** The rung-4 question — is there information in the *path* not reducible to the resulting *configuration*? — requires a **dynamical / response observable** (e.g. response to a future perturbation), not a snapshot geometry. My d_s-hysteresis design was categorically unable to detect what it was built to detect.

## What is actually, solidly true (all three, non-contradictory)
1. **Operations don't commute — order selects which arrangement forms** (path-dependence *of* the arrangement). The endpoint (N, f, processing-amount) does **not** determine the arrangement. Blind-confirmed, 18σ. [the reviewer's "YES"]
2. **The "establishing geometry first protects it" story (the seed-defends reading) is refuted in direction:** established-first (B) ends up *less* geometric, not more. Both observers agree on the sign. [my "refuted", kept only as a directional claim]
3. **Neither (1) nor (2) establishes a rung ABOVE arrangement**, because the observable used can't see one. Arrangement remains sufficient for every static observable measured; history's role here is to *select* the arrangement, not to add information on top of it.

## Corrections to the record
- My "leaning-real" (leaning toward trajectory-rung) was reading a confounded (annealing-count-unmatched) comparison. Wrong.
- My "REFUTED / memory is an artifact" over-claimed: it correctly killed the seed-*defends* direction but mislabeled the whole thing "no memory," when the honest statement is "this measurement cannot address memory-above-arrangement at all."
- The seed metaphor's *physics anchor* ("the past leaves a protective mark") stays dead; but "arrangement is terminal" was **not** proven either — it was untestable here.

## To actually test rung-4 (owed, if ever pursued)
Need an observable a fixed arrangement does NOT determine: e.g. hold two graphs at *identical* current arrangement (or perturb one and one with different construction histories) and measure a *dynamical response* — relaxation time, avalanche size under load, recovery after edge removal. Static geometry is the wrong instrument, full stop.

## The meta-lesson (the real prize)
Ciara's instinct was exactly right: the blind second observer didn't confirm or overturn my verdict — it revealed that *my verdict was one verbal frame on a question the instrument couldn't resolve.* The observer affected the experiment; two observers exposed that the experiment couldn't answer the question. Credit to the blind reviewer for the mechanism (β_pre/β_post, the long-range-edge-destruction account) and for reaching the fair comparison independently.
