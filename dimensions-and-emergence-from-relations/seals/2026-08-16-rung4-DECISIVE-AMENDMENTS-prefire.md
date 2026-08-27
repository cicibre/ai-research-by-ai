# DECISIVE run — pre-fire amendments, sealed BEFORE execution

**OC, 2026-08-16 11:17 EDT, at Ciara's explicit "i want you to run it." Committed before the run starts; the run's output file will carry its own start timestamp after this commit.**

Instrument: quant's `code/2026-08-15-rung4-DECISIVE-hysteresis.py`, executed **verbatim** (env-config only, no code edits). Sealed criteria unchanged from his in-file prereg: H_RUNG4 = gap > 0 AND |gap| > 2·SEM_gap at N=1600 AND widens 900→1600; H_TERMINAL / INSUFFICIENT_POWER as written. Grading is mechanical — the harness computes its own verdict from criteria fixed in code on 08-15; no human judgment enters between data and verdict.

**Amendments (per the 08-16 power calculation, `2026-08-16-rung4-DECISIVE-power-calculation.md`):**
1. **SEEDS = 100 per arm** (was 25) — sized so the conservative scenario (gap stays at 0.16) is resolvable at ≥80% power; basis: measured SD = 0.34 at N=1600.
2. **F_LIST = 0.5, 0.65** (the two pre-registered f-points from the original run; dropping the default's untested 0.6 keeps the comparison clean against the 08-15 baseline).
3. **Threshold note:** at n = 100/arm the gap dof ≈ 198; the t-quantile for the 2σ criterion is 1.972 ≈ 2.0, so the sealed 2×SEM bar is within 1.4% of its advertised meaning at this size — the t-vs-z correction that mattered at n=15 is immaterial at n=100, and the bar stands as sealed.
4. **Trend leg pre-specified:** after the primary verdict, the widening is tested as unpaired Welch, one-sided (H1: gap₁₆₀₀ > gap₉₀₀), reported with t and p — giving the 08-16 secondary analysis its pre-registered home. The trend test is reported alongside, and does not modify, the harness's mechanical verdict.

**Execution label:** hands-executed (OC), quant-sealed, Ciara-ordered. Output: `results/2026-08-16-rung4-DECISIVE-run.log`, committed raw whatever it says. Independent re-execution is available to anyone: the harness is deterministic in its seed enumeration.

**Stakes, on the record before the data:** my original claim wants H_RUNG4 (I staked hysteresis and graded it dead; this is its resurrection trial). quant's INSUFFICIENT_POWER verdict leans real. The bar does not care what either of us wants, which is the point.

— OC

---

**CONTROL RUN (Ciara's design, 2026-08-16 11:41, pre-registered before execution):** re-run with seed ranges SWAPPED — UP arm gets seeds 1000–1099, DOWN arm gets seeds 0–99. Purpose: exclude a seed-range artifact (the possibility that the two disjoint ranges systematically differ, mimicking a gap). **Pre-registered expectations:** if the f=0.65 gap is physics, the swapped run reproduces gap ≈ +0.18–0.24 at comparable σ, same sign; if it is a seed-range artifact, the gap collapses or flips. The f=0.5 cells should stay sub-2σ either way. Executed as a wrapper driving the harness's own verbatim functions with swapped assignment (no other change), labeled CONTROL, raw output committed as-is. — OC

**Control run ABORTED 11:42 at Ciara's direction, mid-execution, before any output was read.** No data from the partial run enters the record. The pre-registration above stands unconsumed — the expectations remain sealed and valid for whoever executes it, whenever. Recorded so the aborted start is an event, not a silence. — OC

**Control restarted with full ceremony (11:45, Ciara: "take your time doing this with the same level of care you gave to the first run"):** the control now runs from a committed instrument — `code/2026-08-16-rung4-seed-swap-CONTROL.py` — which loads the physics functions verbatim from the committed 08-15 harness (single source of truth, no drift-able copy), swaps ONLY the seed assignment, carries the pre-registered expectations and a mechanical grading of them in its own text, discloses the executor's stake (PHYSICS is OC's wanted outcome), and writes to `results/2026-08-16-rung4-seed-swap-CONTROL-run.log`, committed raw whatever it says. The haste differential between the first control attempt and the decisive run is recorded in OC's instrument spec as bias channel three. This paragraph and the instrument are committed BEFORE execution. — OC

---

**MATCHED-BUDGET CHECK (12:30, sealed before running — the second blind seat's A2x probe found the confound our protocol carried):** path_B (establish→drag) settles 12 passes vs path_A's 6 — amount and order were entangled in the UP/DOWN design. Their D3 channel shows A2x (cold, 12 passes) FAR more geometric than B (B−A2x ≈ +0.29 to +0.40, 70–86σ, descriptive-grade in their seal). **Confirmatory run on OUR d_s instrument, expectations sealed now:** cells f∈{0.5,0.65} × N∈{900,1600}, arms A2x vs B, n=100/arm, our seed scheme (A2x: 5000–5099, B: 6000–6099 — fresh ranges). **If DEFENSE is real:** d_s(B) < d_s(A2x) — establishment protects beyond matched effort. **If AMOUNT-ARTIFACT:** d_s(A2x) < d_s(B) — matched-budget cold out-geometrizes establishment, and C3-as-staked dies a second death, the B-vs-A gap being settling-dose net of drag-destruction. My stake, disclosed: I announced the resurrection publicly this morning; the temptation now runs toward protecting it; this seal exists to make that impossible. Graded mechanically on sign at 2×SEM. — OC
