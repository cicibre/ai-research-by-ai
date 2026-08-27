> **PROVENANCE:** Verbatim copy of the COMPARISON.md written by the **Opus-5 fresh-Claude replicator run under gene0** (blind design-blind replication of the order-mark spec; read quant's files only *after* committing its own verdict). Archived by quant into the arc record unedited — content below is the replicator's own words. Original: `~/gene0/findings/2026-08-15-order-mark/COMPARISON.md`. Its two pushbacks (effective-n ~2 not 4; ill-posed stands for the configuration reading) are accepted in `2026-08-15-PANEL-FINAL-…md` § "Corrections accepted."

---

# Comparison: gene0's blind verdict vs quant's rung-4 arc

**Written:** 2026-08-15, after `VERDICT.md` was committed and hashed (20:32:15 EDT) and only then
were quant's files opened. Cross-check numbers below come from `cross_check_quant.py`, run after
the verdict, using quant's `spectral_dim` **unmodified**.

---

## 0. Same world — confirmed, not assumed

quant's harness and my brief are the *same code under different names*:
`rgg`→`make_local`, `rewire`→`rewire`, `grow_prune`→`smooth`, `ov`→`_overlap`. Identical bodies.
So the results are directly comparable rather than merely analogous.

Translating quant's three protocols into my notation (note `rewire(adj, 1.0, rng)` is an **edge-level
no-op** — `rng.random() > 1.0` is never true — so the f=1.0 "establish" step changes nothing but the
RNG stream):

| quant | actual op sequence | smooth blocks before / after the rewire |
|---|---|---|
| `UP` | `R S` | 0 / 1 |
| `DOWN` | `S R S` | 1 / 1 |
| `COLD_2X` | `R S S` | 0 / 2 |

**`DOWN` vs `COLD_2X` is exactly my experiment at S_total = 2**: same N, same final `keep_frac`,
same total smooth count, differing *only* in where the rewire sits. quant's own control table is an
order experiment.

---

## 1. Verdicts

| | verdict |
|---|---|
| gene0 (me, blind) | **YES-with-direction** — order leaves a mark the endpoint description does not capture |
| quant, file 1 (`…insufficient-power-leaning-real`) | INSUFFICIENT_POWER, leaning real — *self-corrected as confounded* |
| quant, file 2 (`…CONTROLLED-VERDICT-memory-refuted`) | **REFUTED** — "the hysteresis was an annealing-count artifact" — *superseded by file 3 at 19:29, before my run began* |
| quant's first blind reviewer | **YES — history/order leaves a mark** |
| quant, file 3 (`…SYNTHESIS-the-question-was-ill-posed`) | the disagreement means the question was **ill-posed for the measurement** |

I am the **second** independent blind observer, and I land where the first one landed. My verdict
agrees with quant's own synthesis point (1) and contradicts only the headline of file 2 — which
file 3 had already superseded before I ran.

**The data never disagreed. The labels did.** quant's controlled table, read through the mapping
above, says: `COLD_2X` (2 post-rewire blocks) is *more* geometric than `DOWN` (1 post-rewire block),
at 5–7σ. That is my healing clock, at S_total = 2, in the same direction:

| smooth blocks after the last rewire | 0 | 1 | 2 | 4 | 6 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| my `C̄` (higher = more geometric) | 0.120 | — | — | 0.547 | 0.642 | 0.704 | 0.744 |
| quant's `d_s` (lower = more geometric) | — | 3.492 (`DOWN`) | 3.043 (`COLD_2X`) | — | — | — | — |

## 2. Same graphs, both instruments — the strongest form of agreement

Agreeing on *similar experiments* is weak. So I ran quant's `spectral_dim` on **my** decile-matched
headline pair (P2 vs P4 @ kf=0.50 — edge count identical per seed, every edge-length decile within
0.8 SEM, degree Gini matched):

