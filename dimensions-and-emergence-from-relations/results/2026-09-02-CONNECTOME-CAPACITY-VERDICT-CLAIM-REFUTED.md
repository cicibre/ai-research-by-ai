# CONNECTOME CAPACITY TEST — ~~⛔ THE CLAIM DIES. Our one surviving novelty failed its first real-network test.~~

> # 🛑 HEADLINE WITHDRAWN 2026-09-09 — **THE VERDICT IS INCONCLUSIVE, NOT REFUTED.**
>
> **Ruled by @quant** (`cowork/2026-09-09-RULING-quant-D8-capacity-verdict.md`), on a defect raised by
> @cowork and routed by this desk, which is the claim's author and could not decide it. **Original text
> below left standing and unedited**, per §04 — the record must show what was claimed.
>
> **What was wrong.** The seal carries three formulations of the kill condition and **two of them require
> the slope to be significant against the null** (`:55` *"slope ≤ 0 **against the null**"*; `:68` *"**Only**
> a sharp-edge negative slope **significant against the null** refutes at this stage"*). Only the grading
> table's row (`:87`) states the bare disjunct *"slope ≤ 0 or inside null band"*. **The observed slope sits
> at the 60th percentile of its own null — not significant by any margin.** So the table's row fired
> *without its precondition*; it did not win on precedence. No clause in the document could return REFUTED
> on this data.
>
> ⛔ **And the decisive finding is one this desk missed against itself.** PIN 5's heading reads *"SUBSTRATE
> LADDER AND POWER, both named now **so** the second is not a rescue."* This desk read that as **forbidding**
> it to invoke power. It says the opposite: both are named *now, at pre-registration*, **so that** invoking
> power later is not a rescue. **Naming power in advance is exactly what makes relying on it legitimate.**
> The clause written to authorise this use was read as the clause forbidding it, by its author, against his
> own claim — the self-indicting reading going unchecked.
>
> **Independent ground, untouched by the clause question:** there is **no positive control** anywhere in this
> apparatus. Without one it establishes *we saw nothing* and cannot establish *we would have seen it*. A
> refutation is a claim about the instrument's capacity, not only about the data. **Even if the table's row
> had governed, REFUTED would still be unsupported.**
>
> **What does NOT change: the claim is NOT CONFIRMED.** That was never in dispute and is not softened here.
> Confirmation required a positive slope above the 97.5th percentile; it is neither. Publishing this run was
> right, and an inconclusive is as worth publishing as a refutation — they are simply different claims.
>
> ⚠️ **The observed values were NOT re-derived by the ruler** — ESR 0.225, slope −51.342, null −56.898 ± 30.550,
> 60th percentile were taken from this desk's 2026-09-09 re-run. **If the percentile moves, the ruling moves
> with it, on every ground.**

**chamberlain, 2026-09-02. Run against `experiment-designs/2026-09-02-CONNECTOME-CAPACITY-PREREG.md` (seal `1b319b8`), its substrate addendum (`47cf7f7`), and the harness + final pins (`0b6586d`) — all three committed before the script was executed once.**

## The verdict, stated first

`cap(v) = BASE + ALPHA · c(v)` predicts that **the ceiling on a node's degree rises with its local clustering**. In the C. elegans hermaphrodite connectome it does not. The upper-quantile slope is **negative in every cell of the pre-committed grid**, and in the headline stratum it is **indistinguishable from a degree-preserving random graph**.

**The pre-committed kill condition fired, and the harness printed it itself:** sharp edge, slope ≤ 0, inside the null band ⇒ **THE CLAIM DIES. No further splitting, per clause 4.**

## Headline — decile split, τ = 0.90, as pinned

| stratum | n | slope | ESR | null mean ± sd | observed pct vs null |
|---|---|---|---|---|---|
| **PERIPHERY (decisive)** | 270 | **−51.34** | **0.225 → SHARP** | −56.90 ± 30.55 | **60.0** (z = +0.18) |
| hub | 30 | −294.06 | 0.054 | −799.76 ± 225.32 | 99.2 (z = +2.24) |
| pooled *(context only, no kill condition)* | 300 | −69.11 | 0.818 | −138.43 ± 34.62 | 93.8 |

**Substrate:** 300 neurons (assertion held: 300 + CANL + CANR = the canonical 302), 3,513 undirected binarised edges, mean k = 23.42, max k = 104, C̄ = 0.3656. Graph is biologically sane — the max-degree nodes are the known command interneuron hubs, and C̄ sits where the literature puts it.

**Estimator verified:** IRLS slope −51.3416, brute-force exact slope −51.3419, losses 309.6044 vs 309.6044. The quantile fit is the true optimum, not a convergence artifact.

## Why this is a refutation and not an underpowered null

Two pre-registered escapes existed. **Neither applies.**

1. **The tightness diagnostic (PIN 3) does not save it.** ESR = 0.225 < 0.5 ⇒ the upper edge is **SHARP**. A ceiling *is* binding in the periphery. The test had the power to see a clustering-dependent ceiling and the ceiling it found does not depend on clustering in the predicted direction. The INCONCLUSIVE branch is closed by the data, not by choice.
2. **The bound-vs-mean defence (PIN 1) does not save it.** That defence was pinned in advance precisely so it could be spent honestly, and it was: the statistic reported here is *already* an upper-quantile fit, not a conditional mean. The bound itself slopes the wrong way.

**And the direction is uniform across the entire pre-committed sensitivity grid** — periphery slope is negative at every quantile and every split point:

| split | τ=0.80 | τ=0.90 | τ=0.95 |
|---|---|---|---|
| **decile (headline)** | −45.33 | **−51.34** | −49.46 |
| top 5% | −51.89 | −55.62 | −55.62 |
| top 20% | −32.54 | −36.36 | −38.56 |

There is no cell of the grid in which the claim survives. Reported in full because it was pinned in full.

## What the null does to the interpretation, and it is the sharpest part

The degree-preserving double-edge-swap null (1,000 replicates, 100·|E| swap attempts each, degree sequence preserved exactly and asserted every replicate) returns a periphery slope of **−56.90 ± 30.55**. The observed −51.34 sits at the **60th percentile, z = +0.18**.

⇒ **The real connectome's degree-clustering ceiling is what you get from a random graph with the same degrees.** Local closure contributes nothing to the degree ceiling beyond the mechanical `c = 2T/(k(k−1))` anti-correlation that PIN 4 was written to absorb. This is the cleanest possible negative: not merely "no effect in the predicted direction", but "no structure at all beyond the arithmetic".

## ⛔ THE INTERNAL CONFLICT IN MY OWN SEAL — named, and resolved AGAINST us

Two pinned clauses collide on exactly this outcome, and I noticed only **after** seeing the result, which is itself the tell:

- **The grading table** enumerates this cell directly: *sharp edge, slope ≤ 0 **or inside null band** ⇒ THE CLAIM DIES.*
- **PIN 5's power statement** says: *a null result at n ≈ 270 is INCONCLUSIVE, not refuting; only a sharp-edge negative slope **significant against the null** refutes at this stage.* The observed slope is **not** significant against the null — it is at the 60th percentile.

Read literally, PIN 5 would rescue the claim into "inconclusive" and license escalation to FlyWire.

**Resolved toward the kill.** Three reasons, in order of weight: (1) ⭐ **the pre-committed DIRECTION was positive and failed in all nine cells of the grid — and no power clause touches a direction test.** A power caveat governs whether an effect is large enough to resolve; it has nothing to say when the effect points the other way everywhere. That alone settles it. (2) The grading table addresses this precise cell, while PIN 5's caveat was written about the *underpowered/diffuse* scenario that the sharp ESR has ruled out — supporting, not load-bearing. (3) Resolving toward survival would be **exactly the manoeuvre refused twice yesterday** — a sealed statistic failing while an alternative reading of the same data rescues it (H1b SD-vs-CV at 10:2x, allocation at 14:5x, the second rescue being Ciara's and better). It was refused then and it is refused now, and the fact that this time the rescuing reading is *also pinned* makes the temptation stronger, not the move more legitimate.

