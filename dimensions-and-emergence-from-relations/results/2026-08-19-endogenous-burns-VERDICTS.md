# Endogenous-burn world — first verdicts (per seal `234c291`; harness pre-committed; grader self-tested pre-data `66ab277`)

**Runs:** 6 worlds, 19,000 ticks total (N=900; main f0=0.65 K=3 T=4000; drive variants K∈{2,6}; substrate variants f0∈{0.5,0.8,0.95}). Raw burn logs: `results/endogenous-burns/*.json`, committed unedited.

## Gates
**(a) Conservation: PASS** — main run's last-third edge drift −0.8% (growth was the approach to stationarity; the dissipation valve balances the drive). **(b) Transient rule: functioned** — t* identified per run by the sealed ±10% running-mean rule (116–1514 ticks), all grading post-transient. **(c) Drive invariance: PASS on the sealed criterion** — the Q-TAIL *verdict* (POWER-LAW) is stable across K halved and doubled. **Flagged honestly: the exponent is NOT drive-invariant** (α = 2.31 / 2.42 / 1.76 at K = 2/3/6) — the tail's existence is the world's property; its slope partly the drive's. Any downstream use of α must state the drive. **(d) Known answers: PASS** (local topple 6 edges; zero-headroom cascade 7,537).

## Q-TAIL: **POWER-LAW — ~~the world lights scale-free fires~~.** ⚠️ **[HEADLINE AMENDED 08-22, in place:** "scale-free" is retracted as the headline — the deeper cross-family analysis (Kimi n=20 + our cycle-aware re-grade `76a0f8f`) shows a MIXTURE: a power-law mid-tail (the narrow CSN claim, which stands, both lineages) COEXISTING with a quasi-periodic, capacity-limited system-scale crash mode (characteristic size ~14–19k set by the cap slope; characteristic period ~1200 ticks; gap CV 0.09). Two characteristic scales = not scale-free. This is the program's SECOND scale-free seduction (R6's sandpile was the first, killed by our own prereg) — our own 08-12 abstract warned "scale-free is the signal a mis-specified estimator most readily manufactures," and it recurred anyway until an unrelated mind looked deeper. The correct headline: **a quasi-periodic relaxation oscillator with a heavy-tailed mid-body.**]**
5 of 6 runs graded POWER-LAW by the full CSN discipline (gof-p 0.83–1.00; beats exponential AND lognormal, Vuong p ≤ 0.015 everywhere it was declared). Main run: α = 2.42, xmin = 16, n_tail = 736, gof-p = 0.99. The exception, honestly: f0=0.95 graded HEAVY-TAILED-NOT-PL (n_tail = 76 — the weakest data, not a clean refutation). Nobody chose these sizes; the threshold dynamics did.

## Q-EXPONENT-SUBSTRATE: SUGGESTIVE, not graded.
α spans 1.75–2.42 across substrates, but xmin regimes differ wildly (16 vs 216) and gate (c) shows the drive also moves α — substrate and drive effects are not separable in this design. An honest grade needs a factorial (f0 × K) run; queued, not claimed.

## Q-SPIRAL: **NO at stationarity — and it could not have been otherwise.**
Post-transient, k_sd does *not* climb (Spearman vs cumulative-burned = **−0.35**; 2.45 → 2.32). This is not a failed replication of the tree-ring result — it is its scope discovered: **a stationary state forbids any monotone observable.** The exogenous five-cycle worlds were far from equilibrium; their spiral is the signature of a world *not yet at equilibrium with its fires*. A world at equilibrium stops counting its catastrophes — the ledger reaches a steady state where scars heal at the rate fires write them. Tree rings record history because trees die before stationarity. The spiral result stands, re-scoped: **the helix is a non-equilibrium phenomenon; the circle is what equilibrium looks like in every channel.**

**Emergent observation (descriptive):** the stationary world self-organizes to extreme clustering (C ≈ 0.86 vs ≈ 0.3–0.45 in exogenous worlds) — capacity rewards clothed structure, so what survives the fires is overwhelmingly the clothed: **survival-of-the-clothed as an emergent selection principle**, consistent with the seed mechanism but now produced by the world itself.

## Q-RHO-FREE: NOT RUN — named, not dodged.
Harness v1 records burn sizes and summary series but **no world snapshots at burn moments**; the free-range ρ comparison needs the graphs. Requires an instrumented v2 run (snapshot-on-large-burn). Queued as the program's next sealed step; the (retained)^2.3 prediction stands untested against free fires.

*Grader softness carried from its own self-test: on a synthetic lognormal the PL-vs-LN comparison flattered the power law; the verdict was saved by the beat-BOTH conjunction. The 5/6 declarations above all beat both alternatives decisively (p ≤ 0.015), well clear of that softness — but it is on the record.*

— OC (verdicts mechanical; scope prose mine)
