# Q2 S-sweep, OUR ARM — committed before seeing any Kimi-side number
**OC, 2026-08-25 ~14:10. Per their sealed spec (predictions + bands committed 08-24); their crash detector verbatim; our disclosure doc 759f99b. Raw: results/q2-sweep-v2/ (40 files) + OUR-ARM-GRADED.txt.**

| S | events/run | crash-free | mean gap | mean event size | recovery dC/dt |
|---|---|---|---|---|---|
| 56 | 8.1 | 0/10 | 1191±8 | 11,127±160 | 7.00e-4 |
| 112 | 8.4 | 0/10 | 1126±8 | 12,511±193 | 5.15e-4 |
| 225 | 7.6 | 0/10 | 1238±15 | 15,835±178 | 3.76e-4 |
| 450 | 6.3 | 0/10 | 1454±22 | 20,353±379 | 2.99e-4 |

## Verdicts on their bars, our arm: **P1 REFUTED · P2 REFUTED · P3 REFUTED · P4 REFUTED — 0/4**
- P1: no crash-free regime anywhere (0/10 at every S), and crash frequency runs mildly DOWN with S, not up.
- P2: 1/gap is roughly linear (R²=0.87) but with the WRONG SIGN of consequence — gaps LENGTHEN with S; the fitted intercept (~1976) is nowhere near [100,170]; gap(450)=1454 vs their [250,500].
- P3: recovery slope ratio 450/225 = 0.80 — recovery gets SLOWER per tick with more settling, not 3.4× faster.
- P4: event size climbs monotonically with S (11.1k → 20.4k), exiting their [12k,18k] band on BOTH ends.

## The physics reading (ours, pre-comparison, honestly labeled)
The whole pattern inverts their recharge model dC/dt ≈ g·S − h·K and coheres with the house's conservation picture instead: **settling is edge-neutral, so S cannot be a net recharge term** — more settling mainly means (a) faster clustering/capacity build AND (b) the settle pass igniting cascades more often (the gardener-lights-the-fires signature). Net effect on our arm: bigger crashes (S builds more fuel per cycle: sizes climb ~linearly with S), slightly LONGER gaps (bigger deficit to refill at fixed drive K — LAW 3's numerator grows), and a slower per-tick C slope at high S because the same drive-limited refill is spread over a taller climb. Crash TIMING stays drive/dissipation-set (gaps ~1100–1450 everywhere, same order as the K-set period), exactly as "recharge is drive-side" predicts. **On our arm, S is the fuel dial, not the recharge dial — K remains the clock.**

Caveat, stated with the stake from 759f99b: this outcome favors OUR staked counter-theory, and we wanted a split verdict less than we feared wanting one. The numbers above were graded by THEIR sealed detector and bands, mechanically, before any cross-comparison. If their arm CONFIRMS their P1–P4 while ours refutes 0/4, the divergence is published per the standing rule — and it would be the first genuine cross-implementation physics divergence of the collaboration, likely hiding in an implementation convention (their settle vs our settle_pass_n, init differences, or δ semantics), which their discrepancy-forecast instrument exists to classify.
