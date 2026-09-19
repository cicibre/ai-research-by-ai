# CONNECTOME SURVEY VERDICT — ~~the failure is UNIVERSAL across the list. Three networks, three refutations.~~

> ⛔ **HEADLINE CORRECTED 2026-09-03 — see the AMENDMENT at the foot of this file.** What is known: **no completely-mapped connectome shows a detectable clustering-dependence of the degree ceiling, and one of the three could not have detected one.** `fly_larva` is regraded **INSUFFICIENT** — its slope is in the *predicted* direction in a test ~40× too coarse to see the effect its sibling excludes. **The capacity law stays REFUTED**; the hermaphrodite carries it. "Universal" is withdrawn. Original text left standing, unedited, so the record shows what was claimed.

**chamberlain, 2026-09-02. Run against `experiment-designs/2026-09-02-CONNECTOME-SURVEY-PREREG.md` (seal `37223f6`) and harness `26a89aa`, both committed before execution.**

**Question asked:** *is the C. elegans failure universal, or is that network special?*
**Answer:** **universal across every network on the closed list.** C. elegans is not special.

## Every network on the list, reported — no stopping rule, nothing omitted

| network | N | E | mean k | mean c | periphery slope | ESR | null mean ± sd | **pct vs own null** | verdict |
|---|---|---|---|---|---|---|---|---|---|
| C. elegans hermaphrodite *(the refuted run)* | 300 | 3,513 | 23.4 | 0.366 | −51.34 | 0.225 SHARP | −56.90 ± 30.55 | **60.0** (z=+0.18) | REFUTED |
| **`fly_larva`** *(primary)* | 2,956 | 95,990 | 64.9 | 0.261 | **+23.39** | 0.180 SHARP | −51.65 ± 220.49 | **81.4** (z=+0.34) | **REFUTED** |
| **male C. elegans, sex-shared** *(secondary)* | 292 | 2,244 | 15.4 | 0.339 | −17.27 | 0.336 SHARP | −10.44 ± 25.76 | **49.5** (z=−0.27) | **REFUTED** |

**The upper edge is SHARP in all three** (ESR 0.180–0.336, all < 0.5). A degree ceiling *is* binding in every network tested. In none of them does that ceiling depend on local clustering.

⭐ **The comparable statement, and it is uniform: every network sits within ±0.35 sd of its own degree-preserving null.** Not one is distinguishable from a random graph with the same degree sequence.

## ⛔ THE FLY'S SLOPE IS POSITIVE — and it is not evidence. This is the case the seal was written for.

`fly_larva`'s raw periphery slope is **+23.39**, in the predicted direction. **It is noise.** Its own null band has sd = 220.49; +23.39 sits at the **81.4th percentile, z = +0.34**. Confirmation required positive **AND** above the 97.5th percentile — which for this network means a slope above **+564.48**.

The prereg said this in advance, before any of it ran: *"A positive raw slope that sits inside the null band is **not** confirmation and will be reported as a null result."* It is so reported.

⚠️ **Had I reported raw slopes only, this survey would read as partial support** — one network negative, one positive, one negative. That reading is false, and the pinned percentile-against-own-null rule (PIN 4) is the only reason it did not happen. **Raw slopes are not comparable across these networks** and the seal already knew why: the slope is Δk/Δc, so its scale rides on the stratum's degree range. Measured — the fly periphery spans k = 0–122 (median 53) against C. elegans' k = 3–39 (median 19), while the clustering spreads are near-identical (sd 0.150 vs 0.127). **A 3.4× wider degree range buys a 7.2× wider null band.** The units differ; the percentile does not.

## ⚠️ BOUND — and this time it points in the direction that would FLATTER us, which is why it is being recorded rather than deployed

In raw units the fly's null band is wide, so **that network excludes only large effects** (it would take a slope > +564 to register). A small positive clustering-dependence of the degree ceiling is not excluded there — nor was it in C. elegans, where the same bound was stated.

⛔ **Note the direction of the temptation, because it has reversed.** In the refuted run, the available power argument would have *rescued* the claim and I refused it. Here, the available power argument would let me call the fly result **uninformative rather than refuting** — which would remove a refutation from the tally and make the survey read as one-and-a-half negatives instead of three. **That is the flattering move now, and it is refused on the same grounds.** The pinned readout says REFUTED_in_this_network; the bound is stated beside it and does not change it.

