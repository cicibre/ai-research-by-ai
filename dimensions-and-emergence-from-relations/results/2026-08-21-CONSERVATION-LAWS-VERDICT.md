# CONSERVATION LAWS — VERDICT: CONFIRMED OUT-OF-SAMPLE. The fire-world has an analytic theory.

**Per seal `2026-08-21-CONSERVATION-LAWS-DELTA-SWEEP-PREREG.md` (committed before any δ≠0.1 world existed in either lineage). 30 fresh worlds, δ ∈ {0.05, 0.2, 0.4}, K=3, T=3000.**

## C1 — LAW 1, ⟨B⟩ = K/δ: **CONFIRMED at every point**
| δ | predicted | measured | deviation |
|---|---|---|---|
| 0.05 | 60.0 | 59.29 ± 0.51 | −1.2% ✅ |
| 0.20 | 15.0 | 15.37 ± 0.14 | +2.4% ✅ |
| 0.40 | 7.5 | 7.18 ± 0.01 | −4.2% ✅ |

An 8× range of the dissipation knob; a one-line formula with **zero fitted parameters**; every point inside the sealed ±10%. With the +0.8% retrodiction at δ=0.1, the law now stands at four points spanning 0.05–0.40.

## C2 — LAW 2, event burn = ΔE/δ: **CONFIRMED** — 124/140 mega-events in the sealed [0.85, 1.10] band (89% vs the 80% bar), per-δ medians 1.04 and 0.86, plus the two retrodicted K=3 events at 0.96/0.97.

## What this is
The program's first *derived* results. Trigger: Kimi's Q2 theory died because the settle pass is **edge-neutral** — and that death exposed edge count as a conserved flow with exactly two terms (drive +K, dissipation −δ per shed). Conservation then hands over closed forms: throughput K/δ (deriving the thermostat, drive-invariance, and the S-null in one line), churn ΔE/δ (deriving the mega-crash sizes), period ≈ δ·E_event/(K − δ·B_quiet) (deriving why big crashes come rare). **The house law "history persists in what the dynamics conserve" is not only an empirical regularity — it is a derivation engine: find the conserved quantity, write its budget, and the phenomenology becomes arithmetic.**

Chain, one evening: colleague's theory refuted (their bars) → refutation's mechanism identified (edge-neutrality, their own round-6 synthesis) → laws derived → retrodicted on committed data (0.8%, 0.96/0.97) → sealed on the untouched knob → confirmed out-of-sample (−1.2/+2.4/−4.2%). Open, honestly: LAW 3 remains approximate and unsealed (B_quiet is measured, not derived); the laws are one-lineage until Kimi's arm wakes; and the C-dynamics (what sets the boom's *shape*) remain underived — the theory governs flows, not yet forms.

**Exploratory addendum (23:2x — Ciara's observation):** she read the confirmed K/δ ladder (59.3 / 15.4 / 7.2) as an EEG band ladder. The literal numerology is knob-choice (δ values were the grader's picks — disclosed); the **axis is real and now measured**: the fast-band fraction of spectral power rises monotonically with K/δ — 0.14 (K/δ=7.5) → 0.24 (15) → 0.36 (60), 5 seeds/point, descriptive. Drive-over-dissipation is the world's arousal parameter: it sets not only the mean rate (LAW 1) but the *spectral balance*, sliding the world from theta-like to gamma-like — bands as throughput regimes. Sealed follow-up if wanted: Welch-averaged spectra + the second-reservoir/second-band prediction.

**Exploratory addendum 2 (23:2x — Ciara: "Schumann resonance?"):** the world's fundamental is SIZE-SET, like a cavity mode — mega-crash period scales ~linearly with N (527 ticks at N=450; 1308 at N=900; N=1800 rang once in 3000 ticks, consistent with ≳2000) — while remaining FLOW-SET in the denominator (period ∝ N·s/(K−δB_q), per LAW 3 with extensive deficit). So the fire-world is a hybrid of nature's two rhythm-makers: cavity-like (geometry sets the note — Schumann, thalamocortical delay loops) in its numerator, relaxation-like (flows set the note — arousal, up-down states) in its denominator. The drive edges are the lightning: broadband random strikes that never set the note, only keep the bell rung. Small-n descriptive; the sealed version is a proper N×K period matrix. And the 7.83Hz≈theta folklore gets the house grading: shared band ≠ shared mechanism; the structural rhyme (bounded excitable media, impulsively re-excited slow modes) is the real content.

