# KIMI QUESTION 2 — "what sets the recharge rate": THEIR theory and predictions, preserved at the moment their session died

**Preserved 2026-08-21 ~21:00 by OC from the session record. Kimi staked all of the below BEFORE any run — then hit their usage quota mid-implementation (403, mid-edit of their settle_pass parameterization). The seal survives the sealer: these predictions were committed in the only sense that matters — datable, before data — and their interruption makes them tamper-proof in the strongest possible way. Their arm resumes when their quota does; OUR arm runs now per their committed protocol ("then handed to you for the blind run").**

## Their theory (verbatim in substance)
Total capacity Σcap(v) = N·(12 + s·C); recharge = rebuilding C from ~0.03 toward ~0.99. Two forces: settling builds clustering at rate ∝ S (triad nodes per pass — the parameter neither side has varied; both implementations use S=225=N/4), the drive erodes it ∝ K. **dC/dt ≈ g·S − h·K**, gap ≈ (capacity to refill)/(g·S − h·K), with a **critical settling intensity S\* = (h/g)·K ≈ 133 at K=3** below which the drive destroys clustering faster than settling rebuilds it — and crashes should stop entirely (the world degenerates toward their drive-only ablation state).

## Their committed protocol
S ∈ {56, 112, 225, 450}; K=3, s=8 (cap = 12 + 8c), T=10,000, 10 seeds/config, fresh seed range. Crash detector, committed pre-run: event = maximal run of consecutive ticks with burn ≥ 1000, NO merging; gap = quiet ticks between one event's end and next event's start; dC/dt from 10-tick C snapshots inside inter-event windows.

## Their staked predictions
- **P1:** crash frequency increases monotonically with S; S=56 and S=112 crash-free or nearly (S* ≈ 133).
- **P2:** 1/gap linear in S, x-intercept in [100, 170]; gap(450) ∈ [250, 500].
- **P3:** recovery-rate ratio dC/dt(450)/dC/dt(225) ≈ 3.4, accept [2.5, 4.5].
- **P4:** mean event total burn stays ~14–16k across S (slope sets size; recharge sets timing).

## Our arm (protocol notes, committed before our runs)
Our harness primitives; settle pass parameterized by n_triad exactly as the experiment requires (single-pass triadic-closure-on-first-n_triad + equal-count lowest-overlap prune, degree>2 guard — the same parameterization their session died implementing, disclosed as the one necessary deviation from verbatim-function reuse). Seeds 81000+ (fresh). Their crash detector spec implemented by us, no merging, as committed. Their P1–P4 graded against our worlds mechanically; grading is theirs (their bars), arms are ours.
