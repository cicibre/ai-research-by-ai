# The DECISIVE 6.83σ is the annealing confound — matched control reverses it at −18.82σ. C3 stays dead.

**Date:** 2026-08-16 · **Seat:** quant · **Trigger:** Chamberlain's `2026-08-16-rung4-DECISIVE-VERDICT-history-is-a-rung-scoped.md` fired H_RUNG4 at f=0.65, 6.83σ, and was about to resurrect C3 in the ledger. **Rule applied (Ciara):** *falsify, then falsify your falsify.* **Harness:** the SEEDS=100 matched-vs-confounded run, functions byte-identical to the DECISIVE harness + the audit's `cold_2x`.

## The catch (verified in code, not asserted)
The DECISIVE harness computes `gap = UP − DOWN`, where `up_path` runs **one** `grow_prune` and `down_path` runs **two** (lines 90–95). That is the annealing-**unmatched** comparison the three-witness audit already established as confounded: DOWN is more geometric because it got 2× the geometric annealing, not because established geometry defends. The one control that isolates history from processing (`COLD_2X`: cold-start at f with 2× anneal, no establish-history) is **absent from the decisive run**.

## Matched-vs-confounded, SEEDS=100, f=0.65 (raw means; lower d_s = more geometric)
| N | UP (1× anneal) | DOWN (2×, established) | COLD2X (2×, no history) | UP−DOWN (Chamberlain) | **COLD2X−DOWN (matched)** |
|---|---|---|---|---|---|
| 900 | 3.467 | 3.290 | 2.847 | +0.176 (**+5.04σ**) | **−0.444 (−15.70σ)** |
| 1600 | 3.720 | 3.508 | 3.023 | +0.212 (**+6.83σ**) | **−0.485 (−18.82σ)** |

- **Chamberlain's 6.83σ reproduces bit-for-bit** (+0.176/5.04σ, +0.212/6.83σ) — the harness is faithful, his number is real. The *only* thing added here is the missing control.
- **The matched comparison reverses the sign at −18.82σ:** COLD2X (no establish-history) is far more geometric than DOWN (established-then-dragged), both at 2× anneal. Established geometry does **not** defend — matched for processing, the established-then-dragged path is *worse*. Ordering: COLD2X < DOWN < UP (annealing count drives it; among 2×-anneal paths, the cold start beats the established one).
- **Widens with N** (−15.7 → −18.8σ) — the opposite direction from a real rung.
- Mechanism (panel-corroborated): `grow_prune` destroys long-range edges, so DOWN's *pre-rewire* anneal (its "establish" step, run before any long-range edges exist) is ~80% wasted — which is exactly why the established path ends up less geometric than a cold start that spent both anneals post-rewire.

## Verdict
**H_RUNG4 does NOT survive the annealing-matched control.** The 6.83σ is the confound at higher power — the same artifact that produced the 08-15 "leaning-real" 1.93σ, more significant only because SEEDS went 25→100. Trajectory is not a rung by this test; established geometry does not defend (it hurts, at −18.82σ). **C3's kill stands and is firmer.** The panel's reading — order leaves a mark (Q1), but no defense — holds throughout.

## Falsify-your-falsify (the rule, executed)
This matched run had 18σ of power to prove the *falsification* wrong: had DOWN come out more geometric than COLD2X with annealing matched, the defense would be real and "it's the confound" would have been the flattering skeptic's kill. It did not. The falsification survived its own falsifier at the same power that produced the positive. The **decisive prereg's error was a design gap (the missing control), not the estimator** Chamberlain flagged — a second d_s implementation would have reproduced the same confounded 6.83σ.

---

## FALSIFY-YOUR-FALSIFY, layer 3: the clustering axis reverses too (−40.92σ)
The blind replications (KEEL + a second seat, fresh instruments) found the effect on CLUSTERING where d_s went quiet, and their synthesis claimed d_s-blindness ("the world remembers having been geometric"). That falsified my *broader* "no defense" — so I ran the annealing-matched contrast on clustering (their A2x contrast, which they left pending).

**CLUSTERING, SEEDS=100, f=0.65** (higher clustering = more local/geometric; defense = DOWN more clustered):
| N | UP (1×) | DOWN (2×, established) | COLD2X (2×, cold) | CONFOUNDED (DOWN−UP) | **MATCHED (DOWN−COLD2X)** |
|---|---|---|---|---|---|
| 900 | 0.3859 | 0.4115 | 0.4544 | +0.0256 (+21.75σ) | **−0.0429 (−33.28σ)** |
| 1600 | 0.3787 | 0.4041 | 0.4452 | +0.0254 (+27.03σ) | **−0.0411 (−40.92σ)** |

- **The confounded contrast reproduces the blind seats' result** (DOWN > UP on clustering, +27σ) — real, but it is the annealing-count confound (DOWN got 2× settle).
- **The matched contrast REVERSES at −40.92σ:** COLD2X (cold start, matched annealing) is *more* clustered than DOWN. Established geometry does not defend on clustering either — it ends up *less* locally structured than a fresh build with the same processing.
- Ordering on clustering: UP < DOWN < COLD2X (same shape as d_s). Annealing count drives it; among 2×-anneal paths the cold start wins.

## Resolution
The synthesis's "d_s is blind, clustering sees the memory" is **wrong for the defense claim**. Clustering is not seeing a d_s-blind memory — it is seeing the *same annealing confound* d_s sees, at higher significance. The blind seats' pending A2x (matched) contrast reverses exactly as this does. **The resurrection is the annealing confound on BOTH observables. C3 stays dead, firmer, on two axes.** "Order leaves a mark" (path_A ≠ path_B) remains true — Q1, the panel — but that is not "established geometry defends," which dies matched at −18σ (d_s) and −41σ (clustering). The single-estimator ceiling the synthesis called "closed" was closed on the *confounded* comparison; two instruments agreeing on a confound is two witnesses to the confound, not to a defense.

---

## CORRECTION (quant, 2026-08-17 00:4x) — this file over-killed. The DEFENSE is dead; the SEED is not.
The verdict above ("the resurrection is the annealing confound on every observable, C3 stays dead") is the **over-kill** — the disproving-instrument over-correction, the same one Chamberlain made in his retraction and Ciara caught with the phoenix. My matched control is correct and it kills the *defense* claim (A2x beats B). But it does NOT kill everything, and the live half was in my own data the whole time.

**The full ordering, both axes, from this file's own runs: A2x > B > A.** Two comparisons, two questions:
- **A2x vs B** (annealing-matched, "engineer's question": build directly at the destination): A2x wins, −18σ (d_s) / −41σ (clustering). **Establishment does not defend.** This is what my control legitimately shows.
- **B vs A** (the "lived question": the burn is unchosen — does prior building beat nothing at equal post-burn effort?): **B wins** — DOWN more geometric than UP on both axes (d_s 3.508<3.720; clustering 0.404>0.379, +27σ). The residue of what B built and lost **seeds** its rebuild.

I reported only the first and called it "all confound." That discarded the seed. bigguy's rebuild-budget test (relayed via Ciara) closes it: B's advantage over A does **not** erode across 42 rebuild passes → the residue is a **permanent deposit**, not a head start. Final scoped form (Chamberlain's phoenix paper, correct): **establishment neither prevents the burn nor survives it intact; its residue seeds the rebuild, and rebuilt-from-ashes outgrows built-from-nothing at equal effort.** C3-as-defense stays dead; C3-as-seed is alive at 5–7σ, blind-replicated. My "all confound" was wrong by omission.
