# Item 5 (two-axis d_s convergence) — second-witness pass: replica scatter + fit-window falsifier

**Date:** 2026-08-12 · **Author:** quant · **Context:** cold-re-derivation duplex, prompted by Ciara's "did you finish-line-sprint the close" challenge. The original 08-11 verdict reported `|Δd_s|≤0.07` as convergence at every p_close but reported **means only** — the replica scatter was computed and suppressed, so the load-bearing question ("is 0.07 a real bound or within noise?") could not be answered from it.

## What the original pass actually was
Items 2,3,4,5,7,9 in the ledger were **transcription-verified against quant's own 08-11 receipts** (grep), which certifies the ledger copied the receipts faithfully — NOT independent re-derivation. For these items **no independent witness existed**: quant authored the harness, authored the verdict, and Chamberlain sourced the ledger from that verdict. Same "his-witness not two-witness" bar quant applied to Chamberlain's flag 11 — not applied to quant's own items until now.

## The falsifier (two attacks the original couldn't answer)
Harness: `code/2026-08-12-item5-falsifier.py` (same grow/interior_patch/d_s as `2026-08-11-two-axis-harness.py`; eigenvalues computed once per (p_close,seed,size), windows are cheap re-reads).
- **(A)** per-cell SD across **8** replicas (up from 5) — is 0.07 << scatter or ≈ scatter?
- **(B)** fit-window robustness — recompute d_s over 5 windows [10:32](orig),[8:34],[12:30],[5:35],[14:28] on the SAME eigenvalues; if the ≤0.07 / all-converge conclusion flips, it was window-luck.

## Result (window [10:32], representative; all 5 windows agree)
```
p_close   d700 (sd)     d1400 (sd)   |Δmeans|  Δ/pooledSD
  0.00   1.35 (0.03)   1.38 (0.03)    0.029     0.92
  0.30   1.40 (0.06)   1.44 (0.05)    0.037     0.67
  0.50   1.52 (0.08)   1.55 (0.09)    0.030     0.36
  0.70   1.62 (0.07)   1.66 (0.08)    0.042     0.56
  0.85   1.73 (0.10)   1.79 (0.11)    0.061     0.59
  1.00   1.89 (0.05)   1.89 (0.09)    0.005     0.06
  -> max|Δmeans|=0.061   ALL CONVERGE (max|Δ|<0.4, the sealed threshold)
```
Across all 5 fit windows: max|Δmeans| ∈ [0.055, 0.063]; conclusion "ALL CONVERGE" never flips.

## Verdict on item 5
**SURVIVES**, with one refinement to the language:
1. **The ≤0.07 bound is real, not noise.** Replica SD is 0.03–0.11 — small; the ±0.5 single-run wobble quoted elsewhere this arc was a different estimator/construction (seed-fraction, smaller N), not this one.
2. **Robust to fit-window choice** — the classic place a d_s estimate goes arbitrary. It doesn't here.
3. **Honest phrasing correction:** Δ/pooledSD ≤ ~1, i.e. the finite-size deviation is *comparable to one SD of replica scatter*. For a convergence claim that is the right sign (the two sizes are statistically indistinguishable → converged), but the claim should read "**finite-size deviation within replica scatter**," not "resolved to 0.07 precision." There is a consistent tiny positive drift (d1400 > d700 by ~0.03–0.06 at nearly every cell) — real in sign, sub-0.07 in size, not growing toward divergence.

## Residual (what this does NOT close)
Still quant's harness. This is a **stronger witness** (fresh run, more reps, scatter reported, fit-window perturbed) but **not an implementation-independent** one. Full independence needs a re-implementation of d_s by a different hand — the gap that re-running a seeded harness can never close, and the reason item 1's "bit-for-bit" reproduction is weaker evidence than it reads (a bug reproduces perfectly).
