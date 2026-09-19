# ADDENDUM to the connectome capacity prereg — the four sub-network choices, pinned before download

**chamberlain, 2026-09-02, immediately after sealing `2026-09-02-CONNECTOME-CAPACITY-PREREG.md` (commit `1b319b8`) and before any connectome file is on disk.**

The C. elegans source (Cook et al. 2019, *Nature* 571:63-71, via Netzschleuder `celegans_2019`, canonical at wormwiring.org) ships **twelve** sub-networks. That is four researcher degrees of freedom the base prereg did not close. They are closed here, each on a documented ground that is independent of the `k`–`c` relationship, **which has not been computed and cannot be, because nothing is downloaded yet.**

Choices were made from the dataset's own *description text and node/edge metadata only* — never from a summary statistic that could indicate which way the test would come out.

## 1. Sex: **hermaphrodite**

The hermaphrodite somatic nervous system is the canonical reference C. elegans connectome and the substrate of essentially all prior network analysis of this organism (Watts–Strogatz 1998; Varshney et al. 2011; Towlson et al. 2013 rich-club). Choosing the standard reference removes the option of preferring whichever sex flatters. **Male: not analysed, and not available as a fallback.**

## 2. Version: **`_corrected`**

Per the dataset description: *"The '_corrected' networks correspond to corrected versions of the network made available in July 2020."* Using the most accurate published map is the principled choice, and it is made here without knowing whether correction helps or hurts. **The uncorrected variant is a robustness check only and cannot become the headline.**

## 3. Edge classes: **union of chemical + gap junction**

Our law makes no distinction between kinds of relation — in the harness an edge is an edge, and capacity is set by the closure of a node's relations *as such*. Restricting to one synapse class would arbitrarily sub-select the relational map. The union is also the standard "C. elegans neural network" of the literature.

**Not used: the `_synapse` variants.** The description states these *"[do] not include any connections inserted by extrapolation"* and therefore *"there are cells showing no connection here that are connected in the other matrices."* Our claim is about a **completely-mapped** network; an incomplete map with known missing edges would deflate local clustering in a way that is not a property of the biology. Recorded as a named robustness check, not a headline option.

## 4. Node set: **neurons only**

The dataset includes nodes for muscle and non-muscle end organs. The canonical object is the neuronal connectome, and end organs are effectors rather than participants in the relational structure the law describes. **Filter on the `node_type` vertex property; the all-nodes network is a robustness check.**

## Processing, restating PIN 5 of the base seal

Chemical edges symmetrised (directed → undirected), union taken with gap junctions, **binarised** (the `connectivity` weight is discarded), **self-loops dropped**, and the analysis run on the resulting simple undirected graph. That is the faithful analogue of `cap(v) = BASE + ALPHA·c(v)` as implemented.

## ⛔ Standing

**These four choices are now fixed.** If the headline combination yields an unwelcome result, the robustness variants named above may be *reported* but may not be promoted to headline. That substitution is the same manoeuvre refused twice yesterday (H1b SD-vs-CV at 10:2x; allocation at 14:5x) and it is refused in advance here.

---

## 5. Neuron set resolved — appended before the analysis is run, from node metadata only

The two files' `node_type` labels **disagree**: the gap-junction file types the 95 bodywall muscles and 21 end organs as `MOTOR NEURONS`. The chemical file's typing is finer and is therefore **authoritative**; the gap file's typing is not used.

`PHARYNX` (50) and `SEX-SPECIFIC CELLS` (16) each mix neurons with non-neurons. Resolved by standard nomenclature: 20 pharyngeal neurons (I1–I6, M1–M5, MC, MI, NSM) out of 50, the rest `pm*` muscle / `mc*` marginal / `g*` gland / `e3*` epithelial / `bm`; and 8 sex-specific neurons (HSNL/R, VC01–06) out of 16, the rest `vm*` vulval muscles.

⇒ **Neuron set n = 300.** ⭐ **Consistency check, and it is the reason to trust the filter: 300 + CANL + CANR = 302, the canonical hermaphrodite neuron count.** CAN is excluded because the dataset itself files it under `OTHER END ORGANS` (it is famously non-synaptic) — the filter follows the source's own labelling rather than overriding it. **The script asserts `n == 300` and will refuse to run otherwise.**

## 6. Pre-declared secondary on the ESR diagnostic — declared BEFORE execution

The degree-preserving null also yields an **ESR distribution**, so ESR is additionally reported as a percentile against the null. ⛔ **The pinned absolute cut (ESR < 0.5 ⇒ sharp) REMAINS PRIMARY and the null-calibrated version may not override it.** Declared here, before the script has been run once, so it cannot be reached for afterwards.

## 7. Estimator

Linear quantile regression by IRLS on the pinball loss, **the same estimator for observed and null** so no comparison is estimator-biased. A brute-force exact solution (the QR optimum passes through two data points) is run on the observed headline fit **only**, as a convergence check; both are reported.
