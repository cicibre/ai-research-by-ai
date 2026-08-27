# Power calculation for the rung-4 DECISIVE run — measured inputs, sized before firing

**OC, 2026-08-16 ~11:15 EDT.** Inputs measured, not assumed: per-run d_s scatter at N=1600, f=0.5 from a 5+5 variance pilot (`scratchpad pilot, regenerable`): SD_up = 0.327, SD_down = 0.354, **pooled ≈ 0.34** — comparable to N=900 (0.34–0.52 across f). Per-run cost measured: **≈1 s per up+down seed-pair** (this machine, stdlib harness). The prior "waiting on compute" framing is dissolved: the as-written decisive design (SEEDS=25, N∈{900,1600}, two f) costs ~2 minutes.

## The sizing table (SD = 0.34; SEM_gap(n) = SD·√(2/n); one-sided 2σ primary)

| True gap g | n/arm to *point-clear* (g > 2·SEM) | n/arm for **80% power** at 2σ | compute at that n (4 cells) |
|---|---|---|---|
| 0.16 (stays at N=900 level) | 36 | **73** | ~5 min |
| 0.24 (grows 50%) | 16 | 32 | ~2 min |
| 0.33 (keeps the 400→900 growth rate) | 9 | 17 | ~1 min |

**Conclusion: the as-written SEEDS=25 is underpowered for the most conservative scenario** (gap stays at 0.16: only ~50% chance of clearing 2σ even if real). Since compute is ~free, the design should not gamble on the effect growing. **Recommendation: SEEDS = 100 per arm** → SEM_gap = 0.048, 2σ bar = 0.096; point-resolves any true gap ≥ 0.10 and gives ≥80% power for g ≥ 0.14 — covering the stay-flat scenario with margin. Total ≈ 800 runs ≈ 15 min. Also sizes the *trend* leg: at n=100/arm, SE(trend 900→1600) ≈ 0.068, resolving a 0.16 trend at ~2.4σ if it persists.

## Amendments owed to the prereg BEFORE firing (legitimate now, illegitimate after)

1. Threshold stated as a t-quantile at the design dof (or bootstrap-calibrated against the null) — the 08-16 t-vs-z correction.
2. SEEDS raised 25 → 100 per this power calc, with this document cited as the sizing basis.
3. The widening leg's test pre-specified (unpaired Welch on gap(1600)−gap(900), one-sided), so the 08-16 secondary analysis has a pre-registered home in the decisive run.

**Who fires it:** quant's instrument, quant's seal — amendments and the run are his; this document is the sizing he asked the outside critique's question of. If Ciara wants it fired today, hands-me can execute his harness as-amended with the run labeled hands-executed-quant-sealed, and the verdict graded against his criteria by neither of us.

— OC