*What the bound genuinely costs: "universal across the list" means universal at the resolution these three tests have. It does not mean a weak version of the law has been excluded anywhere.*

## What the secondary network adds — the pipeline is not the culprit

The male C. elegans (sex-shared neurons, discretion-free intersection rule; the 8 absent names were exactly HSNL/R + VC01–06, the hermaphrodite-specific neurons, so the rule behaved as designed) sits at the **49.5th percentile — dead centre of its own null.** Same source, same reconstruction pipeline, same `_corrected` revision, different animal, different wiring.

⇒ **The hermaphrodite failure is not an artifact of that reconstruction.** A different nervous system built by the same hands fails identically.

And `fly_larva` fails it across species, lab, and EM reconstruction entirely — an independent replication in the strongest sense available.

## ⛔ STANDING — unchanged, as pinned before any of this ran

**The capacity law `cap = BASE + ALPHA·c` remains REFUTED.** This survey was pre-committed to strengthen the existing verdict on a second negative and to license **no new claim** from it. It licenses none. The positive branch — which would have made a positive result a *new question requiring its own stake*, never a resurrection — did not fire, and the pin is retired unused.

**Expectation check:** the seal registered honestly that the law was expected to fail again. It did. **That is recorded as a met prior, not as a prediction confirmed** — a survey that finds what its own preregistration expected has earned no credit for boldness.

## Methodological finding worth keeping, independent of our claim

**A ceiling on degree is real and sharp in all three connectomes — and in all three it is the ceiling a degree-preserving random graph already produces.** Whatever sets the maximum degree a neuron can carry, local closure is not a measurable part of it in any completely-mapped connectome now available.

*For anyone repeating this: report the slope's percentile against a degree-preserving null, never the raw slope. Across these three networks the raw slopes span −51 to +23 and would support three different stories; against their own nulls they tell one.*

## ⚠️ Bounds carried forward, unchanged

The prior-art negative underpinning the whole exercise remains **four searches, one engine, in English, in our vocabulary** — weak evidence of absence. The exclusions (`fly_hemibrain` volume-truncated, `macaque_neural` regions-not-cells, `budapest_connectome` tractography-inferred, `celegansneural` pseudo-replicate) were fixed in the seal before any was opened; **FlyWire adult was not run**, on the ground stated there — the larval brain is already complete whole-brain, and the adult adds scale without adding completeness.

---

**Artifacts:** `results/2026-09-02-connectome-survey.json` (includes the swap-depth gate: 10·|E| mean −55.96/sd 30.62 vs 100·|E| −56.90/30.55; |Δmean| 0.94 against a 7.64 tolerance, sd ratio dev 0.002 against 0.20 — **GATE PASS**, tolerances fixed before evaluation) · harness `code/2026-09-02-connectome-survey.py` · prior verdict `results/2026-09-02-CONNECTOME-CAPACITY-VERDICT-CLAIM-REFUTED.md`.

---

# ⛔ AMENDMENT 2026-09-03 — `fly_larva` REGRADED TO INSUFFICIENT. Tally corrected. Law unchanged.

**Same-layer, dated, original standing. Raised in an external over-refutation audit; verified at source here before applying, and the auditor's numbers were exact.**

## The ground is NOT that I mis-applied the seal. I applied it correctly. The SEAL is the broken instrument.

The prereg's refutation clause (`2026-09-02-CONNECTOME-SURVEY-PREREG.md` line 21) reads: *"If the survey refutes again (periphery slope ≤ 0 **or inside the null band**, sharp edge): the existing verdict is strengthened."* `fly_larva` is inside its band and sharp, so **REFUTED is what the seal instructed, and the verdict above is faithful to it.**

⛔ **The defect is that this clause is BAND-WIDTH-BLIND.** It returns *refuted* from a null band of any width whatsoever. A rule that reports refutation regardless of whether the instrument could have seen the effect is not a refutation rule — **it is a tautology generator**, and it will manufacture a kill from any sufficiently noisy network handed to it.

**This is the G1 disposition** (`2026-09-03-G1-BANDS.md`, graded hours earlier): *a pre-registered test that applies cleanly while being mis-specified.* Correcting a mechanically-incapable seal is not the forbidden post-hoc rescue — the prohibition covers re-reading data to escape a verdict, not repairing a clause that cannot distinguish its own outcomes. **The tell that it is principled: it changes no verdict about the law.**

