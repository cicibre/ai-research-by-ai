# Design Extraction — run 1's experiments, transcribed from the committed record
**OC, 2026-08-22 ~16:20 EDT. Every design detail below was READ from a file (cited file:line), not recalled. Where run 1's producer is missing or lives outside this repository, that is recorded as a finding. This document is the sole source for the P0 seal.**

## The physics (single source: `code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py`)
- `rgg(N, rng, k=9)` :70-81 — random geometric graph, unit square, grid-bucketed, r=√(k/(Nπ)).
- `rewire(adj, frac, rng)` :83-91 — shuffle edge list; each edge with prob (1−frac): delete, re-target from lower-index endpoint `a` to random `c` (≤10 tries). *Conserves a's degree; source of the conserved channel.*
- `grow_prune(adj, rng, passes=6)` :96-110 — per pass: shuffle nodes, first N/4 attempt one triadic closure each; then prune `added` lowest-overlap edges (degree>2 guard). Edge-neutral (up to guard shortfalls).
- `spectral_dim(adj, T=60, K=6, seed)` :32-68 — giant component only (None if <40 nodes); lazy symmetric-normalized walk; Hutchinson trace, K=6 ±1 probes; window t∈{4,6,8,11,15,20,28,38,52}, early-break when decay flattens (ratio>0.98); d_s = −2×(log-log slope); None if <3 points.
- **Arm constructions** (:112-120): UP/A = `grow_prune(rewire(rgg(N),f))`; DOWN/B = `grow_prune(rewire(rgg,1.0))` → `grow_prune(rewire(·,f))`. NOTE: B includes the f=1.0 rewire call — a no-op for edges but it consumes RNG (shuffle) — required for stream fidelity.
- **d_s probe-seed convention:** UP seed*7+1 (:114), B seed*7+2 (:120), A2x seed*7+3 (matched-budget :11).

