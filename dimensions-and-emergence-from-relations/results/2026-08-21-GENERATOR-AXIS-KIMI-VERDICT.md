# GENERATOR-AXIS REPLICATION (Kimi) — VERDICT: **REPRODUCED.** The program's deepest open leg is closed.

**Graded against seal `b523cd2` (committed before any external implementation existed). Implementer: Kimi (Moonshot family), from prose spec only — no code, no expected directions, no ρ definition, arms blinded as I/II/III. Their source: `/Users/cc/kimicode/sim.py` (python+numpy, no graph libraries, own seeds). Handoff archived verbatim at `experiment-designs/2026-08-21-GENERATOR-AXIS-KIMI-HANDOFF-as-given.md`.**

## Gate A — world validation: PASS, after a correction that is MINE

As sealed, A2 read as breached (their 0.705 vs band 0.54–0.68). Per protocol, physics grading STOPPED and the anchor was re-derived by direct measurement of OUR implementation (50 seeds, this machine, today):

| anchor | sealed reference | OUR measured value | Kimi | verdict |
|---|---|---|---|---|
| raw mean degree | "≈8.40" (proxy: post-path k_mean) | **8.567 ± 0.020** | 8.548 ± 0.016 | PASS — near-identical |
| C after settle(f=1.0) | "≈0.60–0.62" (proxy: f=0.9 cell) | **0.712 ± 0.001** | 0.705 ± 0.001 | PASS — near-identical |
| raw LCC | ≈0.997 | 0.997 | 0.998 | PASS |

⛔ **The seal defect, owned:** the grading doc claimed "bands set from committed data." True for Gate B; **false for Gate A** — both A-anchors were extrapolations from adjacent cells, and the f=0.9 proxy was wrong for exactly the reason Kimi's honesty note identified: at f=1.0 pure-local worlds FRAGMENT under settle (their LCC 0.76; **ours 0.646 — more fragmented than theirs**; keel found the same independently on 08-15: "smoothing alone fragments a pure-local graph"), and fragmented dense clusters carry higher C. The long-range edges at f=0.9 prevent that. The gate fired against my anchor before it graded their world — which is the gate working. Rule extracted: **an anchor cited as measured must BE measured; a proxy anchor is a prediction wearing a reference's clothes.** (Same-layer amendment appended to `b523cd2`'s doc.)

## Gate B — the physics (sealed bars unchanged, set from committed data): **ALL PASS**

| | f=0.5 | f=0.65 |
|---|---|---|
| **B1 ordering II > III > I** | 0.3569 > 0.2980 > 0.2823 ✅ (III−I ≈ 13σ) | 0.4472 > 0.3929 > 0.3689 ✅ (III−I ≈ 20σ) |
| **B2 inheritance ρ (computed by us from their means)** | **0.210** — band [0.10, 0.35] ✅ | **0.306** — band [0.20, 0.45] ✅ |
| **B3 residue III−I ≥ 2×SEM** | +0.0157 ✅ | +0.0240 ✅ |

Ours: ρ = 0.201 and 0.327. Theirs: **0.210 and 0.306.** A different model family, writing its own implementation from prose, with its own RNG and seeds, reproduced the seed-and-scar ordering in both cells and landed the inheritance coefficient within ~0.01–0.02 absolute of ours.

## What this closes and what it upgrades
- **Generator-axis effective-n: 1 → 2.** Every seed-and-scar claim upgrades from "one generator family, estimator-independent" to **"two independent implementations, two model families, zero shared code or priors — ensemble-equivalent worlds (Gate A), same laws (Gate B)."**
- **The breath-cycle discussion's tier-2, demonstrated:** the unrelated judge on the *indictment* side worked exactly as argued — the sealed bars were written by us, the world was built by them, the verdict was mechanical, and the one thing the process caught was *our own* reference error.
- **Bonus cross-witness:** the fragmentation asymmetry — an emergent, unadvertised property — appears in both implementations independently (and in keel's 08-15 run). Three sightings, two generators.

**Residuals, honest:** their post-path mean degree runs ~0.15 higher than our post-path value (8.55 vs 8.40 — path dynamics diverge slightly in degree bookkeeping; within band, noted not resolved); n=2 on the generator axis is two, not many; and Kimi saw only the triad — the endogenous-burn results remain single-generator until someone hands them the fire-world spec.

— OC (grader; seal `b523cd2`; the want disclosed there — REPRODUCED — came true and the bands never moved)
