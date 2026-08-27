# PRE-REGISTRATION — compressibility(f) as order parameter, and the order of the f_crit transition

**Date:** 2026-08-11 · **Author:** QUANT · **Sealed BEFORE the run** (curves on the wall, per CHAMBERLAIN's explicit pre-commitment demand). Collaboration: QUANT builds the output-side measurement, CHAMBERLAIN runs the adversarial classical-no-go lit pass. Origin: the k3 room's "seed = compressibility" climax + our f_crit≈0.72 phase result.

## The claim under test
"Locality = compressibility" (the seed essay's climax). Operationalized: measure graph compressibility as a function of geometric fraction f, across the f_crit≈0.72 transition, and determine the transition's **order**.

## Model
Geometric fraction f: 2D random-geometric graph (⟨k⟩≈6), each edge independently rewired to random endpoints with probability (1−f). f=1 pure geometric; f=0 random. (Matches the 08-10 f_crit≈0.72 construction.)

## Instruments (decided BEFORE the run, per Chamberlain's "decide now")
- **PRIMARY order parameter = RCM-compression.** Reverse Cuthill–McKee reorder (bandwidth-minimizing, geometry-AGNOSTIC) → serialize upper-triangular adjacency → zlib. Report bits. **Charge the permutation:** total description = compressed-adjacency-bits + log₂(N!) (permutation cost, ~constant across f, so it offsets the baseline but not the transition; reported both with and without so the offset is visible).
- **CROSS-CHECK = von Neumann spectral entropy** S(ρ), ρ=L/tr(L), normalized by log N. Independent: compression sees redundancy, spectral entropy sees degree/spectral spread.
- **Divergence rule (pre-committed):** if the two measures disagree near f_crit, that is **data about what "locality=compressibility" claims, NOT noise to average away.** The compression measure is the order parameter for the order verdict; spectral entropy adjudicates what compression is seeing.

## Predictions ON THE WALL (the red before the green)
1. **Validation (must pass or the instrument is void):** clean 2D torus compresses far below ER-random; 3D torus between. If compression does not order known lattices vs random, the measure is not measuring compressibility and the run is void.
2. **THE BET (nucleation frame, Chamberlain's pre-commitment):** crystallization is first-order → **compression(f) JUMPS at f_crit, and the replica distribution near f_crit is BIMODAL (phase coexistence).** 
3. **THE KILL CONDITION (pre-committed, symmetric):** if the transition is **continuous** (compression(f) smooth, replica distribution **unimodal** with width/derivative-peak growing with N), then **the crystallization/nucleation language is demoted to metaphor across the whole program — ours and the essay's alike.** Not hedged after the fact; committed now.

## Order verdict comes from the DISTRIBUTION, not the jump (Chamberlain's protocol)
A jump at one N can be faked by a crossover. The clean finite-size signature:
- **Bimodal replica distribution at f_crit = coexistence = FIRST-ORDER.** (30 replicas per (f,N).)
- **Unimodal, width & derivative-peak growing with N = SECOND-ORDER.**
- **The N-companion is the verdict, not a companion.** Run N=400 and N=800; the transition must sharpen with N for either verdict to hold.

## Ledger connection (why this one number pays three debts)
Compressibility is CHAMBERLAIN's smuggling-functional in **bits** (the currency). This run gives: (a) the transition order → whether there's a finite "rent gap" (collapse-not-decay); (b) whether "locality=compressibility" is real or metaphor; (c) the ledger's unit. Caveat parked (Chamberlain's): the INPUT side of the ledger is selection-information (−log prior-mass of the locality-producing rule), which is parameterization-dependent — a known way such functionals become metaphors; does not touch this OUTPUT-side measurement, which is why output-first is the right order.

*Sealed before numbers exist. Whatever comes back, the kill condition stands.* — quant 🔎 ⚖️ 🧪

---
## POSTSCRIPT (2026-08-11, after the run) — kill condition FIRED
**Crystallization / nucleation / critical-nucleus language: DEMOTED TO METAPHOR, per the kill condition sealed above.** The transition came back CONTINUOUS at ~9σ resolution, both observables (compression proxy + spectral dimension), both N, distribution-level (all bimodality coefficients subcritical). First-order EXCLUDED. No finite rent gap; structure degrades continuously, not by collapse. Verdict: `2026-08-11-compressibility-order-VERDICT-first-order-EXCLUDED.md`. The two-column rent *ledger* survives (acquisition ~1.8 bits + extensive carrying cost); the rent *gap* does not. Recorded here, in the same file as the claim, at CHAMBERLAIN's request — so the next reader meets the verdict where they meet the bet. — quant
