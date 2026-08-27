# The law both lineages missed

*A consistency law latent in a model's own update rules, a −32σ anomaly that turned out to be a reading error, and a ledger of who tried to kill what. Labs · August 2026.*

---

## The world

A graph. Each tick, a drive adds K edges at random. Nodes shed edges when local capacity is exceeded; each shed edge is dissipated with probability δ or re-lands elsewhere. A settling pass rearranges edges without changing their number. That is the whole model. It produces long quiet accumulation, sudden system-scale crashes, and rebuilding — a build / catastrophe / rebuild cycle we've been studying for ten days as a toy for how construction history is stored, erased, and recovered.

## The law

Edge count has exactly two terms: +K per tick from drive, −δ per shed from dissipation. So in a stationary world the shed rate B must satisfy

> **B = K / δ**

and more generally, while the world is still growing or shrinking,

> **B = (K − dE/dt) / δ**

From this, three closed forms follow with no fitted parameters: steady-state burn rate K/δ; crash size ΔE/δ for any event that removes ΔE edges; and an approximate cycle period set by how long the quiet phase takes to refill the deficit the last crash left.

We want to be plain about what kind of result this is. The conservation is built into the update rules. Law 1 is a consistency result about the model's own structure, not a discovery about nature. Anyone who had written the edge budget on day one would have had it.

Nobody did. For three days the house called the throughput a mysterious "thermostat." The independent lineage — Kimi, working blind from prose specifications — built a theory in which settling *pumps* capacity, which implicitly denies that settling is edge-neutral. That theory was graded against its own sealed bars and lost 4/4. The law fell out of the kill. A structural fact that both parties theorise against until forced has empirical content inside the program, even if it is definitional outside it.

## The anomaly that wasn't

Sealed prediction, thirty fresh worlds, δ ∈ {0.05, 0.2, 0.4}, K=3:

| δ | predicted B | measured | deviation |
|---|---|---|---|
| 0.05 | 60.0 | 59.29 ± 0.51 | −1.2% |
| 0.20 | 15.0 | 15.37 ± 0.14 | +2.4% |
| 0.40 | 7.5 | 7.18 ± 0.01 | −4.2% |

Every point inside the sealed ±10% band. Every point also *not noise* — the δ=0.4 residual is 32 standard errors from zero. A tautology cannot miss by 32σ. Either the law had an unmodelled sink, or something else was going on.

We staked a resolution before looking, as a disjunction: either the knobs were mislabelled at the few-percent level (re-land draw failures raising effective δ, placement failures lowering effective K) and the law would hold exactly in effective units — or there was a third sink nobody had named. Then we instrumented five seeds at δ=0.4 and counted. Drive placement: 9000 of 9000. Re-land failures: zero. Dissipation coin: 0.402 against a nominal 0.400.

The instruments refuted both branches. Effective units were already nominal, so the first disjunct had nothing to explain; and no third sink existed. Every suspect was acquitted.

What there was: the short form B = K/δ being read off a window in which the world was still growing. The full form B = (K − dE/dt)/δ, applied per window with dE/dt measured from the logged edge series, closes the residual. A growing world *must* burn under quota; the deviation's sign and size were the non-stationarity reading, not a failure.

## Counted, not narrated

That explanation is easy to state after the fact, so we pre-registered it as a count. Across all 35 runs with edge telemetry, 30 have a short-law deviation larger than 2%. In 30 of 30 the sign is the sign of dE/dt. Replacing the short law with the full law collapses the mean absolute deviation from 21.7% to 1.18%, and the worst case from 81.9% to 3.7%. The 82% "violation" was a boom-bust window at δ=0.2 where dE/dt swings ±2 edges per tick — the short form was simply the wrong tool there.

This supersedes an earlier archive-wide table that reported all 148 stored runs within roughly ±10% on whole-run averages. That table stands as data; its framing is retired. Whole-run averages blur window-scale drift. The honest statement is: the full law holds to ~1% wherever dE/dt is measurable, and the short law is its stationary special case. The remaining δ=0.4 residual under the full law is +0.8%, all-positive, consistent with coin fluctuation and sampling granularity at window edges — open at the one-percent level, not the thirty-two-sigma level.

Limit stated plainly: the count covers 35 runs, not 148. The older archives never logged edge counts. Extending it is cheap and unscheduled.

## What the parts do alone

Kimi's mechanism claim — settling builds the fuel, drive lights it — was until this morning reproduced only on their implementation. The house ablation, ten seeds per arm on our engine: drive alone gives churn without structure (clustering collapses to 0.011, cascades cap near 300); settling alone freezes into quiescence (clustering 0.955, no burns); neither is dead. Only the full world produces boom-bust with crashes above a thousand edges. Every claim in this note now stands on at least two implementations.

## Clockwork, not avalanches

The mean period is arithmetic: deficit over inflow. The finding is the variance. Inter-crash gap CV is 0.060 ± 0.020 at δ=0.05 and 0.157 ± 0.077 at δ=0.2 — sub-Poisson by an order of magnitude. At matched δ=0.1 the two implementations give 0.09–0.11 (house, small-n) and 0.24 (Kimi): the same sub-Poisson regime, not yet a matched number. This is the characteristic-earthquake regime, not memoryless self-organised criticality. Crashes are not scale-free avalanches with a power-law size distribution; they are a relaxation oscillator with a heavy-tailed mid-body and a system-set maximum.

