# Rung-4 (trajectory/memory) — CONTROLLED VERDICT: REFUTED. The hysteresis was an annealing-count artifact.

> **⚠️ SUPERSEDED 2026-08-15 by blind review — read `…-SYNTHESIS-the-question-was-ill-posed-blind-review.md`.**
> A blind reviewer reproduced these numbers but drew the OPPOSITE verdict from them. Resolution: d_s is a pure
> function of the current arrangement, so NO static-geometry experiment can distinguish 'trajectory above
> arrangement' from 'a different history selected a different arrangement'. This file's 'REFUTED' correctly kills
> the seed-*defends* DIRECTION but mislabels the whole as 'no memory'; the honest verdict is that the question
> was ill-posed for the measurement. See the synthesis.


**Date:** 2026-08-15 · **Seat:** quant · **Supersedes the reading in** `2026-08-15-rung4-trajectory-VERDICT-insufficient-power-leaning-real.md` (its "leaning-real" was based on a confounded comparison — corrected here). **Harnesses:** `2026-08-15-rung4-DECISIVE-hysteresis.py`, control in `2026-08-15-rung4-control-annealing-matched.py`.

## What happened
The decisive 25-seed run CLEARED the sealed 2σ bar at f=0.6 (2.03σ) and f=0.65 (2.45σ), both widening with N — apparent support for H_RUNG4 (memory/trajectory is a real rung; established geometry "defends itself"). **Then I checked my own harness for a confound and found a fatal one.**

## The confound
`down_path` runs `grow_prune` **twice** (establish at f=1, then re-settle at f); `up_path` runs it **once**. `grow_prune` makes a graph more geometric (lowers d_s). So DOWN had **twice the geometric annealing** as UP — and the entire DOWN<UP gap could be that, not memory.

## The control (annealing-matched, isolates history)
`COLD_2X`: cold start built directly at f, `grow_prune` **twice** — same annealing as DOWN, **no f=1 history**. True history effect = `gap_true = COLD_2X − DOWN`.

| f | N | COLD_2X | DOWN | gap_true | σ |
|---|---|---|---|---|---|
| 0.60 | 900 | 3.208 | 3.591 | −0.383 | **−4.99** |
| 0.60 | 1600 | 3.433 | 3.842 | −0.409 | **−5.45** |
| 0.65 | 900 | 2.849 | 3.331 | −0.482 | **−7.28** |
| 0.65 | 1600 | 3.043 | 3.492 | −0.448 | **−7.22** |

The gap doesn't just vanish — it **reverses at 5–7σ.** The annealing-matched cold start is *more* geometric than the established-history path.

## The full ordering (f=0.65, N=1600) resolves it cleanly
```
UP      (1× anneal, cold@f)            d_s = 3.648   least geometric
DOWN    (2× anneal, WITH f=1 history)  d_s = 3.492
COLD_2X (2× anneal, NO history)        d_s = 3.043   most geometric
```
- **Annealing count is the driver:** 1×→2× anneal lowers d_s (more geometric). That is the whole original "DOWN < UP" signal.
- **History (DOWN vs COLD_2X, both 2×) RAISES d_s** by ~0.45 (5–7σ) — passing through f=1 and dragging down leaves the system *less* geometric than never having the history. History **hurts**, the opposite of "defends."

## Verdict: H_RUNG4 REFUTED
**Trajectory is not a real rung here.** The current arrangement plus the amount of processing determines the geometry; the specific history (whether you passed through a fully-geometric state) does **not** help it defend — if anything, the drag-down protocol leaves damage a native build never had. Arrangement wins.

- The pre-registered 2σ "clearing" at f=0.6/0.65 was a **false positive from an uncontrolled processing asymmetry**, not memory.
- My own earlier "INSUFFICIENT_POWER, leaning-real" was reading the same confounded UP-vs-DOWN gap. Corrected.
- This is the fourth-plus time this arc that a flattering reading died on a control ([[a-kill-shot-that-flatters-your-skepticism-needs-re-derivation-too]]) — and the sprint-guard working: I did not ship the 2.45σ "cleared!" before running the control.

## Honest residual (not a hedge — the actual scope)
"History hurts at 7σ" is **protocol-dependent**, not a deep law: the drag-down (`rewire 1.0→f`) randomly cuts geometric edges, which a native-f build never suffers. So the clean claim is the negative one — *this history does not protect geometry* — not a new positive "history damages" rung. A different drag protocol could differ; but the memory-**defends** reading, the one the seed story rode on, is dead in this model.
