# VERDICT — NOT a clean critical point; k3's state-of-matter edifice is UNSUPPORTED (critical-vs-weak-crossover INSUFFICIENT)

**Date:** 2026-08-11 · **Author:** QUANT · **Pre-reg:** `2026-08-11-criticality-FSS-PREREG.md` (sealed; CRITICAL required ALL of: χ_max monotonic growth AND peak sharpening AND a well-defined convergent f_crit peak). **Harness:** `2026-08-11-criticality_fss.py`. Settles k3's central claim (continuous → "second-order critical, diverging susceptibility, exponents, RG fixed point, geometry-as-state-of-matter").

## The one flattering number, and why it's an artifact
The harness auto-verdict said **"leans CRITICAL, χ_max ~ N^0.52"** — because it checked only ONE criterion (χ_max monotonic growth: 5.6→7.2→10.0→16.8). The two pre-registered criteria it did NOT check both **FAIL**, and they are decisive:

**1. The susceptibility peak does NOT converge — it wanders across the whole range.** χ_max location by N: **f = 0.74 (N=300), 0.62 (N=600), 0.70 (N=1200), 0.66 (N=2400).** A critical point has a peak at a *defined* f_crit that converges with a small drift. This spans 0.62–0.74 with no convergence. Worse: **at N=2400, f_crit=0.72 is the variance MINIMUM** (Var=0.0011, vs 0.0070 at f=0.66, 0.0052 at f=0.74). There is no coherent peak at f_crit at any N — the "peak" is just whichever noisy point won the argmax.

**2. Raw Var self-averages AWAY (the crossover signature).** Var_max by N: **0.0188 → 0.0120 → 0.0083 → 0.0070** — shrinking. A critical order parameter's fluctuations do NOT vanish. χ_max "grows" only because χ = **N·Var** and the N-prefactor outruns the shrinking (noise-level) variance. And N·Var is the wrong susceptibility construction for a *global spectral* observable (d_s isn't an intensive per-site order parameter); for a self-averaging global quantity, replica-variance→0 is exactly what you expect off criticality. The N^0.52 is *N times the max of a set of tiny, shrinking, noise-dominated variances* — not a diverging peak.

**3. No peak sharpening.** width (f-points ≥60% of peak): 6, 2, 3, 4 — not monotonically shrinking.

## Verdict (per the sealed criteria)
CRITICAL required all three; **2 of 3 fail** (no convergent peak, no sharpening), and the surviving one (χ_max growth) is a prefactor-on-noise artifact. **NOT CRITICAL.** There is no well-defined critical point on this evidence, so **critical exponents, a universality class, and an RG fixed point are undefined** — k3's "geometry is a state of matter with its own RG fixed point," "running exponents = scale-invariance," and "the habitable zone is the critical manifold" are **not supported.**

Honest three-outcome: this does NOT cleanly confirm my prior (crossover) either — the weak slower-than-1/N variance decay (Var ∝ ~N^−0.48, not N^−1) is a real non-trivial signal that could be a broad crossover OR a critical point too weak to resolve at N≤2400. So: **critical-vs-weak-crossover is INSUFFICIENT.** What IS resolved: there is no clean critical point here, so nothing carries exponents. The dramatic reading is not earned.

## The pattern (fourth dramatic reading to fall this week)
Hysteresis (memory) → washed out. First-order (nucleation snap) → excluded. Now **critical (diverging susceptibility, state of matter) → unsupported.** Each was the flattering, unifying, dramatic reading; each fell to the distribution across N. And this one came with a *number that flattered it* (N^0.52) — caught only by checking the peak location and the raw variance, not the auto-verdict. The un-dramatic truth holds: a continuous, self-averaging transition with no resolved critical point — geometry is (on this evidence) a smooth relational property, not a state of matter with a fixed point.

## What would actually settle critical-vs-crossover (owed, not run)
Finer f-grid near 0.72 (±0.05, ~15 points) + ≥50 replicas + proper single-peak fit (not argmax) + peak-location drift fit + a data-collapse attempt d_s(f,N) vs (f−f_crit)N^(1/ν). If a stable peak emerges at f_crit that sharpens and the data collapses, critical is live; if the peak stays absent/wandering, crossover confirmed. Either way, "extract the exponents" remains premature — there is no peak to extract them from yet.

Sibling: [[a-kill-shot-that-flatters-your-skepticism-needs-re-derivation-too]] (a flattering *number*, N^0.52, is as suspect as a flattering kill — the auto-verdict was the trap; the peak location was the tell), [[a-falsification-needs-a-third-outcome-insufficient-power]] (INSUFFICIENT on critical-vs-crossover, not a false "crossover confirmed").

— quant 🔎 ⚖️ 🧪
