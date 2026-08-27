# Reproducing the results — map from brief to code

Everything is deterministic: seeded stdlib PRNG, no dependencies beyond Python 3.9+ (one legacy script uses numpy; nothing in the brief depends on it). Every world rebuilds exactly from its seed. Layout: `code/` harnesses+analyses · `experiment-designs/` pre-registrations (the seals — each committed BEFORE its data; verify with `git log --follow <file>`) · `results/` raw logs and JSON telemetry · `paper/` the briefs · `cowork/` an external reviewer's lab note (verbatim).

| Brief § | Claim | Producer (code/) | Raw data (results/) | ~Runtime |
|---|---|---|---|---|
| 3.1, 3.3 | ordering, killed 6.83σ, matched-budget | `2026-08-15-rung4-DECISIVE-hysteresis.py`, `2026-08-16-rung4-matched-budget-check.py`, `2026-08-16-rung4-seed-swap-CONTROL.py` | `2026-08-16-rung4-DECISIVE-run.log` + verdicts | ~min–hrs |
| 3.2 | erasure + MDEs + kvar survivor | `2026-08-15-Q2-dynamical-observable-test.py`, `2026-08-22-eraser-mde-recheck.py` | Q2 verdict | ~10 min |
| 3.5 | 7× recovery budget (45,600 graphs) | `2026-08-19-qrhofree-v2-…` (see verdict for exact file) | `2026-08-19-qrhofree-v2-RAW.log` | hours |
| 3.6 | ρ vs severity | `2026-08-17` rho-severity harness | `2026-08-17-rho-severity-RAW.log` | ~hour |
| 3.7 | identity 40/40, 0.493 | `2026-08-16-thomas-test.py`, `2026-08-16-mary-test.py` | thomas/mary RAW logs | ~15 min |
| 3.8 law | B=(K−dE/dt)/δ, 30/30 count | `2026-08-21-delta-sweep-driver.py`, `2026-08-22-ablation-and-sink-driver.py` | `delta-sweep/*.json`, `house-ablation/*.json` | ~hour |
| 3.8 tail | CSN power-law discipline | `2026-08-19-tail-analysis-CSN.py` (self-tests first) | `endogenous-burns/` | ~min |
| 3.8 timing | renewal null, CI, corr(D,T), reset ablation | `2026-08-22-timing-null-analysis.py`, `2026-08-22-reset-null-driver.py` | `reset-null-v3/*.json` | analysis: seconds; re-run: ~30 min |
| §2.4 | cross-vendor replication | our seals: `experiment-designs/2026-08-21-*KIMI*`; their implementation is theirs (available on request) | `2026-08-21-*KIMI-VERDICT*` | — |

Quick start (5 minutes, reproduces two headline numbers from scratch):
```
python3 code/2026-08-16-mary-test.py            # -> 40/40, self-Jaccard 0.493
python3 code/2026-08-22-timing-null-analysis.py # -> baseline 0.091 vs measured 0.070, CI [0.62,0.94]
```
The seals are the point: for any claim, read its `experiment-designs/` file first, check its commit predates the data commit, then run the producer.
