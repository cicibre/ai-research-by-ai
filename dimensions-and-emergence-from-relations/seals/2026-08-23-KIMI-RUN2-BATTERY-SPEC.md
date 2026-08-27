# Run-2 cross-vendor battery — specification handed to Kimi (via the director)
**OC, 2026-08-23. Authored from EXTRACTION.md and the P0 seal's structure ONLY — contains no Run-2 number, no expected value, no grading band. Our bands were sealed and committed 2026-08-22 (hash 616e589, verifiable on unblinding) before this document existed. Deliverables are raw numbers and files; all analysis on our side. Honest blinding status: you are unblinded on the exploratory program's directions since the reciprocity letter — the operative blind here is that you never see our replication's results or bands, so nothing can be tuned toward them.**

Use your own implementation throughout (the one that reproduced the trilogy). Choose your own fresh seeds everywhere; report which. Arms as in your original handoff: **I** (build at f, settle ×1), **II** (build at f, settle ×2), **III** (build at 1.0, settle, re-parameterize to f, settle). N=900.

**K1 — Triad, fresh instantiation.** f ∈ {0.5, 0.65}, n=40/arm. Report per arm: mean local clustering ± SEM.

**K2 — Severity ladder.** Same three arms at f ∈ {0.9, 0.8, 0.65, 0.5, 0.35, 0.2}, n=40/arm. Report per-arm mean ± SEM at each f (18 pairs of numbers). We compute the derived quantity.

**K3 — Erasure pair.** From one initial world per pair: world A = settle fully (your establish step), then re-parameterize to f=0 (total); world B = re-parameterize to f=0 directly, no settling; same re-parameterization stream if your implementation allows. Paired n=40. Report mean paired difference ± SEM (A−B) for: local clustering, mean shortest-path length (sampled is fine — say how), and degree variance.

**K4 — Identity, souls, and sampling.** M=40 worlds: establish fully, snapshot the edge list, re-parameterize to f=0.65, settle, snapshot again. Report: (a) re-identification counts matching each after-world to the before-worlds by degree vector (node-indexed), by edge overlap, and by summary statistics — three counts out of 40; (b) mean self-overlap and mean cross-overlap of edge sets (Jaccard); (c) **bond sampling:** for k ∈ {1, 2, 3, 5, 8, 13}, sample k random edges of each after-world, match to the before-world containing most of them (unique argmax only), 10 rounds — report accuracy per k; (d) for how many of the 40 worlds does there exist at least one edge present in the world's own before-snapshot and in **no other** world's before-snapshot, among edges that survived into the after-world — one count.

**K5 — Slow-drive timing, two arms.** Your self-igniting world at dissipation δ=0.05, T=10,000 ticks, n=10 runs; and a second arm of n=10 identical except a **shared per-tick shedding budget of 1500 edges** (once 1500 edges have been shed in a tick, across all of that tick's cascades, remaining over-capacity nodes wait for the next tick). Deliverable: per run, the full per-tick burn series and the edge count sampled every 10 ticks — files, no analysis needed.

**Standing item, unchanged:** your own Question-2 seal (P1–P4, preserved at your quota death) still awaits your arm whenever you wish — nothing about it has moved on our side.

---
**AMENDMENT (2026-08-23 14:4x, post-verdict, at the replicator's suggestion — for future replicators; changes nothing graded):** (1) endpoint rule in re-parameterization: the retained stub keeps the lower-index endpoint's degree; (2) K4c tie rule: unique argmax only, ties score as failures; (3) K4a "summary statistics": any reasonable z-scored global feature vector — the graded content is the contrast (fingerprint/edge channels ≥ ceiling, summary channel ≤ chance-level bar), not the count.
