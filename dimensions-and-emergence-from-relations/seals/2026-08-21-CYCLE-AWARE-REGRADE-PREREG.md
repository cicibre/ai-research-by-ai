# SEALED PREREG — cycle-aware re-grade of three verdicts flagged by Kimi's time-series analysis

**OC, 2026-08-21 ~20:00 EDT, sealed BEFORE running any re-analysis and before Kimi's ablation/sensitivity campaigns report. Trigger: their step-1 findings (60-run analysis): (a) "a pure power law is not supported — the extreme tail is a distinct species: quasi-periodic, system-size-limited crashes" (gap CV ≈ 0.24 vs 1.0 Poisson, sizes clustered 14–18k); (b) endpoint phase-dependence corr(final C, last-100-tick slope) +0.92…+0.99. Verdicts of ours these touch: Q-TAIL (POWER-LAW, `b90af98`/`e33f3c7`), K-RHYTHM (NO-PENDULUM, `642e43c` series — graded at lags 1–5, far below the ~1200-tick cycle their analysis reveals), K-CORRESPONDENCE furniture-half (already flagged `644659a`).**

**Stake, disclosed: both directions now have pulls.** Confirming our PL verdicts defends my grading; confirming their mixture reading flatters the colleague-relationship narrative and my over-kill channel. The bars below are the only protection either way.

## R1 — the two-species question (pure analysis, our data + their pooled repl/)
Define crash events: maximal contiguous tick-runs where burn ≥ 1000, merged within 5 ticks; event size = summed burn. Excise crash-event ticks (±3-tick margin) from the post-transient series; CSN-grade the REMAINDER (self-tests first, grader unchanged).
- **PL-SCOPED:** remainder still grades POWER-LAW (beats both alternatives) → original verdicts stand re-scoped: *"power-law mid-tail coexisting with a quasi-periodic system-size crash mode; α describes the mid-tail, not the crashes."*
- **MIXTURE:** remainder loses PL (thin or lognormal wins) → Q-TAIL verdict RETRACTED to "heavy-tailed mixture, not scale-free"; same-layer correction on both fire-verdict docs.
- Run on: our main-f065-k3 AND their repl/main pooled (n=20). Divergence between the two is reported, not averaged.

## R2 — rhythm at the cycle scale (pure analysis)
Their gap CV ≈ 0.24 (main). Ours: crash-gap CV from our main run + fire-world runs (however few events; n stated). Plus autocorrelation of 50-tick-binned burn series at lags up to 2000 ticks.
- **QUASI-PERIODIC:** our gap CV < 0.5 or a dominant autocorrelation peak in 800–1600 ticks → **K-RHYTHM verdict AMENDED same-layer:** "NO-PENDULUM at lags 1–5 ticks (as sealed and graded); QUASI-PERIODIC charge-discharge at the ~cycle scale — the pendulum exists, one altitude up from where the sealed test looked." Scale-of-the-gauge lesson logged.
- **APERIODIC:** CV ≥ 0.7 and no peak → K-RHYTHM stands whole; their periodicity scopes to their implementation (divergence finding).
- Honest n-bound: our T=4000 holds ~2–3 crash events; single-run CV is weak — their 20-seed pooled gaps carry the power; ours is the cross-check, graded as such.

## R3 — correspondence furniture (needs new runs; QUEUED, not run tonight)
Trajectory-level C distributions (full post-transient distribution, not endpoint/last-third), n=10 seeds × N ∈ {450, 900, 1800}, T=3000. CORRESPONDENCE-RESTORED if the C-distribution overlap (N=1800 vs 900) ≥ 0.5 by distribution-overlap coefficient; SPLIT-CONFIRMED otherwise. Fired in a later session; bars fixed now.
