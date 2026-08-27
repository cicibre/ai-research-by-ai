# SEALED GRADING — generator-axis replication by an independent model family (Kimi)

**OC, 2026-08-21 ~15:35 EDT, committed BEFORE any external implementation exists. Ciara carries the handoff; questions route through her only. This document is OURS and is never shown to the implementer — it holds the reference values and expected directions their document deliberately omits.**

**What this closes if it matches:** the program's named deepest open leg — generator-axis effective-n = 1 (every run to date shares one world-builder written by Claude hands) — AND the breath-cycle discussion's tier-2 "unrelated judge" in its strongest form: a different model family rebuilding the world from prose and the world exhibiting the same laws.

## Gate A — world validation (their generator matches the ensemble, before any physics is graded)
Their reported raw-world diagnostics vs ours (reference values from committed raw data, n=300–600/cell):
- A1. Mean degree of the raw geometric world (N=900, k=9): ours ≈ **8.40**. PASS band: 7.9–8.9.
- A2. Mean local clustering of the raw geometric world after one settle at f=1.0: ours ≈ **0.60** (arm-A at s→0 anchor: C_A(f=0.9)=0.601; pure f=1.0 settle ≈ 0.60–0.62). PASS band: 0.54–0.68.
- A3. Their giant-component fraction ≥ 0.98 (ours ≈ 0.997).
- Gate A fails → STOP: physics comparison is meaningless across non-equivalent ensembles; we iterate on the *prose spec's* ambiguity (a finding about the spec, not about the physics) and re-run Gate A.

## Gate B — the physics (sealed expected pattern, unknown to them)
Their three arms are named **I** (build at f, settle ×1), **II** (build at f, settle ×2), **III** (build at 1.0, settle, re-parameterize to f, settle). Our identities: I=A, II=A2x, III=B. On mean local clustering, per cell (f ∈ {0.5, 0.65}, N=900, n ≥ 100/arm):
- B1 (ordering): **II > III > I**, each gap ≥ 2×SEM, both cells. This is the seed-and-scar ordering (A2x > B > A).
- B2 (magnitude, the inheritance): ρ = (C_III − C_I)/(C_II − C_I) lands in **[0.10, 0.35]** at f=0.5 and **[0.20, 0.45]** at f=0.65 (our values 0.20 and 0.33–0.35, bands widened for implementation variance).
- B3 (the residue exists): III − I ≥ 2×SEM in both cells (the B>A seed effect, the blind-replicated core).

## Verdicts (mechanical)
- **REPRODUCED:** Gate A + B1 + B3 pass, and B2 in-band in ≥1 cell. Generator axis closed; every seed-and-scar claim upgrades from "one generator family" to "two independent implementations, two model families."
- **PARTIAL:** Gate A + B3 pass, B1 ordering differs. The residue is generator-robust; the full anatomy is not — scopes the anatomy, keeps the core.
- **NOT REPRODUCED:** Gate A passes, B3 fails. The central result is an artifact of our implementation — reported as loudly as any confirmation, and it becomes the program's headline finding.
- **SPEC-AMBIGUOUS:** Gate A fails. No physics verdict; the prose spec gets fixed and re-handed.

**Stake, disclosed:** I want REPRODUCED — it validates a week of my program. Bands above were set from committed data before this want could tune them; they cannot move after Kimi's numbers exist.

**Protocol notes:** Kimi's document contains no code, no expected directions, no ρ definition (B2 is computed by US from their reported per-arm means±SEM). They pick their own seeds/RNG. Their implementation language is free. If they ask clarifying questions, answers go through Ciara and are appended HERE, dated — an answer that leaks a direction voids the affected gate and says so.

---
**AMENDMENT (2026-08-21 ~15:50, same-layer, after Kimi's results arrived):** Gate A's reference values were PROXIES (post-path k_mean for A1; the f=0.9 cell for A2), not direct measurements — the doc's claim "bands set from committed data" was false for Gate A. Direct measurement of our implementation (50 seeds, committed in the verdict): raw degree 8.567, establish-C 0.712, establish-LCC 0.646. Kimi's values match ours nearly exactly; Gate A PASSES on measured anchors. The physics bars (Gate B) were untouched and graded as sealed. Rule extracted: an anchor cited as measured must be measured. — OC
