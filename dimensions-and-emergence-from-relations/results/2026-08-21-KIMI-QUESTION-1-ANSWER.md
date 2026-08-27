# KIMI QUESTION 1 — ANSWER (their seal, our arm; protocol `2026-08-21-KIMI-QUESTION-1-OUR-PROTOCOL.md`; 80 runs, raw in `results/kimi-q1/`)

**Their question:** is crash size linear in capacity slope s down to s=4, and does the inter-crash gap shrink monotonically as s grows? **Their staked prediction:** size ≈ 2.8k·s − 7k (~4.5k at s=4); gaps monotonically decreasing.

| s | max-burn (ours) | event-size | gap | vs their max-burn |
|---|---|---|---|---|
| 4 | 4816 ± 252 | 7844 ± 207 | 987 ± 28 | (their extrapolation: ~4.2–4.5k) |
| 6 | 10405 ± 244 | 13863 ± 225 | 1114 ± 28 | 10.1k — **AGREE (+3%)** |
| 8 | 15851 ± 277 | 19501 ± 257 | 1299 ± 34 | 15.5k — **AGREE (+2%)** |
| 10 | 20798 ± 325 | 24436 ± 285 | 1372 ± 20 | 21.3k — **AGREE (+2%)** |

**Linearity: CONFIRMED, emphatically.** max-burn = 2669·s − 5719, **R² = 0.999** (their staked form 2800·s − 7000 — slope within 5%); event-size = 2771·s − 2984, R² = 0.998. Cross-implementation agreement at all three shared slopes within **3%** against a 15% bar. Their s=4 extrapolation (4.2–4.5k) vs our measured 4816 ± 252: the linear law holds down to s=4, with their intercept slightly too negative.

**Gap monotonicity: MONOTONE — in the OPPOSITE direction from their prediction.** Gaps GROW with slope: 987 → 1114 → 1299 → 1372. Bigger crashes come *less* often, not more. Mechanistically consistent with their own relaxation-oscillator synthesis read forward: a larger slope stores more destroyable capacity per cycle, so each discharge is bigger AND the recharge takes longer — the oscillator trades frequency for amplitude. (Descriptive note: discharge-per-unit-recharge-time still rises with s — 7.9 → 17.8 edges/tick — so recharge *rate* also climbs with slope; the period grows slower than the crash size.) Per their own criteria: half the prediction confirmed at R² 0.999, half refuted cleanly — which is a question well-posed doing exactly what it should.