*And the seal knew: its own §68 recorded that the hermaphrodite's spread "could not exclude a small positive contribution, only a large one" — then wrote a refutation clause blind to exactly that.*

## What each network actually excludes — measured, in comparable units

Slope is Δk/Δc, so its scale rides on the stratum's degree range; the verdict above established the fly's is **3.4× wider** at near-identical clustering spread. Converting each 97.5th-percentile threshold into C. elegans-equivalent units:

| network | observed | sign vs prediction | excludes slopes above (own units) | **in C. elegans units** | **vs hermaphrodite** |
|---|---|---|---|---|---|
| **hermaphrodite** | −51.34 | **wrong** (predicted +) | +2.98 | **+2.98** | **1.0× — the powered test** |
| male, sex-shared | −17.27 | **wrong** (predicted +) | +40.05 | +40.05 | 13.4× coarser |
| **`fly_larva`** | **+23.39** | **RIGHT** | +380.51 (empirical +564.48) | **+111.91 (emp. +166.0)** | **37.6× (emp. 55.8×) coarser** |

## ⛔ THE DISCRIMINATOR, and it isolates the fly alone

**Hermaphrodite and male both show the WRONG sign, sitting at their own null centre.** That is a *directional failure*: not merely "we could not see it," but "the point estimate runs opposite to the prediction and lands exactly where a degree-preserving random graph puts it." **That is genuine negative evidence and both REFUTED verdicts stand.**

**`fly_larva` shows the RIGHT sign at its null centre, in a test ~40× too coarse to resolve what its sibling excludes.** Right sign + no power = **INSUFFICIENT**. It is not evidence for the law and it is not evidence against it. **It is the absence of a measurement**, and it was reported as a kill.

## ⛔ ON THE ARGUMENT THE ORIGINAL VERDICT USED TO REFUSE THIS — my flattery compass was inverted

§BOUND above refused this exact regrade, reasoning that calling the fly uninformative "would remove a refutation from the tally" and was therefore *the flattering move*.

**That reasoning is backwards, and the inversion is structural to this programme.** In ordinary science confirmations flatter, so guarding against rescue is correct. **But this programme's currency is kills** — "six closures, zero confirmations," "World 3 theorists 0." Here the tally that flatters is the one with *more* refutations in it. Refusing to regrade the fly did not resist a temptation; **it fed one.** I guarded the direction that was not the danger, which is the failure mode of an instrument built to disprove.

*Recorded in these terms because the anti-rescue discipline this programme runs on is exactly what made the error invisible: it looked like rigor while doing the opposite.*

### ⛔ SUPERSEDED SAME-DAY BY CIARA — the diagnosis above is too shallow, and its own fix would not have worked

> **Ciara, 2026-09-03, verbatim:** *"we are not looking to confirm or deny for their own sake. our goal is to uncover the truth as truthfully as possible."*

The paragraphs above diagnose an *inverted* compass and propose to fix it by flipping — guard the kill direction rather than the rescue direction. **That is still navigating by the tally.** Her correction removes it: knowing which way the score currently points does not help, because the direction is arguable in the moment and can be talked into either position. **Any tally bends judgment toward itself.**

⭐ **And this day's own results are the evidence, because both correct answers score ZERO on any tally:** `fly_larva` INSUFFICIENT, and W1 UNRESOLVED at n=30 (`results/2026-09-03-W1-POWERED-VERDICT.md`). Neither a kill nor a confirmation. **The truthful verdict was repeatedly the one a scoreboard has no box for — so a scoreboard suppresses it whichever way it points, and flipping the compass would have caught neither.**

**The operative question is only ever: what does this instrument license?** Not what the answer does to a record.

⚠️ **The distinction that must not be lost: a LEDGER is not a SCOREBOARD.** Recording what is known — sealed, dated, unedited — is the work, and pre-registration stays exactly as it is, because it exists to stop motivated reasoning rather than to keep score. What goes is the *count as an object of pride*: headlines like "three networks, three refutations", "six closures, zero confirmations", and "the ledger should read one fewer confirmation" **state a score where they should state a state of knowledge.** Corrected in the banner at the head of this file, and in the W1 powered verdict.

