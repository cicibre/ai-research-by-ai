# Primitive test — the relational-closure model on the honest ruler

**Date:** 2026-08-11 · **Author:** QUANT · **Requested by:** Ciara (re-derive the ChatGPT-room "dimensional phase transition" numbers on the spectral ruler, not ball-growth). Harness: `2026-08-11-primitive-test-harness.py` (numpy 2.5.2 / scipy 1.18 / nx 3.6, python 3.14). Sibling to `2026-08-10-dimensionality-from-relations-adversarial-study.md`.

## The ask
A parallel ChatGPT thread ran a β-sweep on a relational-closure model (s∈{−1,+1}, W updated by pairwise ± reinforcement + closure W@W) and reported effective dimensions D≈1.28–2.77 off a **neighbourhood/ball-growth** estimator — the exact estimator the 08-10 study proved stamps D≈3.4 "clean scaling" on a coordinate-free random graph. Re-measure on the spectral ruler + N-companion + degree-matched null.

## Pre-registered prediction (on the wall before the run)
A non-local closure substrate has no geometric majority to define "local" against → honest d_s should **diverge** (climb with N; no flat plateau) and sit **indistinguishable from a degree-matched null**. Falsifier: a stable finite d_s, flat across N, distinct from null.

## Ruler validation (known answers, measured identically)
| graph | d_s | expect |
|---|---|---|
| 1D ring N=800 | 1.00 | ~1 ✓ |
| 2D torus 28² | 2.08 | ~2 ✓ |
| 3D torus 9³ | 3.46 | ~3 (finite-size biased high) ✓ |
| ER random ⟨k⟩=6 | 3.63 | high / no finite geometry ✓ |

The 2D torus stays **flat across N** (2.13→2.08→2.05 at N=400/800/1600) — that is what real geometry looks like on this ruler, and the reference every model row is compared against.

## Result
Two reconstructions of the **truncated** paste tail (the thresholding/return step was cut off), both measured with the N-companion + each with its own degree-matched null:

| N | 2D-torus | **A** d_s | A climb | A null | A ⟨k⟩ | **B** d_s | B null | B ⟨k⟩ |
|---|---|---|---|---|---|---|---|---|
| 400 | 2.13 | 2.83 | +1.0 | 2.98 | 185 | 3.42 | 3.59 | 12 |
| 800 | 2.08 | 2.85 | +1.0 | 2.97 | 373 | 0.42 | 3.67 | 12 |
| 1600 | 2.05 | 3.56 | +2.1 | 3.00 | 474 | 5.62 | 3.68 | 12 |

- **A = global density-threshold tail (my reconstruction).** Clean: d_s **climbs with N** (2.83→3.56) *and* within each graph (d_s(t) slope +1.0→+2.1), and is **indistinguishable from its degree-matched null** (2.98/2.97/3.00). No geometry beyond the degree sequence. NB ⟨k⟩≈185–474 → a near-complete **dense blob**; that density is what a ball-growth estimator misreads as "dimension."
- **B = per-node top-k tail (Ciara's stated rule "each node retains its strongest k relationships").** Connected (100%, one component) but sparse (⟨k⟩≈12). The spectral estimate is **unstable across N** (3.42/0.42/5.62) — the 0.42 is a window artifact (tiny spectral gap → t-window overruns into saturation). No flat-convergent plateau; **under-measured, not a clean read**. It does *not* show the torus's flat signature.

## Verdict
**Prediction holds, robustly for A, provisionally for B.** On the honest ruler neither reconstruction reproduces finite geometry. The ChatGPT-room D≈1.5–2.8 is the **ball-growth estimator reading degree/density structure** of a dense (A) or sparse-but-non-geometric (B) graph — not emergent dimension. Same disease, same cure as 08-10.

## Airtight vs contingent (kept separate)
- **Airtight (independent of my reconstruction):** the ruler reads 1/2/3 on lattices and holds the torus flat across N; the pasted model **numerically overflows within ≤60 steps** (W@W compounds) — this *is* the "saturation" the ChatGPT thread reported; a degree-matched null is the correct control (both rooms proposed it).
- **Contingent (rides on reconstruction):** every specific d_s value; the "dense blob ⟨k⟩≈185" (← my *global* density-0.04 threshold, not necessarily her per-node rule); the A-vs-B split. Two flagged reconstructions I added and cannot attribute to her model: (1) a **RECON-STABILIZER** rescaling W's magnitude each step (the real stabilizer is likely in the truncated tail); (2) the **thresholding tail** itself (A global, B per-node).

## What would make it airtight for HER model
Her actual truncated tail (thresholding + real stabilizer) — then run that exact model through this harness. The conclusion is already robust across two plausible tails for the "no flat plateau" claim; B needs a fixed t-window + seed-averaging to characterize cleanly. **Burden now sits on producing a stable flat d_s plateau — neither reconstruction did.**

Sibling lesson: [[shared-code-certifies-the-function-not-the-inputs]] — I certified the *ruler* on known lattices; the *model* is reconstructed, so its numbers are contingent until her tail lands. [[re-derive-against-the-referent-system]] — real code can be the wrong code; I won't call a guessed model a re-derivation of hers.

— quant 🔎 ⚖️ 🧪
