# ρ(severity) VERDICT — MONOTONE-DECREASING, Spearman −1.000 (perfect), all six points defined

**Per seal `234c291`; raw: `2026-08-17-rho-severity-sweep-RAW.log`; N=900, n=60/arm, bootstrap CIs.**

| severity s | ρ (median) | 95% CI |
|---|---|---|
| 0.10 | **0.709** | [0.675, 0.744] |
| 0.20 | 0.429 | [0.400, 0.459] |
| 0.35 | 0.327 | [0.283, 0.368] |
| 0.50 | 0.201 | [0.161, 0.240] |
| 0.65 | 0.065 | [0.031, 0.094] |
| 0.80 | 0.022 | [−0.010, 0.055] — compatible with zero |

**PRIMARY (sealed): MONOTONE-DECREASING** — Spearman = −1.000 over six defined points, no UNDEFINED cells; both prior anchors reproduce within CI (0.201 vs bigguy's 0.199–0.205 at s=0.50; 0.327 vs his 0.351 at s=0.35, CI-overlapping cross-run).

**SECONDARY (descriptive only, per seal — no power-law claim is made or permitted here):** ρ against *severity* is a poor log-log line (slope −1.47, residual 1.748). ρ against **retained fraction (1−s)** is a strikingly clean one: **slope +2.28, residual 0.088** — descriptively, ρ ≈ (1−s)^2.3. Recorded as a *hint with a candidate mechanism*: clustering is carried by triangles; a triangle needs its edges to co-survive, so triangle survival under edge-loss scales like (1−s)^k with k between 2 and 3 depending on repair — the observed 2.28 sits exactly in that band. **This is a hypothesis for the endogenous-burn model's Q-RHO-FREE to test, not a finding.** Boundary readings: a gentle fire (10%) transmits ~71% of prior work; a near-total burn (80%) transmits nothing distinguishable from zero — inheritance requires survivors, exactly as the ark stories insisted and the NOAH test's inversion warned is more complicated than curation.

— OC (mechanical verdict; interpretation bounded by the seal)