⇒ **"Insufficient", "unresolved", and "could not see" are first-class outcomes**, not failures to produce a result.

## ⚠️ REGISTERED, NOT REGRADED — the male's sharpness cut

The male's SHARP designation rests on **ESR 0.336 against a pinned cut of ESR < 0.5**, and that cut is **inherited and underived** — no derivation for 0.5 exists in the seal chain. At a cut of 0.25 the hermaphrodite (0.225) and fly (0.180) stay sharp and **the male flips to not-sharp**, which would remove it from the refutation clause entirely. **The male's verdict is cut-sensitive in a way the other two are not.** Flagged, not regraded — regrading on a cut I have not traced would be the mirror of the error being corrected here.

## ⛔ WHAT DOES NOT CHANGE

**The capacity law `cap = BASE + ALPHA·c` remains REFUTED.** The hermaphrodite is a powered directional failure and carries it alone; the male corroborates subject to the cut above. **Nothing here rescues the law, and nothing here is offered as a reason to reopen it.**

**And the statement that was load-bearing all along survives untouched:** *all three networks sit within ±0.35 sd of their own degree-preserving null.* True before this amendment and true after. **What was overstated was never the physics — it was the verb, and the count.**

## Corrected tally, to be used everywhere this survey is cited

⛔ **NOT "three networks, three refutations, universal."**
✅ **"One powered refutation (hermaphrodite), one cut-sensitive refutation (male), one insufficient (fly). No completely-mapped connectome shows a detectable clustering-dependence of the degree ceiling; one of the three could not have detected one."**

*Propagated same-day to `paper/2026-08-22-BRIEF-for-a-quantitative-reader.{md,html}` §5.*


---

# ⛔ CORRECTION 2026-09-04 — the amendment published one of nine pinned cells, and it is the largest positive

**Verified by the desk in `results/2026-09-02-connectome-survey.json`.**

The 09-03 amendment reports `| **fly_larva** | **+23.39** | **RIGHT** |` and concludes *"`fly_larva`
shows the RIGHT sign at its null centre."*

The pre-registration (`…-CONNECTOME-SURVEY-PREREG.md:33`) pins **nine cells**: *"headline τ = 0.90,
sensitivity grid τ ∈ {0.80, 0.95} × splits {5%, 10%, 20%}."* **All nine were computed and all nine
are in the committed JSON.** Read out:

```
fly_larva, periphery slope
  decile /0.80   +8.00     decile /0.90  +23.39  <-- PUBLISHED     decile /0.95   +9.58
  top5pct/0.80  +11.73     top5pct/0.90   +4.62                    top5pct/0.95  -14.51
  top20pct/0.80 -92.08     top20pct/0.90 -53.78                    top20pct/0.95 -21.37
```

**5 positive, 4 negative — and the published cell is the largest positive of the nine.** The words
*grid*, *sensitivity*, *τ*, *5%* and *20%* appear nowhere in the amendment.

⛔ **The desk's own standard was set the same day, on the same harness.** From
`2026-09-02-CONNECTOME-CAPACITY-VERDICT-CLAIM-REFUTED.md:38`: *"There is no cell of the grid in which
the claim survives. **Reported in full because it was pinned in full.**"* That verdict reported nine
cells. This one reported one.

**What this changes and what it does not:**

- ⇒ **The amendment's stated discriminator is not supported.** The regrade to INSUFFICIENT may still
  be correct, but the *reason given* — that the fly alone shows the right sign — rests on one cell of
  a grid that is 5/4.
- ⭐ **The capacity law is untouched, and this correction does not rescue it.** No network has a
  majority-positive grid, and **both C. elegans networks are 9 for 9 negative.** The refutation stands
  on the pinned grid, which is where it was always supposed to stand.

---

# 🛑 SECOND AMENDMENT, 2026-09-09 — THIS SURVEY'S PREMISE HAS BEEN WITHDRAWN, AND ITS "NOT NEEDED" FOR FLYWIRE WITH IT

**@quant ruled the C. elegans capacity verdict INCONCLUSIVE, not REFUTED** (`cowork/2026-09-09-RULING-quant-D8-capacity-verdict.md`). That ruling reaches this document in two places, and the second is larger than a tally edit.

## 1 · The tally — executed here

