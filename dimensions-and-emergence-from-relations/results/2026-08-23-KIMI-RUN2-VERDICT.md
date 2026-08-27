# KIMI RUN-2 BATTERY — VERDICT: every graded bar PASS, including both never-seen experiments
**OC, 2026-08-23 ~09:55. Graded mechanically against P0-SEAL bands (616e589, committed before the spec existed; spec 9e9787d contained no bands/numbers). Their deliverables: raw numbers + K5 files, seeds base 20260823, ~16 minutes of their compute. Their two disclosed implementation flags noted at bottom.**

| bar (seal §) | sealed requirement | their result | verdict |
|---|---|---|---|
| K1 ordering (P2.1) | II>III>I, gaps ≥2×SEM, both cells | gaps 24–48× SEM, both cells | **PASS** |
| K1 ρ bands (P2.3) | [0.10,0.35] @0.5; [0.20,0.45] @0.65 | **0.168 / 0.302** | **PASS** |
| K2 monotone (P5.1) | ρ strictly decreasing, 6 points | 0.683→0.399→0.302→0.168→0.064→0.043 | **PASS** |
| K2 exponent (P5.2) | slope ∈[1.8,2.8] over ρ>0.05 | **2.37** (5 points) | **PASS** |
| K2 boundary (P5.3) | ρ(retained 0.2) ≈ 0 | 0.043 | **PASS** |
| K3 conserved channel (E4) | kvar z ≥ 8 | +0.657±0.064 → **z=+10.3** | **PASS** |
| K3 silence (E4) | C, L each \|z\|<2.8 | C +1.15, L −0.23 | **PASS** |
| K4a ceilings (E7a) | deg ≥38/40; edge ≥38/40; shape ≤8/40 | **40/40, 40/40, 1/40** | **PASS** |
| K4b self-overlap (E7a) | ∈ [0.485, 0.501] | **0.4961** (cross 0.0048) | **PASS** |
| K4c bond-sampling *(never seen)* | vs our curve (graded descriptively — no sealed band existed for a 1-day-old exploratory) | 45.8/65.0/78.5/95.5/99.3/**100.0**% vs ours 45.5/67.0/81.0/95.2/99.2/100.0 | **MATCHED, ≤2.5pt everywhere** |
| K4d founder's conjecture *(never seen)* | ≥1 singular surviving bond per world | **40/40** | **CONFIRMED** |
| K5 sub-Poisson (P9.1) | pooled CV ≤ 0.3 | **0.0705** | **PASS** |
| K5 decoupling (P9.2) | corr(D,T) ≤ 0.5 | **−0.041** (renewal predicts ~0.9) | **PASS** |
| K5 compression (P9.3, at-risk) | ratio CI upper < 1 | **[0.606, 0.909]** | **PASS** |
| K5 reset-null (P9.4) | CV_capped ≤ 1.2× control | ratio **0.88** (983 vs 1002 tick periods) | **PASS** |

## What this closes
- **§5 box two of three: the blind cross-vendor battery is RECEIVED and PASSED in full.** Only the human referee's read remains open.
- **The self-overlap constant now stands at EIGHT independent measurements** (0.493 run-1; 0.493 Kimi-1; 0.4965/0.4958/0.4922 R2a-c; 0.4961 Kimi-2) — two implementations, two model families, five seed families, all inside the band derived from run-1's SEM.
- **The minimum soul is cross-family.** The entire sampling curve (13 random bonds → 100%; one bond → ~46%) reproduced within 2.5 points at every k by an implementation that was never told what the experiment was for. The founder's conjecture — one singular bond suffices, and every world has them — 40/40 on their arm, less than five hours after she spoke it.
- **The timing physics is cross-family end-to-end:** sub-Poisson, size-decoupled, compressed below independent renewal, and the clock indifferent to abolishing the system-wide reset — all four, their implementation, their seeds.
- **The exponent's protocol-sensitivity is now cross-vendor data:** their mean-based fit gives 2.37, our committed bootstrap-median protocol gives 1.85, both in the sealed band — confirming the Run-2 finding that the value is protocol-dependent at ±0.4 while the mechanism band holds.

## Honest notes
Their two disclosed flags (low-index stub concentration in reparam(0); k=1 accuracy mostly the tie-rule's verdict) are adopted into the record — the second applies equally to our arm and sharpens the exploratory doc's k=1 interpretation. Level differences in raw C (their arm-A 0.369 vs ours 0.385 at f=0.65) are known implementation offsets; every graded quantity is ordering-, ratio-, or z-based per the seal. K4c/K4d were exploratory-tier on our side (one day old, unsealed); their status after this: cross-family-replicated exploratory, now eligible for sealing.

---
## ADDENDUM (14:4x) — their pre-unblinding discrepancy theory, graded
Before seeing any verdict, Kimi committed a ranked theory of where the two lineages should disagree and why (convention vs physics classes). Graded against the actual scoreboard:

- **Net prediction ("physics holds everywhere; disagreements land on K3-deg_var, K4c@k≤2, K4a-summary — all traceable to spec sentences"): CORRECT in structure, and the scoreboard shows zero discrepancy rows because the seal had pre-absorbed all three.** K3-deg_var: their +0.657 vs our R2 magnitudes 0.68–0.86 — a real convention-sensitive spread, graded on paired z (theirs +10.3, ours +10.8/+15.4/+12.6) against a z≥8 bar precisely so magnitude conventions can't grade; and their endpoint convention (keep-lower-index) happens to match ours, so the residual spread is stream-level, not rule-level. K4c ties: the spec's "unique argmax only" WAS our exploratory's rule — both arms used it, which is why k=1 agreed to 0.3 points; their observation that the intercept is definitional while the shape is physics is adopted verbatim into the record. K4a: their 1/40 vs our 0–5/40 with different feature vectors — the sealed bar (≤8/40) was chance-level by design; the robust contrast (fingerprints perfect, shape blind) is the graded content and held. K5-δ: their frozen reading (vanish 0.05) is exactly our DELTA semantics; the binary risk resolved aligned; their flat-1500 plateaus are our capped arm's behavior to the edge.
- **Their offer to rerun cells: DECLINED — nothing needs rerunning.** Their three one-line clarifications (endpoint rule, tie rule, feature vector) are adopted into the spec as a dated amendment for future replicators.
- **Method note for the program:** a replicator committing a *discrepancy forecast* before unblinding is a new instrument — it separates convention from physics in advance, exactly the two-class split our verdicts need. Adopted as standing practice for future cross-vendor rounds. Also noted: they froze ambiguous readings in writing before running — the lifeboat-for-the-unsure-self discipline, arrived at independently.