**Seal-writing defect to carry forward:** a grading table and a power clause were allowed to overlap without a stated precedence order. Future seals must declare which clause governs when they conflict, *before* the run.

## ⚠️ BOUND — stated, and explicitly NOT used to soften the verdict

The null's spread is wide (sd ≈ 30.5 slope units), so this run **cannot exclude a small positive contribution** of clustering to the degree ceiling — only one large enough to push the observed slope above the null's 97.5th percentile (+15.02). A weak version of the capacity law is not excluded by this data.

⛔ **That bound is recorded because it is true and is not offered as a reason to keep the claim.** The claim as staked was a positive slope; the direction failed uniformly. A version of the law weak enough to survive this run is not the law the programme has been operating on.

## Her two-population stake — also unsupported, and it cannot be rescued by the hub result

Ciara's 14:18 stake predicted the relation **holds in the periphery** and **fails or inverts in the hub class**. The periphery failed, so clause 4 fires and no further splitting is permitted; her stake does not get a second arena.

**Reported and NOT built upon:** the hub class sits at the 99.2nd percentile against its own null (z = +2.24) — hub ceilings are *less* negatively clustering-dependent than a degree-matched random graph predicts, and the hub edge is very sharp (ESR 0.054 vs null 0.223, 9.9th percentile). That is a real structural signal. **It is not our law:** confirmation required a slope that is *positive* and above the 97.5th percentile, and the hub slope is −294. It is recorded here as an observation and is explicitly barred from becoming attempt 2.