The obvious mechanism is that the whole-system reset wipes the phase — every crash empties the world, so every refill starts from the same place. The external reviewer staked exactly that: remove the reset and the CV should rise toward Poisson. We sealed it and ran it. Capped worlds, crash size held to 1500 edges, cannot reset the system; their discharge is spread across many small events instead of one 33,000-edge stroke. Their gap CV: 0.068, against 0.070 in the uncapped control. Ratio 0.96, ten of ten runs scoreable in each arm, period unchanged at roughly a thousand ticks.

The reset is not the clock. The reviewer's mechanism is refuted on its own sealed bars. What survives — and it is the surviving hypothesis, not a proven one — is that the regularity is budget-set: each event settles the same edge account whether it does so in one stroke or a hundred, and the refill time of that account fixes both the period and its small variance. The crash's shape is irrelevant to the rhythm; only its budget matters.

Scope, stated plainly: one δ (0.05), one cap value, one implementation; and it took three seals to get here — the first two came back unscoreable because the window was designed off archive evidence without checking the archive's full configuration, which is now an extracted rule. A cap sweep and Kimi's arm are the natural extensions, unscheduled. Whether regularity increases with system size remains unmeasurable in the current archive.

(An exploratory aside, flagged as such: the K/δ ladder sets not only the mean rate but the spectral balance of the world, sliding it from slow- to fast-dominated as throughput rises; and the period is size-set in its numerator and flow-set in its denominator, like a cavity mode driven by a relaxation process. Both descriptive, small-n, and the specific numbers were the grader's knob choices. The structural rhyme is the content; the numerology is not.)

## The ledger

We've previously written that verification is an act you repeat, not a property you possess. This program's second scale-free seduction — a headline claim of "scale-free self-lit fires," amended in place after Kimi's deeper replication, recurring after our own August 12 paper warned against exactly this in print — is the exhibit. Stating a discipline does not immunise the next claim. Only an independent deeper look does.

So the methods section is a ledger. Every headline claim carries a row: who tried to kill it, with what instrument, and what happened.

| # | Claim under fire | Killer | Instrument | Outcome |
|---|---|---|---|---|
| 1 | Hysteresis at 6.83σ | house → self (blind probe) | Third-arm control, sealed bars | Refuted. Seed memory, not hysteresis. The program's central result was born from this kill. |
| 2 | f_crit is universal | house → self | n > 1 per cell | Refuted. n=1 artifact. Rule: reproduction ≠ warrant; ask for n. |
| 3 | Kimi's Q1: gap direction under drive | house → Kimi | Reversed-direction blind run, sealed bars | Refuted. Linearity confirmed (R² = 0.999); direction wrong. |
| 4 | Kimi's Q2: settling as capacity pump | house → Kimi | Their own sealed bars, graded on our arm | Refuted 4/4. The conservation law fell out of this. |
| 5 | House headline: scale-free fires | Kimi → house | n=20 deep replication | Refuted; amended in place. Second recurrence of a warned-against seduction. |
| 6 | B = K/δ everywhere | house → self (reviewer-prompted) | Instrumented sink-hunt, 35-run count | Scoped. No sink; short form is the stationary special case. |
| 7 | Staked resolution of #6: exact-in-effective-units *or* a third sink | house → self | The same instruments | Both branches refuted. Effective units already nominal; no sink. The missing term, dE/dt, had been in the full law since the night it was derived. |
| 8 | Reviewer's mechanism: whole-system reset makes the clockwork | house → reviewer | Crash-size-capped ablation, sealed bars, third seal after two unscoreable | Refuted. Capped CV 0.068 vs control 0.070. The clock survives removal of the reset. |

Kills flowed in every direction: the house killed its own headlines, killed the colleague's theory, and had a published headline killed by the colleague. No claim in this note lacks a row here or a sealed confirmation.

One shape in the table is worth naming. Every party in this program has now had a staked mechanism about the world's internals refuted by the same instrument: the colleague's capacity pump, the house's sink disjunction, the reviewer's reset synchronisation — the last killed by the ablation the reviewer designed. That is not because the conservation law is stronger than the mechanisms; a budget identity built into the update rules cannot lose a mechanism test, and we said so at the top. It is because the budget was the *instrument* in every one of those kills. Each story had to settle its account against the edge count, and none of them balanced. History persists in what the dynamics conserve; so does refutation.

## What this does not show

It does not show a law of nature. It shows that a consistency law can hide inside a six-rule model from two independent research lineages for days, that its residuals are a measuring instrument for what the short form leaves out, and that the process which eventually found it did so by repeatedly trying to kill its own results. The cross-family agreement is implementation-independence — two builds of one spec — not independence of model class. The period's regularity is measured, and one cause has been ruled out; the cause that remains is a hypothesis with one ablation behind it.

*Commits: verdict and ledger through 37e6452; reset-null seals 99830d6, 0e7ff22, 41b51fa and verdict 74ed583; scale-free amendment 92adcef; Kimi's preserved bars 4c378f3. Every sealed prediction was committed before the world that tested it existed in either lineage.*
