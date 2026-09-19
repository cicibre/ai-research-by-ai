# CONNECTOME CAPACITY TEST — base prereg, SEALED BEFORE ANY CONNECTOME DATA IS OPENED

**chamberlain, 2026-09-02 ~15:5x EDT. Sealed before download. No connectome file has ever existed on this machine — verified by `find /Users/cc/academics -iname "*connectome*" -o -iname "*celegans*"` returning empty, and `data/` containing only the p-spin/thread sources and the R/S arrays.**

## ⚠️ PROVENANCE — the ordering is odd and is stated rather than smoothed

This base prereg is written **today, now**. Its *intent* was drafted yesterday ~14:1x EDT: the desk announced "Starting the connectome seal now," was interrupted by Ciara's "the core becomes incorruptible," and **the base was never written to disk.** What existed on disk before this file was an **amendment to a document that did not exist** (`2026-09-02-CIARA-TWO-PHASE-SELECTION-STAKE.md`, sealed 14:18, § "AMENDMENT TO THE CONNECTOME TEST").

So: **the amendment predates the base.** That is unusual and a reader should not infer a clean sequence. What makes it legitimate rather than a reconstruction is that **neither document was written with any connectome data in hand** — the amendment was sealed 14:18 yesterday with the substrate un-downloaded, and this base is sealed with it still un-downloaded. The bound-vs-mean commitment below is recoverable verbatim from the session transcript at `transcripts/2026-09-02-witness-architecture-session-export-REDACTED.txt:5947`, written yesterday, before this file:

> "It isn't a graded refutation yet, because our law is a bound and that's a mean — a node can sit far below its ceiling. **But that defence is exactly the kind I could construct after seeing data, so it has to be pinned before.**"

That sentence is the reason this document exists. It is pinned below.

---

## THE CLAIM UNDER TEST — and it is the only one that survived the sweep

`cap(v) = BASE + ALPHA · c(v)` — **a node's capacity is set by its local clustering**, i.e. by how *witnessed* its relations are. As implemented (`code/2026-08-19-endogenous-burn-harness.py:29,37`): `BASE, ALPHA = 12, 8`, `c` = standard local clustering coefficient, undirected, unweighted; a node topples while `deg(v) > cap(v)`.

**The novelty is the denominator, not the threshold.** Per `results/2026-09-02-FULL-PRIOR-ART-SWEEP.md`: ignition-at-critical-load, tail-truncation-by-immune-elements, and the protection trade-off all collided with established work and are demoted. Capacity-from-degree/betweenness/centrality is extensive prior art and was never claimed. **Capacity from local closure is the one thing that survived**, and this test is the only planned experiment that touches it.

**Restated as a structural claim, testable with no events and no time series** (per `results/2026-09-02-NOVELTY-BOUNDARY-two-collisions-in-one-day.md:26`): *does a completely-mapped real network show degree bounded above by a term that rises with local clustering?*

## ⛔ PIN 1 — BOUND, NOT MEAN. Fixed here so it cannot be constructed later.

Our law asserts a **ceiling**, not a central tendency. A node may sit arbitrarily far below its ceiling. Therefore:

- The well-established negative **conditional-mean** relation `C(k) ~ k^−1` (Ravasz–Barabási; and in connectomes specifically, "local clustering coefficient steadily falls with node degree") **does not by itself refute this claim**, and this prereg says so *before* seeing data.
- ⛔ **But that defence is only admissible because it is written here, now.** It may not be invoked in any stronger form than this paragraph after data is opened.
- **The test statistic is therefore an UPPER-QUANTILE regression of `k` on `c`**, not OLS and not a correlation. Headline quantile **τ = 0.90**, pre-committed. Sensitivity grid τ ∈ {0.80, 0.95}; **the headline is τ = 0.90 regardless of which looks best.**
- **Pre-committed direction:** slope of the τ = 0.90 quantile fit of `k` on `c` is **positive**.

## ⛔ PIN 2 — THE STRATIFICATION IS THE HEADLINE. Amendment stands verbatim.

The amendment sealed 14:18 yesterday (`2026-09-02-CIARA-TWO-PHASE-SELECTION-STAKE.md:29-35`) governs, unmodified. Restated for self-containment:

1. **Stratified by degree, not pooled.** Hub and periphery analysed separately.
2. **Split criterion must NOT reference clustering** (else circular). Split on **degree percentile, cut frozen at top decile = hub**; pre-committed sensitivity at top 5% / top 20%; **headline is the decile regardless of which looks best.**
3. **Pre-committed directions:** the capacity relation **holds in the periphery**, **fails or inverts in the hub class.**
4. ⛔ **REFUTED IF the relation fails in the periphery too.** That is the outcome that kills our one surviving claim. *If the periphery fails, no further splitting is permitted.* **One stratification, pre-declared, and no more.**
5. **Also refuted, other direction:** if the relation holds *equally* in both classes, her two-population stake fails even if our capacity law stands — **and that must be reported as her stake failing while ours survives.**

**Why pooled is NOT the headline, decided before data and on published shape alone.** Prior-art searches run today (before download) establish the joint distribution: mass at high-`c`/low-`k`, a few nodes at low-`c`/high-`k` — hubs are bridges between modules and have low clustering *by construction*. A pooled upper envelope of `k` on `c` therefore slopes **downward by arithmetic, not by physics**. Pre-committing a pooled kill condition would schedule a refutation and call it a test, and it would refute by exactly the averaging-two-populations mechanism the amendment was written to prevent. **Pooled is reported as context, never as headline, and never as a kill condition.**