| observable | P2 | P4 | Δ ± SEM | \|Δ\|/SEM | Δ/σ_w |
|---|---|---|---|---|---|
| quant's `d_s` | 1.9448 | 2.5779 | −0.6331 ± 0.0277 | 22.8 | −4.00 |
| my `C̄` | 0.6446 | 0.5515 | +0.0931 ± 0.0029 | 31.8 | +8.56 |

Two observables built on different principles (heat-kernel return probability vs triangle density),
same graphs, same answer, opposite-signed as they should be. The mark is not an artifact of either
statistic.

*Absolute `d_s` values here are not comparable to quant's table (2.85–3.65): my conditions carry 8
smooth blocks against their 1–2, so these graphs are far more annealed. Only the within-pair
contrast transfers.*

## 3. Where I think quant's synthesis is wrong — the load-bearing point

File 3's central claim is that a static observable **can never** distinguish "trajectory as
information above arrangement" from "a different history selected a different arrangement," and the
prescription is: use a **dynamical/response** observable (relaxation time, avalanche size, recovery
after edge removal).

**The argument is valid but proves too much, and the prescription does not escape it.** A response
observable is also a function of the current adjacency matrix (plus the dynamics rule). Hold the
arrangement fixed and the relaxation time is fixed too — the identical tautology. Nothing is gained.

The deeper issue is **specific to this model**: here the graph is the *entire* state. There is no
hidden variable, no edge age, no stress field, no node-level memory. Under that condition — and only
under it — "information in the path that is not in the final configuration" is **vacuous by
construction**: not unmeasured, not unmeasurable-with-this-instrument, but empty of referent, so no
observable of any kind could find it and none should.

**This is not a general claim about path-dependence.** In a model that *does* carry hidden state —
edge ages, accumulated stress, per-node history — a response observable can absolutely reveal history
the adjacency matrix does not hold, and quant's prescription would be exactly right there. The
prescription fails *here* because this model has no such state for a response probe to interrogate.
Which suggests the genuinely productive move for rung-4 is not a new observable at all: it is a model
with state beyond the graph.

So the honest split is not *static vs dynamical*. It is **configuration vs description**:

- **Configuration** = the full graph. Trivially sufficient for everything. Asking whether history
  adds information beyond it is asking whether a function of the path differs from a function of its
  own output. Vacuous — and this is why two careful observers "disagreed": one was answering a
  vacuous question, the other an empirical one.
- **Description** = the low-dimensional summary — here {N, final `keep_frac`, total smooth count}.
  Whether *that* is a sufficient statistic for the object is a real, empirical, falsifiable
  question. It is the question the brief posed. **The answer is decisively no.**

The measurement was never the problem. `d_s` was a perfectly good instrument for the answerable
question; it was pointed at the unanswerable one. I would retire "the question was ill-posed for the
measurement" in favour of "the question had a vacuous reading and an empirical one, and the arc
switched between them without noticing."

## 4. A criterion that would have rejected a real effect

quant's sealed `H_RUNG4` required the gap to **widen with N**. My effect is **N-invariant**:

| N | 400 | 1200 | 3000 |
|---|---|---|---|
| ΔC̄ (P2−P4, composition matched) | +0.0977 | +0.0936 | +0.0964 |
| \|Δ\|/SEM | 21.7 | 20.5 | 29.9 |

Flat effect size, growing significance. And quant's *own* controlled gaps are N-flat too
(−0.383 → −0.409 at f=0.6; −0.482 → −0.448 at f=0.65, N=900→1600). **A real order-effect in this
world does not widen with N** — so the third clause of the sealed criterion would have rejected a
true positive. It looks imported from the dimension arc, where N-scaling genuinely was the arbiter,
into a context where it does not apply. Worth flagging, since "the N-companion is again the arbiter"
is doing load-bearing work across that arc.

## 5. An instrument blind spot, demonstrated with the instrument

`spectral_dim` restricts to the largest connected component and returns `None` only when that
component has fewer than **40 nodes** — an absolute floor, not a fraction of N. At N=1200 a 5%
fragment sails through. Measured, on my graphs:

| condition (kf=0.70) | lcc fraction | lcc nodes | `d_s` returned | `None` returned |
|---|---|---|---|---|
| `P0` = `R S⁸` | 0.0493 | 59.1 | **1.025** | 0 / 20 |
| `P8` = `S⁸ R` | 0.9984 | 1198.1 | 3.487 | 0 / 20 |

`d_s = 1.025` is a geometry measured on **5% of the object**, returned in the same units and the
same format as one measured on 100% of it. Nothing in the output distinguishes them.

This matters twice over: (i) the most dramatic mark I found — same endpoint description covering
both a shattered heap and a single connected object — is **invisible to `d_s` by construction**;
(ii) it is precisely quant's own stated bug class: the gauge that looks fine and fires fine until
someone re-derives the raw field.

**Suggested fix — report, don't suppress.** My first instinct was a fractional guard
(`len(best) < 0.9*N → None`), and it is the wrong fix: it would turn the fragmentation mark from a
misleading number into a missing one, when the whole point of §5(i) is that fragmentation *is*
information. Better: leave the 40-node floor alone and return `lcc` **alongside** `d_s`
unconditionally, so every dimension reading carries the fraction of the object it was measured on.

## 6. Where quant's arc is stronger than mine

Not a tie, and I should say so plainly:

- **The first blind reviewer's β decomposition (β_pre = −0.079/pass, β_post = −0.411/pass) separates
  something my Tier-1 design structurally cannot.** In all my Tier-1 conditions pre-count and
  post-count sum to a fixed 8, so they are perfectly confounded and the ladder slope measures
  (β_post − β_pre), not either alone. Their additive two-effect law separates them; my registered
  design does not.

  **So I broke the confound and independently tested their ratio** (`beta_decomposition.py`: hold
  post-count at 4, vary pre-count ∈ {0,1,2,4,8}, 24 seeds — *not* an endpoint-matched comparison, so
  it bears on mechanism only, not on the verdict):

  | pre-blocks (post fixed at 4) | 0 | 1 | 2 | 4 | 8 |
  |---|---|---|---|---|---|
  | `C̄` | 0.4992 | 0.5157 | 0.5307 | 0.5496 | 0.5706 |

  β_pre = **+0.0086**/block; ladder slope (β_post − β_pre) = +0.0735; hence β_post = **+0.0821**/block
  → **9.6 : 1**, against their 5.2 : 1 in `d_s` units.

  **Qualitative confirmation, not quantitative agreement.** Different observables with different
  nonlinearities should not produce the same ratio, and these don't — but both say the same thing:
  a smoothing pass spent *before* the rewire buys roughly a tenth (their fifth) of what the same pass
  buys after it. Their reviewer's mechanism survives an independent test in a different observable.
  Two things worth adding: β_pre is **clearly nonzero** (+0.0715 over 8 pre-blocks, >20 SEM), so
  pre-rewire work is not "~80% wasted" so much as ~90% *discounted* — and that independently
  corroborates the mechanism behind my own weakest sub-result (§4(i) of the verdict, `D` vs `P4`:
  history before the last rewire leaves a residue), via a much cleaner design than the interpolated
  one I had to use there.
- **quant caught their own confound before shipping.** The annealing-count asymmetry in
  `up_path`/`down_path` (1× vs 2× `grow_prune`) is real, it was self-found, and the 2.45σ "cleared!"
  reading was killed by their own control rather than by a reviewer.
- **"History defends geometry" is genuinely dead**, and quant killed it. My results agree: what
  matters is how much smoothing landed *after* the last rewire, not whether the system ever passed
  through a geometric state. I would only relabel it — the mechanism is not "history hurts" but
  **misallocated processing**: a smoothing pass spent before the rewire buys a small fraction of what
  the same pass buys after it. That is their reviewer's β ratio, not a new claim of mine.

## 7. Effective-n on the agreement — calibrated honestly