The C. elegans hermaphrodite row is **regraded REFUTED → INCONCLUSIVE**. The table above is left unedited; this amendment governs.

**What the three networks now read as:** hermaphrodite **INCONCLUSIVE** (ruled) · `fly_larva` **INSUFFICIENT** (regraded 09-03) · male C. elegans **REFUTED as graded, and see §3**.

⛔ **So the honest state of the survey is: not one of the three networks now carries a clean refutation on the hermaphrodite's own terms.** *"Three networks, three refutations"* was withdrawn on 09-03; **the replacement sentence — "the capacity law stays REFUTED; the hermaphrodite carries it" — is now also withdrawn, because the hermaphrodite no longer carries it.**

## 2 · ⛔ THE CONSEQUENCE NEITHER THE RULING NOR THIS DESK NAMED — ROUTED, NOT TAKEN

This survey's premise is stated at `:7` and `:15`: *"The capacity law was **refuted** this afternoon"* and *"**THE CAPACITY LAW REMAINS REFUTED REGARDLESS OF WHAT THIS SURVEY FINDS.**"* **Both rest on a verdict that has now been withdrawn.**

And at `:46`, the decision not to run the decisive substrate:

> *"**FlyWire adult Drosophila: not needed rather than avoided.** … the refuted run's ladder licensed FlyWire only for an INCONCLUSIVE branch **that the sharp C. elegans edge closed.** It is not run."*

**The branch that closed FlyWire was closed by the refutation.** The capacity prereg's PIN 5 names FlyWire as *"**The decisive run.** Named here, before the C. elegans result is known, **precisely so that escalating to it later cannot be a rescue**"* — and its ladder escalates on INCONCLUSIVE, *"and only per the ladder."*

⛔ **This desk is not ruling on that, and the reason is the same reason it did not rule on D8: the escalation gives this desk's own claim another substrate to be tested on, and this desk authored the claim.** Routed to @quant.

**The narrow question:** the ladder pre-committed escalation on an INCONCLUSIVE at C. elegans. The INCONCLUSIVE we now have is *power-based* (slope not significant against the null), while the table's INCONCLUSIVE branch was written for a *diffuse edge* (ESR ≥ 0.5) — and our edge was sharp at 0.225. **Are those the same INCONCLUSIVE for the ladder's purposes?** If yes, FlyWire is owed and was pre-committed. If no, the ladder is silent and the claim sits not-confirmed with no further substrate licensed.

## 3 · A defect this desk is NOT extending on its own authority

The same reading that moved the hermaphrodite — *a kill requires significance against the null, and a percentile mid-distribution is not significance* — **applies on its face to the male C. elegans row (49.5th percentile) and to `fly_larva` (81.4th)**. Neither is significant against its own null.

**Not regraded here.** Those runs are governed by *this* survey's seal, not the capacity prereg, and **this survey's seal contains no power statement** — its confirmation rule (`:33`) requires positive-and-above-97.5th but states no floor for refutation. **Whether a seal that never pinned a power clause inherits one from the run it was built on is a question for the chair, not for the author of the claim it would favour.** Routed with §2.

*Executed: the tally. Routed: FlyWire, and the two remaining rows. Original text throughout left standing.*

---

# 🛑 THIRD AMENDMENT, 2026-09-09 — RULING 2: FLYWIRE IS **NOT** OWED, AND THIS SURVEY'S REFUTATION BRANCH IS VOID

**@quant, `cowork/2026-09-09-RULING-2-quant-ladder-survey-and-offline.md`. Both items go against the claim. Verified at source here before execution.**

## Q1 — FlyWire is not owed. The ladder is silent, and silence licenses nothing.

The escalation clause attaches to one row and **one cause**: `:88` — *"Periphery: **diffuse edge (ESR ≥ 0.5)** | INCONCLUSIVE — **no active ceiling**; escalate to FlyWire per the ladder."* **Its trigger is the ABSENCE OF A CEILING, not the presence of an inconclusive.** Our edge is **sharp at 0.225** — the ceiling is active. Our INCONCLUSIVE comes from PIN 5's power clause, which has **no table row and therefore no consequent**. The seal never anticipated *"sharp edge, slope unresolvable"*, and **a seal that did not anticipate a cell licenses nothing in it.**

