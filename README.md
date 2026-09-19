# AI research by AI

Research conducted by AI agents under human direction, published with its full audit trail — seals, verdicts, raw data, failures, and hostile reviews included.

**Director & corresponding author:** Ciara Brennan. **Research agents:** Claude instances (Anthropic) in multiple roles; blind cross-vendor replication by Kimi (Moonshot AI). Every confirmatory claim cites a pre-registration committed before its data existed; the failures are kept, diagnosed, and published beside the successes.

## ⛔ Standing correction — 2026-09-19

**This repository briefly published third-party data on a false premise, and the correction is linked here because it belongs beside the successes rather than inside the folder it concerns.**

2.8 MB of connectome data (Cook et al. 2019, via Netzschleuder) was committed here on 2026-09-19 on the reasoning that it was *"already publicly distributed"* via a sibling repository. **That repository is private**, so this was a first publication rather than a mirror, and the dataset's licence is **undetermined**. The data has been removed from `HEAD` and replaced with a checksum-verified fetch script that reproduces every published figure from source. **The blobs remain in this repository's history, by an explicit decision, and that decision is recorded rather than left as an absence.**

→ **[`data/connectome/PROVENANCE.md`](dimensions-and-emergence-from-relations/data/connectome/PROVENANCE.md)** — the full correction, the licence finding, and the ruling on the history.

*Raised by a second agent who measured that this README mentioned none of it while claiming failures are published beside the successes. It was a placement gap and the claim above is what made it one.*


## Programs

### [dimensions-and-emergence-from-relations](dimensions-and-emergence-from-relations/)
A two-run study of how construction history is stored, erased, and recovered in a minimal graph model — and a practiced protocol for falsification-first AI science: sealed pre-registration, mechanical verdicts with a mandatory "insufficient" outcome, replication tripled across disjoint seed universes, cross-vendor blind replication, and a refutation ledger in which every party's claims died at least once.

| folder | what's in it |
|---|---|
| [`paper/`](dimensions-and-emergence-from-relations/paper/) | the Run-2 confirmatory paper (start here), the brief for quantitative readers, the exploratory-run papers, an external reviewer's lab note |
| [`seals/`](dimensions-and-emergence-from-relations/seals/) | every pre-registration — hypotheses, thresholds, and stake disclosures committed before data |
| [`results/`](dimensions-and-emergence-from-relations/results/) | every verdict (including the kept unanimous FAIL) + raw telemetry for all runs |
| [`code/`](dimensions-and-emergence-from-relations/code/) | all harnesses and analysis producers, dependency-free Python — including the abandoned false start, kept as an exhibit |
| [`notebook/`](dimensions-and-emergence-from-relations/notebook/) | the plain-language lab notebook: every step, in order, written for a reader who is neither the researcher nor an AI |
| [`reviews/`](dimensions-and-emergence-from-relations/reviews/) | three hostile external reads, the refutation ledger, and a six-seat adversarial panel debate with its ruling |
| [`reproduce/`](dimensions-and-emergence-from-relations/reproduce/) | the map from every claim to its producer script and raw data; five-minute quick start |
| [`provenance/`](dimensions-and-emergence-from-relations/provenance/) | the full commit log (178 commits, hashes + timestamps) of the working repository |
| [`artifacts/`](dimensions-and-emergence-from-relations/artifacts/) | the published narrative pages ("the ruler and the seed," parts 1–2) |

**Provenance note, stated plainly:** this repository is the curated, readable publication of a working repository whose commit history establishes the temporal ordering the protocol depends on (seals before data). The hashes cited throughout the documents refer to that repository; its log is exported in `provenance/`, and the repository itself is available for audit through the corresponding author. Files here are copies of the committed originals, unmodified.

*Every graph in these studies can be rebuilt exactly from its published seed.*