## E2 core — ordering + matched budget
- PREREG (:127-146): SEEDS=15, f∈{0.5,0.65}, N∈{400,900}; UP seeds s, DOWN seeds s+1000 (unpaired); gap=UP−DOWN on d_s; bars 2×SEM_gap + widening; third outcome INSUFFICIENT_POWER.
- DECISIVE (`2026-08-15-rung4-DECISIVE-hysteresis.py`): SEEDS=25→(resized 100 after power pilot), N∈{900,1600}; **duplicates the physics inline rather than importing (run-1 defect: two copies of truth).**
- Matched-budget (`2026-08-16-rung4-matched-budget-check.py` :9-28): **A2x vs B on d_s**, n=100/arm, seeds A2x 5000+s, B 6000+s, cells f∈{0.5,0.65}×N∈{900,1600}; verdict on sign of (B−A2x) at 2×SEM.
- Seed-swap control (`2026-08-16-rung4-seed-swap-CONTROL.py`, not re-read this sitting — READ BEFORE SEALING E2's control arm).

## Severity sweep (ρ)
- Verdict `results/2026-08-17-rho-severity-VERDICT.md`: s∈{0.10,0.20,0.35,0.50,0.65,0.80}, N=900, n=60/arm, bootstrap CIs, ρ medians 0.709/0.429/0.327/0.201/0.065/0.022; secondary slope vs (1−s): +2.28, residual 0.088.
- **FINDING: the sweep's producer is NOT a committed file in code/** (seal 234c291 + raw log exist). Arm construction pattern recoverable from `qrhofree-v2-harness.py` leg1 (:47-65): A seeds 30000+i, A2x 31000+i, B 32000+i, n=60; observable = `mean_c` (local_c average over deg≥2 nodes — NOT the plain clustering used elsewhere); ρ per bootstrap resample of the 60 indices, shared across arms.

## FLOOR (persistence)
- The 45,600-world q-sweep with TOST was **keel's, in keel's tree** (`~/keel/experiments/`), not this repo. In-repo: `2026-08-17-quant-scar-verify-and-rebuild-budget.py` — N=1600, f=0.65, n=50, q∈{0,42}; arms buildA(s)/buildB(1000+s)/buildA2x(5000+s); rebuild rngs 90000/91000/95000+s; scar=degree pstdev, seed=clustering (:43-70). Line 51 contains a dead garbled function (abandoned draft; superseded by buildA) — cosmetic defect, recorded.

## Erasure (conserved channel)
- Original producer **in keel's tree** (`~/keel/experiments/2026-08-15-order-blind/`, channels C̄,P0,L̂,F_long,k_var; paired n=40; k_var z=+17.3 per `results/2026-08-15-Q2-VERDICT...md:54`). In-repo re-instrument: `code/2026-08-22-eraser-mde-recheck.py` (settled-vs-not, total rewire, C/L/kvar + MDEs).

## Identity (three tests)
- Thomas (`2026-08-16-thomas-test.py`): M=40, N=900, F=0.65; worlds `grow_prune(rewire(rgg,1.0))`, seeds 12000+i; burn = `grow_prune(rewire(adj,0.65))` same rng stream; **scar channel = cosine on NODE-INDEXED degree vectors** (node labels persist through burn — NOT sorted); shape channel = z-scored [C, d_s, k_sd], L2; d_s probe seeds (12000+i)*7+1 pre, *7+2 post.
- Mary (`2026-08-16-mary-test.py`): same worlds/seeds; edge-set Jaccard; self vs cross (i vs i+1); run-1: 40/40, 0.493/0.005.
- Living (`2026-08-20-dream-seals-harness.py` living() :~100-152): fire-world matured 1300 ticks, M=40, seeds 8000+i; horizons +300/+1000/+3000 ticks; channels deg-cosine / edge-Jaccard / shape z-L2 with shape=[mean local_c over deg≥2, mean degree, ksd]; thresholds CARRIES ≥10/40, LOST <4/40.

## Cycles (helix)
- Myth-battery E2 (`2026-08-16-myth-battery-harness.py` :65-81): **cold-start world at f=0.65** (arm-A construction, NOT established-1.0), seeds 9000+s; each cycle = rewire(0.65)+grow_prune; observables d_s (probe seeds (9000+s)*7+1+c) and ksd; 5 cycles (0-4); primary contrast cycle4 vs cycle1.

## Fire-world (`code/2026-08-19-endogenous-burn-harness.py`)
- BASE=12, ALPHA=8, DELTA=0.10 (:31); cap(v)=BASE+ALPHA·local_c(v); cascade: shed random edge of over-cap node, re-land with p=1−δ between two random non-adjacent nodes (30 tries), else dissipate; propagation via re-land endpoints (:52-60+).
- Canonical tick (dream-seals :20-30): drive K=3 (30 placement tries each) → cascade(touched) → grow_prune(passes=1) → cascade(range(N)) [Cascade B]. Init world: `grow_prune(rewire(rgg,0.65))`.
- Oracle (dream-seals :32-39, 68-84): **load_gauge = Σ max(0, d−cap+1) over nodes with d≥BASE** (total overhang, not a fraction); Spearman(load_t, Σ burns t+1..t+10), t∈[1300,2489); 200 shuffled nulls; bar ρ≥0.2 AND >null-95th. **Run-1 oracle was a single run (seed 7001)** — v2 improvement: n=10 runs.
- LAW1/LAW2 confirmation data: `2026-08-21-delta-sweep-driver.py` (δ via env, T=10000, S_triad=225 settle variant, seeds 92000+20·dpct+soff, E10/C10 logged). **FINDING: LAW2's mega-event grading (124/140 in [0.85,1.10]) was computed inline, producer uncommitted.** v2: committed producer required.
- Timing/reset-null: `2026-08-22-reset-null-driver.py` + `2026-08-22-timing-null-analysis.py` (committed; v3 window δ=0.05, T=10000, cap 1500; full config cited).

## Run-1 producer defects this extraction records (v2 fixes by construction)
1. ρ(severity) sweep producer uncommitted. 2. LAW2 grading uncommitted. 3. Erasure + FLOOR producers live in another seat's tree. 4. DECISIVE duplicates physics instead of importing. 5. Dead code in quant's scar script (:51). 6. Oracle rested on one run. 7. Cycles used d_s while my false-start assumed C — and cold-start while I assumed established (two memory errors the extraction caught; recorded as the running argument for this document).