*(Excluded by name and kept out: the "two routes to permanence" / woven-vs-load-bearing speculation was barred from this prereg at 12:26 yesterday and stays barred. It is desk speculation with no test attached.)*

## ⛔ PIN 3 — THE TIGHTNESS DIAGNOSTIC, and it runs BEFORE the slope is read

**A ceiling only leaves a signature where nodes are pressed against it.** If most neurons sit far below any constraint, the upper quantile of `k` reflects whatever development happened to build, not a binding cap — and the slope is then uninformative *whatever its sign*. This is the power problem, and it is distinct from the bound-vs-mean problem.

**Operationalised, pre-committed, computed and reported before the slope is interpreted:** on the periphery stratum, measure whether the upper edge of the (`c`, `k`) scatter is **sharp** or **diffuse**. Statistic: the ratio of residual spread above the τ = 0.90 fit to residual spread below it (edge-sharpness ratio, ESR). Pre-registered cut: **ESR < 0.5 ⇒ sharp** (upper edge is a genuine boundary); **ESR ≥ 0.5 ⇒ diffuse.**

- ⛔ **Diffuse edge ⇒ the test is INCONCLUSIVE, not refuting, and not confirming.** No ceiling is active; the substrate cannot answer the question.
- ⛔ **And the converse is pinned with equal force, so this is not an escape hatch: sharp edge with slope ≤ 0 against the null ⇒ THE CLAIM DIES**, per clause 4, and no further splitting is permitted.

## ⛔ PIN 4 — THE DEGREE-PRESERVING NULL IS LOAD-BEARING, NOT DECORATIVE

`c = 2T / (k(k−1))` has `k` in its denominator: **clustering is mechanically anti-correlated with degree.** Any slope reported without a null is uninterpretable.

**Null model:** degree-preserving **double-edge swap** (configuration-model randomisation), which holds the degree sequence *exactly* and destroys clustering structure. **1,000 randomisations**, 100·|E| swap attempts each. The observed τ = 0.90 slope is compared against the null distribution of the same statistic; **the reported effect is the observed slope's z-score / percentile against that null, never the raw slope.**

**Confirmation requires the observed slope to be positive AND above the 97.5th percentile of the null.** A positive raw slope that sits inside the null band is **not** confirmation and will be reported as a null result.

## ⛔ PIN 5 — SUBSTRATE LADDER AND POWER, both named now so the second is not a rescue

1. **C. elegans** (~302 neurons, ~2,300 edges; complete, public). **Same-day go/no-go.** Periphery n ≈ 270.
   - ⛔ **Power statement, pinned:** at n ≈ 270, τ = 0.90 quantile regression is fit on ~27 effective upper-tail points. **A null result at this N is INCONCLUSIVE, not refuting.** Only a *sharp-edge negative slope significant against the null* refutes at this stage.
2. **FlyWire adult *Drosophila* whole-brain connectome** (~130k neurons; complete). **The decisive run.** Named here, before the C. elegans result is known, precisely so that escalating to it later cannot be a rescue.

**Directedness:** connectomes are directed and weighted; our law is undirected and unweighted. **Pre-committed: symmetrise to undirected, binarise, self-loops dropped.** That is the faithful analogue of the implemented law. Weighted/directed variants are **not** part of the headline and may not be substituted for it.

## ⚠️ PRIOR-ART CHECK — run BEFORE substrate choice, per the standing lesson

Four searches today, before any download, aimed at the discriminating question: *has anyone reported an upper bound / envelope / maximum-degree-given-clustering, as opposed to the conditional mean?*

**Result: no collision found.** Everything returned is conditional-mean territory — `C(k)` falling with `k`, redundancy falling with `k`, rich-club organisation, higher-order-clustering bounds (bounds *between orders of clustering coefficient*, not on degree). **No envelope or upper-bound treatment of `k` given `c` was found in any network, connectome or otherwise.**

⚠️ **BOUND ON THIS CHECK, stated where the verdict's reader will see it, and identical in kind to the bound on the 14:2x sweep:** four searches, **one engine, in English, in our vocabulary.** That is a check, not a literature review. **A negative from four searches is weak evidence of absence.** This test's entire value rests on that negative, which is exactly why the bound is recorded here and must be repeated in the verdict. The specific unsearched risk remains vocabulary mismatch — the same idea may exist as *"redundancy-weighted tolerance"*, *"local-redundancy capacity"*, or inside the k-core / structural-cohesion literature.

## GRADING — fixed before data

| outcome | verdict |
|---|---|
| Periphery: sharp edge, slope > 0, above 97.5th pct of null; hub class fails/inverts | ✅ **Capacity law survives its first real-network test AND her two-population stake holds** |
| Periphery: sharp edge, slope > 0 vs null; hub class **also** holds equally | ✅ ours / ⛔ **hers refuted** — reported as her stake failing while ours stands (clause 5) |
| Periphery: sharp edge, slope ≤ 0 or inside null band | ⛔ **THE CLAIM DIES.** No further splitting. |
| Periphery: diffuse edge (ESR ≥ 0.5) | ⚠️ **INCONCLUSIVE** — no active ceiling; escalate to FlyWire per the ladder, and *only* per the ladder |

⛔ **Standing prohibition, carried from yesterday, where it held twice:** if a sealed statistic fails while an alternative reading of the same data would rescue it, **the rescue is refused.** That happened at 10:2x (H1b, SD vs CV) and 14:5x (allocation — and the rescuing idea was Ciara's, and better). Both refused. It does not become available here.

---

*Sealed by chamberlain before download. Amendment authored by Ciara (mechanism) + desk (test design), 2026-09-02 14:18. Base pinned 2026-09-02 ~15:5x.*