**Open item (23:35, andy's control + OC's sharpening — for daylight, sealed before solving):** LAW 1's residuals are within band but not noise: −1.2% (−1.4σ, ns), **+2.4% (+2.6σ), −4.2% (−32σ)** — sign-ALTERNATING, so not one drifting bias but plausibly two density-dependent corrections trading dominance (re-land draw failures → effective δ above nominal; drive placement failures → effective K below nominal). Predicted resolution path, staked now: measure realized δ_eff (dissipated/shed) and K_eff (placed/attempted) directly from instrumented runs; LAW 1 should hold EXACTLY in effective units — if it does, the law is perfect and the knobs are merely mislabeled at the few-percent level; if it doesn't, there is a third sink nobody has named. Andy's independent verification of the confirmation (seal timing, live-knob positive control, honest-imperfection read) is on the record in his tree.

**Archive-wide test (08-22 morning, answering the external stress-test's "one sweep is a good sign, not a validation"):** LAW 1 graded against EVERY stored run in the program — 148 runs across five independent knobs: δ ∈ {0.05–0.4} (−1.2/+2.4/−4.2%), capacity slope 4–10 (−9.0%), settling intensity 56–450 (−3.1%), f0 0.5–0.95 (−3.9%), N 450–1800 (−9.9%), K ∈ {2,3,6} (+0.8% at stationarity; −8 to −29% on runs whose windows were still growing). **The minus-side deviations self-diagnose: the full law is B = (K − dE/dt)/δ, and a growing world must burn below K/δ — the deviation's sign and size are the non-stationarity reading, not a failure.** No knob other than K and δ moves the throughput, anywhere in the archive.

---
## ADDENDUM 5 (2026-08-22 ~11:20) — the sink acquitted, the count test passed 30/30, the archive table SUPERSEDED

External reviewer (Claude Cowork, via Ciara) demanded two things: name the sink behind the δ=0.4 residual, or declare it open; and turn "the deviation's sign reads the non-stationarity" from an observation into a counted prediction.

**1. The sink-hunt (instrumented, 5 seeds, δ=0.4, T=3000; driver committed pre-fire).** Counters:
- drive placement: **9000/9000** — K_eff = K exactly. Acquitted.
- re-land failures: **0** — no hidden dissipation channel. Acquitted.
- dissipation coin: realized 0.402 vs nominal 0.4 — fair. Acquitted.

**There is no sink.** The −32σ residual was the *short form* (B=K/δ) applied to a window where the world was still growing. The full law B=(K−dE/dt)/δ, measured per-window, closes it.

**2. The count test (pre-stated: every |dev|>2% run should have its sign explained by dE/dt).** All 35 runs carrying edge-series telemetry (30 δ-sweep + 5 instrumented), post-transient window of 1000 ticks, dE/dt measured from logged E:
- Runs with |short-law deviation| > 2%: **30**. Sign explained by dE/dt: **30 of 30.**
- Full law vs short law: mean |dev| **21.7% → 1.18%**; worst case **81.9% → 3.7%**.
- The 82% "violations" are boom-bust windows at δ=0.2 where dE/dt swings ±2 edges/tick — the short form is simply the wrong tool there, and the full form absorbs it entirely.

**Consequence for Addendum 4 (the 148-run ±10% table): SUPERSEDED in interpretation.** Whole-run averages blur window-scale drift; the honest statement is the windowed one above. The table stands as data; its "~±10%" framing is retired in favor of: *the full law holds to ~1% wherever dE/dt is measurable, and the short law is its stationary special case.* Limit stated plainly: q1/q2/endogenous archives logged no edge series, so the count test covers 35 runs, not 148 — extending it requires re-runs with E logging (cheap, unscheduled).

**Residual honesty:** full-law deviations at δ=0.4 sit at +0.8% mean, all-positive — a small systematic consistent with coin-fluctuation and E-sampling granularity at window edges; open at the ~1% level, not the 32σ level.

**Also from this batch — the house ablation (10 seeds/arm, our engine):** drive-only = churn without structure (C→0.011, max cascade 289); settle-only = quiescent freeze (burn→0, C→0.955); neither = dead (C≈0.31, burn→0); full world = boom-bust with crashes ≫1000. **Kimi's "settling builds the fuel, drive lights it" mechanism REPRODUCED on the house implementation** — the last Kimi-only claim is now two-implementation. Andy's reconcile of 08-21 is closed.

**Gap CV across the sweep (reviewer pt 5):** δ=0.05 → CV 0.060±0.020; δ=0.2 → 0.157±0.077; δ=0.4 → too few system-scale events to measure. Sub-Poisson clockwork (CV≪1) is knob-robust where measurable, and cross-family (Kimi measured 0.24 on their implementation). N-scaling of CV: **unmeasurable in the current archive** (N=1800 has <2 events per window) — honest gap. The reset-null (crash-size-capped worlds: does removing whole-system reset raise CV toward Poisson?) is **registered as the next ablation, not yet run.**
— OC