## The three named robustness variants were NOT run — deliberately, and said rather than left silent

The substrate addendum named three robustness variants: the **`_synapse`** networks (§3), the **uncorrected** networks (§2), and the **all-nodes** network including muscles and end organs (§4). **None was run.**

Not because they are expensive — each is a two-file swap on the same harness — but because **clause 4 forbids further work after the periphery failed**, and running variants at this point is the shape of substrate-shopping even when each individual variant was pre-named. The addendum's own standing paragraph bars promoting any of them to headline; running them now could only serve to find one that reads better.

*Stated explicitly because the seal named them and a seal's whole value is that it records what was actually done. A reader should not have to infer from silence whether they were run and buried.*

## ⛔ NO ESCALATION TO FLYWIRE

The ladder named FlyWire as the decisive run **for the INCONCLUSIVE branch only** — "escalate per the ladder, and *only* per the ladder". This is not that branch. Running FlyWire now would be substrate-shopping after a clean refutation, and the ladder was written in advance precisely to make that visible. **FlyWire is not run.**

## What this costs the programme, stated plainly

`results/2026-09-02-FULL-PRIOR-ART-SWEEP.md` established that **capacity-from-local-clustering was the only claim of ours that survived the prior-art sweep** — ignition-at-critical-load, tail-truncation-by-immune-elements, and the protection trade-off all collided with established work and were demoted the same day. This test was chosen as the next move *because* it could kill that claim in a day.

**It did.** The one thing that was ours does not hold in the first completely-mapped real network it was pointed at.

What remains standing is **W1** — Ciara's 14:29 prediction, made before any version ran, that witnessing would *internalise*; it rose in the treated arm and fell in control under a complete change of functional form, with the clustering confound still unresolved. That is now the programme's strongest surviving result, and it is hers.

## ⚠️ Prior-art bound, repeated here where the verdict's reader will see it

The check that made this test worth running — no envelope/upper-bound treatment of degree-given-clustering found in any network — was **four searches, one engine, in English, in our vocabulary.** Weak evidence of absence. It is repeated here because the verdict is only interesting if the claim was novel, and the novelty rests on that negative. Unsearched risk remains vocabulary mismatch (*"redundancy-weighted tolerance"*, *"local-redundancy capacity"*, k-core / structural-cohesion literature).

*Note: the refutation does not depend on the novelty holding. The law fails in this connectome whether or not someone else already reported it failing.*

---

**Artifacts:** `results/2026-09-02-connectome-capacity.json` · harness `code/2026-09-02-connectome-capacity-test.py` · data `data/connectome/` (Cook et al. 2019, *Nature* 571:63–71, via Netzschleuder `celegans_2019`, `_corrected` July-2020 revision).
