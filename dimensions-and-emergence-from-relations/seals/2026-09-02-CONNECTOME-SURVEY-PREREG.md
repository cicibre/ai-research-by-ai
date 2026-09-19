# CONNECTOME SURVEY — is the C. elegans failure UNIVERSAL, or is that network special?

**chamberlain, 2026-09-02 ~16:1x EDT, at Ciara's direction ("look for another network to test on"), sealed BEFORE any degree–clustering relationship is computed on any network in the list.**

## ⛔ WHAT THIS IS, AND WHAT IT IS NOT

The capacity law `cap = BASE + ALPHA·c` was **refuted** this afternoon in the C. elegans hermaphrodite connectome (`results/2026-09-02-CONNECTOME-CAPACITY-VERDICT-CLAIM-REFUTED.md`, commit `9b80563`). Running further networks immediately after a refutation is **substrate-shopping** unless it is structured so that shopping is impossible.

⇒ **The question is therefore NOT "does the law hold." It is: is the C. elegans failure universal, or is that network special?** That is a real question with a real answer either way, and it is the only question this survey asks.

Three structural devices make shopping impossible, and all three bind:

1. **The list is fixed here, in advance, and closed.** No network may be added after any result is seen.
2. **Every network on the list is run and reported**, including any that fails, is degenerate, or is uninformative. There is no stopping rule.
3. ⛔ **THE CAPACITY LAW REMAINS REFUTED REGARDLESS OF WHAT THIS SURVEY FINDS.** See the branch pins below. Nothing here can resurrect it.

## ⛔ THE TWO BRANCHES, PINNED NOW — including the one I would rather not have to handle

**Pre-registered expectation, stated honestly: the law fails again.** After C. elegans, that is the correct prior and it is written down so a second failure cannot be presented as a bold prediction confirmed.

- **If the survey refutes again** (periphery slope ≤ 0 or inside the null band, sharp edge): the existing verdict is **strengthened**, and no new document is required beyond this survey's own verdict. **No new claim may be built from a second negative.**
- ⛔ **If any network shows a positive periphery slope above the 97.5th percentile of its own null:** the capacity law **stays refuted in the record.** That result does **not** resurrect it. It becomes a **new and separate question** — *what distinguishes that network* — which requires **its own stake, its own prior-art check, and its own seal** before anything is claimed anywhere. **A positive here is a question, not a finding.**

*This asymmetry is pinned now, before any result, precisely because the temptation to resurrect will be at its maximum exactly when my guard is lowest.*

## THE LIST — closed

| # | network | source | why it is in |
|---|---|---|---|
| **1 (primary)** | **`fly_larva`** — *Drosophila melanogaster* larval brain, N=2,956 | Winding et al., *Science* 379 eadd9330 (2023) | **"A complete synaptic map of the brain connectome."** Independent species, independent lab, independent EM reconstruction, ~10× C. elegans. The strongest available independent replication. |
| **2 (secondary)** | **`celegans_2019` male**, restricted to the sex-shared neuron set | Cook et al., *Nature* 571 (2019), `_corrected` | Holds the reconstruction pipeline and the source fixed while changing the animal. Controls whether a failure is a property of *this reconstruction* or of *this nervous system*. |

**Processing is identical to the refuted run** (`PREREG` PIN 5): symmetrise, binarise, drop self-loops, undirected simple graph. Same statistics: decile split (rank by degree descending, ties by index ascending, HUB = first ⌈0.10n⌉), upper-quantile regression of `k` on `c`, **headline τ = 0.90**, sensitivity grid τ ∈ {0.80, 0.95} × splits {5%, 10%, 20%}, ESR tightness diagnostic with the pinned cut **ESR < 0.5 ⇒ sharp**, and the degree-preserving double-edge-swap null. Confirmation still requires slope **positive AND above the 97.5th percentile** of that network's own null.

## ⛔ THE EXCLUSIONS — four networks refused on documented grounds, before any was opened

These belong here as prominently as the inclusions, because they are the evidence that the list was constrained by a **criterion** (completely-mapped, synapse-level, cells-not-regions, observed-not-inferred) rather than by what happened to be available.