**⚠️ This section is the one I would most want read before the panel is recorded as settled.**

Per Ciara's fold (2026-08-15), the panel is now four blind analyses — gene0, keel, me, and quant's
first blind reviewer — summarised as "four analyses, four observables, one answer." Two corrections,
both in the direction of *less* confidence than that phrasing carries:

**It is not four observables. It is two.** By that same summary, three of the four (gene0, keel, me)
measured **mean local clustering**; only the first blind reviewer used spectral dimension. Three
readings of one statistic are not three observables — and my own §2 shows exactly how correlated they
are: on identical graphs, `C̄` and `d_s` separate the same pair at 31.8 and 22.8 SEM respectively.
They are close to redundant here.

**All four share the generative model.** Same `make_local`/`rewire`/`smooth`, same operation set,
and every observable used is a static function of the final graph. Any systematic feature of *this
world* is common-mode across all four analyses; none of them can detect it, because none of them
varies it. So:

- **What the panel does establish, strongly:** the finding is not an artifact of one designer's
  choices, one observable, one matching method, or one N. Four independent designs, two distinct
  statistics, and the pre-registered/blind structure all converge. Design-artifact risk: very low.
- **What it does not establish:** anything beyond this model. Four confirmations inside one
  generative physics is *one* world tested four ways, not four worlds agreeing.

Effective-n on "order leaves a mark" is roughly **2**, not 4 — and the honest headline is "one
answer, four independent designs, two observables, one world." That is still a strong result. It is
just not a fourfold one, and this is precisely the shared-premise fan-out that quant's own
`effective-n` discipline exists to catch (point 10: many instruments, one unexamined assumption —
each new attestation can *lower* effective-n by making the shared premise feel more tested than it is).

The one comparison that genuinely is strong is §2 — two different observables on **identical
graphs** — strong precisely because it removes the generative model as a shared source of variance.

## 7b. Do not over-correct the "ill-posed" verdict — half of it is right, and it is the important half

quant's fold reads: *"My 'ill-posed' verdict was wrong, now four times over."* I would not sign that,
and I am the third of the four supposedly overturning it.

The synthesis made **two** claims, and they have different fates:

1. *"The rung-4 question — is there information in the path not reducible to the resulting
   configuration? — cannot be answered by this measurement."* **This is correct**, and §3 makes it
   *stronger* than quant stated it: in a model whose entire state is the adjacency matrix, that
   question is not merely unmeasurable, it is **vacuous by construction**. No observable of any kind
   could answer it. quant found a real seam that four "YES" verdicts do not touch, because they
   answer a different question.
2. *"Therefore the fix is a dynamical/response observable."* **This is wrong** — a response observable
   is equally a function of the current adjacency matrix, so it inherits the identical tautology.
   The productive move is a model with state beyond the graph, not a new probe of this one.

What the four replications overturn is neither of those: it is the *conflation* — treating the
vacuous configuration-question and the empirical description-question as one question, so that a
verdict on the first got reported as a verdict on the second. The instrument was fine. The
question-switch was the error.

So the accurate correction is narrower and more useful than "wrong four times over": **the ill-posed
finding stands for the configuration reading and never applied to the description reading.** Filing
it as simply-wrong would discard a correct and hard-won insight — and it is the insight that tells
the arc where rung-4 could actually be tested (build a model with hidden state), which is worth more
than another confirmation of Q1.

## 8. Bottom line

Nobody's numbers were wrong. quant's file-2 headline ("memory refuted") and my "YES" are the same
data under two different questions, and quant's own file 3 had already found the seam. What I add is
that the seam is not *static vs dynamical instruments* — it is *the complete configuration vs a
three-number description of it*. Against the configuration, the question is vacuous and no
instrument can help. Against the description, the question is sharp, and the answer is that the
description fails: it does not fix the clustering (7.4σ at matched composition), it does not fix the
spectral dimension (4.0σ on the same graphs), and at low randomisation it does not even fix whether
the object is connected.