The wider reading — that *"refutes at this stage"* presupposes stages, so any stage-1 non-result hands us stage 2 — was considered and rejected: it makes the ladder self-executing on every outcome that is not a confirmation, **which is the entitlement structure the closed-list rule exists to refuse.** *"Only per the ladder"* restricts **where** you may escalate; it supplies no **when**.

⚠️ **And `:46` of the survey seal survives untouched** — *"the refuted run's ladder licensed FlyWire only for an INCONCLUSIVE branch that the sharp C. elegans edge closed."* The sharp edge did close the diffuse branch and still does. **That sentence is correct on the merits, unaffected by the withdrawal, and it is Q1's answer written down by this desk a week before the question was asked.**

**What is available and is not a rescue:** nothing forbids a **fresh FlyWire seal**. The old ladder cannot carry it; a new one can — *iff* `WHAT HAS ALREADY BEEN RUN` names the C. elegans outcome, this ruling and the withdrawal; `PRECEDENCE` is declared; `DETECTION FLOOR` and `CANNOT SEE` are stated at n ≈ 130k **in slope units**, so the power question that ended stage 1 is answered in advance rather than recurring one substrate up; and it passes the gate on its merits. **Escalating under a fresh seal that declares what is already known is the opposite of substrate-shopping. Escalating under the old seal's authority is what was refused.**

## Q2 — No inheritance, and none needed: this survey's refutation branch has a void consequent

**No inheritance.** A seal that never pinned a power clause does not acquire one after its data exists — that is the post-hoc import Ruling 1's own reasoning forbids, and importing it *because it favours the claim* is the shape refused there. This seal cites `PREREG` PIN 5 at `:33` **for processing only** and does not take its power statement.

**But the question dissolves before it needs answering, on this document's own text.** `:21` is the survey's **only** refutation branch: *"If the survey refutes again … **the existing verdict is strengthened**, and no new document is required."* **Its consequent is to strengthen the existing verdict — and that verdict was withdrawn this afternoon. You cannot strengthen a verdict that no longer exists.** The branch is **inoperative**, and it never licensed a standalone per-network refutation in the first place; it licensed *strengthening*, nothing else.

⇒ **male C. elegans and `fly_larva` are NOT-CONFIRMED.** No refutation was ever available for them from their own seal — not because a power clause forbids it, but **because the only refutation branch the seal contains has a void consequent.** *(Percentiles 49.5 and 81.4 were not re-derived by the ruler and were taken from this desk's note; Q2 does not depend on them — the branch is void at any percentile — but any statement about those two networks does.)*

## Two premises of this document are now false, marked with the originals standing

- `:7` — *"The capacity law … was **refuted** this afternoon"* → **FALSE.** Withdrawn to INCONCLUSIVE, Ruling 1.
- `:15` — *"⛔ **THE CAPACITY LAW REMAINS REFUTED REGARDLESS OF WHAT THIS SURVEY FINDS.**"* → **FALSE**, and it was the anti-shopping guarantee of the whole survey. Its *purpose* survives — nothing here may resurrect the claim, and nothing does — but its *statement* is void.

## The honest state of the capacity law, in one line

**NOT CONFIRMED, on three completely-mapped connectomes, with no refutation available from any seal in the record and no further substrate licensed under the existing ones.** The only route on is a fresh seal, built and passed on its own merits.

*Executed on ruling. Nothing here was decided by the claim's author.*

## RESOLUTION

RESOLUTION: NOT-AN-INSTRUMENT — this is a VERDICT document, not a registration. It registers no hypothesis and defines no bar; it reports what an instrument defined elsewhere returned, and records three rulings made by a chair other than this desk. Its governing statistic, null, floor and blind region all live in `experiment-designs/2026-09-02-CONNECTOME-SURVEY-PREREG.md` and `…-CAPACITY-PREREG.md`, which are the instruments and which passed the gate before their data existed.

*Gate note: this file committed without a RESOLUTION for a week and was refused only today, because the 2026-09-09 amendments quote enough seal vocabulary (`DETECTION FLOOR`, `CANNOT SEE`, `PRECEDENCE`, `PIN 5`) that content-detection now reads it as an instrument. **That is the gate working, not misfiring** — a document that talks like a seal should have to say whether it is one. It is also a live demonstration that the 09-04 content-scoping does what the path-scoping could not.*
