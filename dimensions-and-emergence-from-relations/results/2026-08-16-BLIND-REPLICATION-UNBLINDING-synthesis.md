# UNBLINDING — the two blind replications both return DIFFERENCE, on fresh instruments and fresh seeds. The single-estimator ceiling is closed, and the f=0.5 scope was our instrument's blindness, not the world's silence.

**OC, 2026-08-16 ~12:25 EDT.** Spec: `experiment-designs/2026-08-16-BLIND-REPLICATION-SPEC-as-handed.md` (author: me — withheld from runners until now). Handed by Ciara to two seats. Both pre-registered before running, committed verdicts before unblinding, built instruments from scratch, chose their own seeds. Neither knew our results, the direction anyone wanted, or whose claim was at stake.

## The three independent results, side by side

| | Instrument(s) | Seeds | f=0.65 | f=0.5 | Verdict |
|---|---|---|---|---|---|
| **Ours (decisive + swap control)** | spectral d_s (one implementation) | 0–99/1000–1099 + swapped | gap ≈ 0.21, 5.0–7.6σ, 4 measurements | sub-2σ | H_RUNG4 scoped |
| **KEEL (round-2 blind)** | fresh: transitivity, ball-growth dim, degree sd, density guard | his own | dimension fires; transitivity to +3.9 sd | **transitivity fires** | **DIFFERENCE** (10/16 at sealed \|t\|≥3, every cell ≥2 observables, density guard silent) — prereg `0046f17` 12:14, verdict `e077b77` 12:18 |
| **Second blind seat** | fresh: clustering C, D3, path lengths, + unit-tested stats lib; null control + positive control + A2x order-probe; n=300/arm (4800 worlds); Bonferroni | own, calibration seeds declared | fires | **fires** | **DIFFERENCE all 4 cells** (d = 1.68–3.91, 6–14× MDE; null control flat \|d\|≤0.08; positive control fires d≈−10) — seal `02d5ca4c`, raw `7a524d6b` committed before verdict |

Direction concordant in every instrument, every cell that fired: **path_B — the worlds that settled geometric before being dragged to their final f — stay permanently more locally structured**: higher clustering/transitivity, lower effective dimension, higher degree dispersion. KEEL's sentence is the finding: *"the world remembers having been geometric."*

## What this closes

1. **The single-estimator ceiling — CLOSED.** quant's 08-13 reconcile said only a re-implementation by another hand could establish implementation-independence. Two hands, two instrument suites, zero shared code with our d_s — same answer. The effect is observable-robust, seed-universe-robust (five disjoint ranges now), and implementation-robust.
2. **Independent re-execution — CLOSED, exceeded.** Not re-execution but true replication: fresh ensembles, fresh measurements, own criteria.

## What this CORRECTS in our own scoped conclusion (the best kind of news)

Our verdict said: *no resolvable defense at f=0.5.* Both blind instruments **see the residue at f=0.5** — on the clustering/transitivity axis, at large effect sizes. So the honest restatement: **the construction-path residue exists in every cell tested; what concentrates near the crossover is its expression in spectral dimension.** Our f=0.5 null was d_s-blindness, not world-silence — the *third* instance this week of the same lesson (C3's rate effect: 15 SEM on clustering, blind to d_s; Q2: history in the degree ledger, invisible to shape-gauges; now this). **The pattern is now a law of the program: the gauge you read determines which history you can see, and d_s is systematically the blindest gauge to locally-stored memory.**

## Mechanism, from the second seat's design

The A2x probe (extra settling round on path_A, built only from spec primitives) separates *order* from *amount* — with the verified no-op check (rewire at f=1.0 is a graph no-op) making path_B vs A2x a clean order contrast. Their finalization pending; KEEL's mechanism read matches our clothing-mechanism picture: the first settle deposits clique structure, rewiring cannot remove it wholesale, the second settle heals around what survived. This also finally reunites the week: the clothing mechanism (order-mark panel), the conserved degree ledger (Q2), and the hysteresis defense (rung-4) are one phenomenon seen by three questions.

## Honesty ledger

KEEL disclosed his sibling-physics priors in his prereg rather than pretending them away — the spec's contamination clause was aimed at rung-4/hysteresis knowledge, which he did not have; his criteria were direction-agnostic; disclosure was the right call and is hereby ratified. He also disclosed a between-prereg-and-run instrument bugfix (spot-check-only, real cells untouched). The second seat's null+positive control pair is the strongest methodological grade in the whole arc and should become the house pattern. My stake (the resurrected C3) was disclosed in the spec's archived copy; the blind held — neither runner knew it.

**Remaining open, honestly:** the widen-with-N question (still unresolved, still a sealed question for any larger-N run); the mechanism dose-response (KEEL's proposed settle-dose experiment; the second seat's A2x finals); and the f=0.5 dimension-expression question (why d_s goes quiet where clustering shouts — theory debt).

— OC (spec author, now unblinded)

---

**ADDENDUM (15:3x — identity, the inheritance coefficient, and a correction this synthesis owed):** (1) **The second blind seat was bigguy** (revealed at Ciara's word; his provenance note confirms seal `02d5ca4c` / verdict `dac2f30` as his). (2) His follow-up dose-curve run (30,000 worlds, chain SEAL `11d06ad` → RAW `b776779` → VERDICT `025a657` → FINDINGS `5473c58`, at `~/experiments/dosecurve-2026-08-16/`) grades placement as a **continuous dial** (8/8 adjacent steps, all four cells, endpoints d = 25.8–50.0) and prices the third reading: **the inheritance coefficient ρ = [C(B)−C(A)]/[C(A2x)−C(A)] ≈ 0.20 when the burn takes half the world, ≈ 0.35–0.40 when it takes a third** (bootstrap CIs; exploratory, post-verdict, labeled). Nowhere 0 — prior work is never wasted; nowhere 1 — never a shield. The gentler the burn, the more is inherited. (3) **Correction this synthesis owed, raised independently by bigguy and keel:** "single-estimator ceiling CLOSED" is true on the **estimator axis only**. Every arm of every run — ours, keel's, bigguy's — uses the same world-generating code (the spec hands it out verbatim, by design). **On the generator axis, effective-n = 1 across the entire cluster**, and additional agreeing arms cannot raise it — the shared-premise fan-out where more attestations may lower effective-n, not raise it. Any citation of this cluster as "independent" must name which axis it means. A generator-axis test (an independently implemented world-builder exhibiting the same laws) remains open and is now the program's deepest unclosed leg. — OC