| refused | reason |
|---|---|
| `fly_hemibrain` (N=21,739) | A **hemibrain** — a volume, not a whole brain. Reconstruction is dense but **truncated at the volume boundary, which systematically severs edges.** That is precisely the coverage artifact that deflates local clustering, and it is the same ground on which the `_synapse` variants were refused in the first run. **Size is not completeness.** |
| `macaque_neural` (N=47) | Nodes are cortical **regions, not cells**, and edges are **collated from published tract-tracing reports** — incomplete by construction. |
| `budapest_connectome` (N=1,015) | Edges are **inferred from diffusion tractography**, not observed; and its `20k`/`200k`/`1m` variants are **threshold choices**, i.e. an engineered edge set — the exact criterion `NOVELTY-BOUNDARY` says to avoid. |
| `celegansneural` (N=297) | The older White/Watts–Strogatz reconstruction of **the same animal** already tested. A **pseudo-replicate**, not an independent network. |

**FlyWire adult *Drosophila*: not needed rather than avoided.** The larval brain is already a *complete whole-brain* connectome; the adult adds scale without adding completeness, and the refuted run's ladder licensed FlyWire only for an INCONCLUSIVE branch that the sharp C. elegans edge closed. It is not run.

## ⛔ SWAP-DEPTH GATE — with the agreement criterion pinned BEFORE it is evaluated

`fly_larva` has |E| ≈ 96,000; the refuted run's 100·|E| swap depth × 1,000 replicates is ~6.4 hours. **Replicate count drives the percentile resolution and is held at 1,000; only swap depth is reduced, to 10·|E|** (standard practice for degree-preserving randomisation).

That reduction is **not asserted — it is gated on a cross-validation with a tolerance fixed here, before it is run.** The C. elegans hermaphrodite periphery null is re-run at 10·|E| and compared to the already-published 100·|E| values (mean −56.90, sd 30.55):

- ⛔ **PASS** if |mean₁₀ − mean₁₀₀| ≤ 0.25 · sd₁₀₀ **and** |sd₁₀/sd₁₀₀ − 1| ≤ 0.20.
- ⛔ **FAIL ⇒ `fly_larva` runs at 100·|E| regardless of runtime.** The gate decides the depth; convenience does not.

**The gate's result is reported in the survey verdict, not buried in JSON** — it is the reason a reader should trust the `fly_larva` null at all. The male C. elegans network is small and stays at 100·|E|.

## Substrate specifics — stated so the differences from the refuted run are on the record, not inherited by accident

- **`fly_larva`:** all 2,956 nodes are neurons (a brain connectome; no muscle or end-organ nodes), so **no cell-type filter is applied.** Edge `etype` metadata (`ad`/`aa`/`dd`/`da`) is **discarded by the binarisation**, as is `count`. **4 nodes are isolated after binarisation and 346 carry a blank `cell_type`.** The harness convention `c := 0.0 for k < 2` and *keep the node* is unchanged from the refuted run — but C. elegans had **zero** isolated neurons, so this case is new and is named here deliberately rather than handled silently.
- **`celegans_2019` male:** ⚠️ **the male file's `node_type` is demonstrably coarse** — it types 223 of 575 nodes as `MOTOR NEURONS`, which on the hermaphrodite's own numbers must be absorbing the ~95 bodywall muscles and ~21 end organs. That is the *same defect* that disqualified the gap-junction file's typing in the refuted run, so **the male's labels cannot be used to derive a neuron set.** (It also spells the sensory category `SENSOSRY NEURONS` and uses `SEX-SPECIFIC` rather than `SEX-SPECIFIC CELLS`.)
  ⇒ **Discretion-free rule, adopted instead of hand-curating a male cell list:** the male neuron set is **the intersection of the hermaphrodite's verified 300-neuron set with the names present in the male files.** Fully deterministic, no judgement, no post-hoc curation.
  ⚠️ **Limitation, stated up front:** this covers the male's wiring among **sex-shared neurons only** — the ~93 male-specific neurons are excluded because they cannot be identified without exactly the hand-curation this survey exists to avoid. It is therefore a test of *a different wiring among the same cells*, which is still an independent network but is **not** the male nervous system entire.

## ⚠️ Bounds carried forward, unchanged

The prior-art negative that makes any of this interesting remains **four searches, one engine, in English, in our vocabulary** — weak evidence of absence. And the refuted run's bound stands: its null spread (sd ≈ 30.5) **could not exclude a small positive contribution**, only a large one. Neither bound is offered as a reason to expect a different answer here.

---

*Sealed before any degree–clustering relationship was computed on `fly_larva` or on the male network. Only node/edge counts, degree summaries, and timing were measured beforehand, in order to write the swap-depth gate.*
