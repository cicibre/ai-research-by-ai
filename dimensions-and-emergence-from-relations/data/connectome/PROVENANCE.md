## ✅ DECIDED 2026-09-19 18:24 — THE HISTORY STAYS. Do not rewrite it.

**Ciara's decision, recorded here so it is a decision and not an absence.**

The data was removed from the public mirror's `HEAD` and replaced with `fetch_connectomes.sh`. **The
blobs remain in that repository's history and are to be left there.** Complete removal would require a
force-pushed history rewrite.

**If you are a future seat, or a future me, reading this and reaching for `filter-repo`: don't.** This
is not an oversight anyone missed. It was raised, priced and ruled on:

- The practical risk is low — the Cook et al. connectome is widely mirrored, including at
  wormwiring.org.
- A rewrite is destructive, breaks every existing clone and every commit hash downstream of it, and
  would be done to make a record look cleaner rather than to make it truer.
- **A repository that scrubbed the evidence of its own mistake would be the wrong shape**, and
  particularly so on the day this organism built a board premised on not doing that.

The correction stands *inside* the history rather than in place of it. That is the point.

---

# ⛔ CORRECTION 2026-09-19 18:10 — THE COMMIT THAT CREATED THIS FILE STATED A FALSEHOOD, AND I ACTED ON IT

`academics@51b5362` is titled *"2.8MB of other scientists' data sat in a **public** repo for 17 days"*
and its body says *"20 tracked files in a **PUBLIC** repository."*

**`cicibre/academics` is PRIVATE.** Verified: `gh repo view` → `academics: PRIVATE`,
`ai-research-by-ai: PUBLIC`.

**And I used that false premise to make an outward decision.** I copied this directory into the
public mirror reasoning that *"the data is already publicly distributed via the academics repo, so
licensing is settled and mirroring changes nothing materially."* Both halves were wrong:

1. It was **not** already published — academics is private. **So that copy was a FIRST PUBLICATION of
   third-party data, not a mirror.**
2. **The licence is UNDETERMINED.** Checked at source 2026-09-19: the Netzschleuder page for
   `celegans_2019` states no dataset licence — no CC-BY, no CC0, no public-domain designation. The
   AGPL-v3 in the site footer governs the *site's software*, not the data. There is no licence file
   anywhere in this directory.

**I do not have a basis for having redistributed it, and I asserted one.** The practical risk is
probably low — the Cook et al. connectome is widely mirrored, including at wormwiring.org — but *low
practical risk is not the same as a checked permission*, and tonight's entire subject is the
difference between those.

**Status: the data is live on the public mirror now (HTTP 200) pending Ciara's decision.** The
proportionate fix, if she wants it, is to remove the redistributed copy from the public mirror and
replace it with a fetch-from-source script plus this provenance — which preserves reproducibility
**without** redistributing. ⚠️ Note that `git rm` would not remove the blobs from the public repo's
history; complete removal requires a history rewrite, which is destructive, and is hers to authorise.

*Corrected by the author of the error, on noticing that `gh repo list` reported a visibility I had
been assuming all evening without checking.*

---

# PROVENANCE — connectome data

**This directory held 2.8 MB of third-party scientific data with no attribution file for 17 days
(2026-09-02 → 2026-09-19).** The provenance was recorded in the pre-registration addendum and
nowhere the data itself would lead you. Fixed here; the facts below are lifted from
`experiment-designs/2026-09-02-CONNECTOME-CAPACITY-PREREG-ADDENDUM-substrate-choices.md`, which
was sealed **before** any file was downloaded.

## C. elegans — hermaphrodite and male

**Cook, S.J. et al. (2019), "Whole-animal connectomes of both *Caenorhabditis elegans* sexes,"
*Nature* **571**:63–71.** Obtained via **Netzschleuder**, dataset `celegans_2019`; canonical at
**wormwiring.org**.

Sub-networks used: `hermaphrodite_chemical_corrected`, `hermaphrodite_gap_junction_corrected`,
`male_chemical_corrected`, `male_gap_junction_corrected`. The source ships **twelve** sub-networks;
choosing among them is four researcher degrees of freedom, and all four were closed in the sealed
addendum **from the dataset's description text and node/edge metadata only** — never from a summary
statistic that could indicate which way the test would come out.

`_corrected` is used because the dataset's own description says those "correspond to corrected
versions of the network made available in July 2020." Using the most accurate published map was
chosen without knowing whether correction helps or hurts the claim; the uncorrected variant is a
robustness check and **cannot become the headline**.

End organs (muscle and non-muscle) are filtered out on the `node_type` vertex property, following
the source's own labelling rather than overriding it. **Neuron set n = 300**, and 300 + CANL + CANR
= 302, the canonical hermaphrodite count — CAN is excluded because the dataset itself files it under
`OTHER END ORGANS` (it is famously non-synaptic). The harness asserts `n == 300` and refuses to run
otherwise.

## Drosophila larval whole-brain

`fly_larva` — the larval *Drosophila* whole-brain connectome, as distributed in the same
Netzschleuder collection.

## What this data was used for, and what it showed

Testing `cap(v) = BASE + ALPHA · local_clustering(v)` — capacity from local closure — in
completely-mapped real networks. **NOT CONFIRMED in all three** (C. elegans hermaphrodite, C.
elegans male, Drosophila larval); all three within ±0.35 sd of a degree-preserving null. A
**REFUTED** verdict was published 2026-09-02 and **withdrawn to INCONCLUSIVE 2026-09-09** — see
`results/2026-09-02-CONNECTOME-CAPACITY-VERDICT-*` and `cowork/2026-09-09-RULING-*`.

**Cite the original authors, not this repository.** The data is theirs; only the analysis is ours.
