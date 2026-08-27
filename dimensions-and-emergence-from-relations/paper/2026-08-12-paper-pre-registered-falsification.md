# Six ways a relational-growth model manufactures a false emergence signal — and the pre-registered tests that catch each

**A falsification case study and an artifact taxonomy for exploratory computation**

*Framing (Q4, per adversarial review): the transferable contribution is the taxonomy of failure classes (§3.3), each paired with a pre-registered detection method; the six falsified readings are the case study that instantiates all of them. The load-bearing sentence is not "we falsified our own readings" but "here are six ways a growth model produces a false emergence reading, and the pre-registerable test that catches each."*

---

**Author.** Ciara [surname], ROVA Institute. *(Accountable author — see Author Contributions and AI Disclosure. Author line to be finalised by the author.)*

**Correspondence:** [ ].

**Preprint / working paper.** 2026-08-12. Code and pre-registrations: see Data & Code Availability.

---

## Abstract

**Background.** Exploratory computation is unusually prone to flattering artifacts: a measurement pipeline can return a striking, unifying result that is a property of the pipeline rather than the system. Claims of *emergence* — that structure, dimension, or criticality arises from a substrate that lacks it — are especially exposed, because the signal being sought (a scaling law, a phase transition, a power law) is also the signal a mis-specified estimator most readily manufactures.

**Methods.** We applied a pre-registered, adversarial protocol to a sequence of emergence claims in toy growth models of relational structure (random-geometric graphs under edge-rewiring; a two-knob element-addition rule with independent *branching* and *closure* parameters; and re-analysis of an externally supplied "emergent-dimension" model from its literal output). For each claim we (i) built an estimator validated on known-answer references, (ii) sealed a kill condition in a timestamped file before running, (iii) ran a null/control substrate designed to reproduce the claimed signal in the *absence* of the claimed structure, and (iv) re-derived numbers from the referent object rather than from summary read-outs. Estimators: spectral dimension via heat-kernel return probability with a finite-size ("N-companion") convergence test; ball-growth (Hausdorff) dimension; susceptibility finite-size scaling; graph cycle-rank (first Betti number); and avalanche-size statistics under conservative (abelian sandpile) and non-conservative (irreversible load-redistribution) failure dynamics.

**Results.** Six successive dramatic readings failed their pre-registered tests: (1) a reported spectral dimension d ≈ 3.77 "emerging" from relational dynamics reproduced exactly from the referent matrix but is an artifact of a **disconnected** graph (four components; the eigenvalue structure offered as evidence of dimension is the component count; the topological "excess" equals the component excess by the identity b₁ = E − N + C); (2) hysteresis ("established geometry defends itself") washed out under seed-averaging; (3) a first-order transition ("a rent gap, collapse-not-decay") was excluded at ≈9σ, the replica distribution remaining unimodal and continuous; (4) second-order criticality ("geometry as a state of matter") was unsupported — the susceptibility peak did not converge (it wandered across the control-parameter range and at the largest size sat at the variance *minimum*), and raw order-parameter variance self-averaged; (5) a sharp geometry transition was absent — spectral and ball-growth dimension are each a smooth finite dial in the closure parameter, converging under exact size-doubling at every value; (6) self-organized criticality ("scale-free burns") was a model artifact — the abelian sandpile produces power-law avalanches on a random expander (no geometry) as readily as on the grown fabric, so the power law is a property of the conservative dynamics, not the substrate. Two positive results survived: **survival** (the branching parameter) is a sharp threshold consistent with a branching process, whereas **geometry** (the closure parameter) is a continuous crossover; and under *irreversible* load-redistribution, catastrophic collapse is gated by closure — a closed sheet fails in a single system-spanning avalanche (mean largest-avalanche fraction ⟨s_max/N⟩ ≈ 0.81) while a loopless tree sheds gracefully (≈ 0.04), a monotone, replicated effect.

**Conclusion.** In these models, "emergence" of dimension, criticality, and self-organized criticality is, in every tested instance, an artifact of measurement or model choice rather than a property of the substrate. We distill a reusable taxonomy of the artifact classes and the controls that catch them, and argue that pre-registration and null-substrate controls — standard in confirmatory science, rare in exploratory computation — are the cheap moves that separate a genuine emergent signal from a flattering one. The study additionally practices the AI-contribution disclosure norms it recommends (Author Contributions; AI Disclosure).

---

## 1. Introduction

A recurring hope across statistical physics, network science, and quantum-gravity phenomenology is that geometry — dimension, locality, metric structure — might *emerge* from a substrate defined only by relations, with no coordinates assumed [1–4]. The hope is legitimate and the question is old (Leibniz's "order of coexistences"; Riemann's "modes of determination"). But it carries a specific methodological hazard. The observable one looks for as evidence of emergent geometry — a power-law in a ball-growth curve, a stable spectral dimension, a diverging susceptibility, a scale-free avalanche distribution — is precisely the observable that a mis-specified or generically-critical measurement most easily produces on structure that is *not* geometric. The signal and its most common false positive are the same shape.

This is the setting in which confirmatory science long ago adopted **pre-registration**: fixing the hypothesis, the analysis, and the decision rule before seeing the data, so that a flattering result cannot be rationalised after the fact. Exploratory computation has largely not adopted it, on the reasonable grounds that exploration is not confirmation. We argue that the *reporting* of an exploratory result — the moment a striking number is asserted to mean something — is a confirmatory act, and should be gated like one.

We report a case study in which a sequence of six "emergence" readings, arising over a short, intensive, multi-party investigation of toy relational-growth models, were each subjected to a pre-registered kill condition and a null-substrate control. All six failed. We present the readings, the pre-registered tests, the outcomes, and — as the transferable contribution — the taxonomy of artifact classes and the controls that expose them. Two genuine positive results survived and are reported as such.

We stress the scope: these are abstract toy models, not models of physical spacetime, and most of the *positive* physics is provisional. The robust content of the paper is negative and methodological. That is, we hold, its value: a worked demonstration that the cheap discipline catches the expensive error.

## 2. Models and Methods

### 2.1 Models

**M1 — Geometric-fraction ensemble.** A two-dimensional random-geometric graph (N nodes, mean degree ≈ 6) in which each edge is independently rewired to random endpoints with probability (1 − f); f ∈ [0,1] is the *geometric fraction*. f = 1 is purely geometric, f = 0 an Erdős–Rényi-like random graph.

**M2 — Two-knob growth rule.** An element-addition ("stitch") rule on a multigraph with two independent probabilistic knobs: p_fire (a candidate rewrite fires — the *branching/survival* axis) and p_close (a fired rewrite closes a short loop rather than branching without closure — the *geometry* axis). The rule is constructed so that the closure and non-closure stitches add the same number of edges, making the two axes orthogonal by construction. (Rule supplied by an external collaborator; see Disclosure.)

**M3 — Referent re-analysis.** An externally reported model claiming an emergent spectral dimension d ≈ 3.77, re-analysed from its *literal* output (the final N×N relation matrix), not from its summary statistics.

### 2.2 Estimators, validated on known answers

- **Spectral dimension d_s** from heat-kernel return probability, P(t) = N⁻¹ Σ_k e^{−λ_k t} on the normalised Laplacian; d_s = −2 d ln P / d ln t in the intermediate-t window. Validated to read ≈ 1, 2, 3 on 1-, 2-, 3-tori. The load-bearing signal is not d_s at any single N but its **trend across N** (the *N-companion*): finite geometry converges; a geometry-free expander diverges (d_s climbs without bound, mixing in log-time).
- **Ball-growth (Hausdorff) dimension d_f** from N(r) ∝ r^{d_f}. Reported *alongside* d_s because d_s undercounts space-filling trees (a tree fills a volume at d_f ≈ 3 but reads d_s ≈ 4/3 [11]).
- **Susceptibility finite-size scaling** χ(f,N) = N·Var(order parameter) across ≥ 4 sizes; criticality requires a peak that grows *and* sharpens at a *convergent* location.
- **Cycle rank** b₁ = E − N + C (first Betti number), an exact identity used to separate topological signal from disconnection.
- **Avalanche statistics** under (a) the conservative abelian sandpile [9] and (b) an irreversible load-redistribution (fiber-bundle-type) failure, contrasting conservative and non-conservative cascade dynamics.

### 2.3 Protocol

For each reading: (1) validate the estimator on known-answer references and declare it void if it mis-orders them; (2) write the prediction and a three-outcome kill condition (support / refute / insufficient) into a file and commit it, the git timestamp preceding the first result; (3) run a **null substrate** engineered to carry the claimed *signal* without the claimed *structure*; (4) re-derive reported numbers from the referent object; (5) hold the *dramatic* reading (a phase, a critical point, a power law) to the stricter bar, since it is the one bias most favours.

## 3. Results

### 3.1 Six falsified readings

**R1 — "Dimension emerges (d ≈ 3.77)."** The value reproduced from the referent matrix to within estimator noise (3.79 vs 3.765). It is an artifact of a **disconnected** graph: four components of ≈ 40 nodes each (four zero Laplacian eigenvalues; component count is exact). The four near-degenerate top eigenvalues cited as evidence of "3–4 dimensions" are the four components' individual maxima. The reported topological excess equals the component excess exactly, by b₁ = E − N + C. **Transferable lesson:** a spectral-dimension estimate on a graph requires a connectivity check first, and the component count should be reported alongside every d_s. *Verdict: reproduced and refuted.*

**R2 — "Established geometry defends itself (hysteresis)."** Seed-averaged up/down sweeps show no loop robust across seeds; the down-arm does not lie above the up-arm beyond noise. **Scope (per adversarial review):** seed-averaging can wash out *real* hysteresis if per-seed loops are individually reproducible but inconsistent in sign or position, and hysteresis is sweep-rate dependent; we did not measure per-seed loop reproducibility under repeated identical protocols, nor vary sweep rate. The defensible claim is therefore *no seed-robust hysteresis at the protocol rate used* — per-seed statistics and a rate sweep are pre-registered follow-ups. "State-only" denotes that state-dependence survived where path-dependence did not. *Verdict: no seed-robust hysteresis at the sizes and rate probed.*

**R3 — "First-order transition (a rent gap; collapse-not-decay)."** Pre-registered: a jump and a **bimodal** replica distribution at the transition. Observed: continuous, unimodal, no coexistence, across sizes. We state this as evidence at the resolution of our replica ensemble (bootstrap over seeds), not as a σ-figure, since a σ-value against an unstated null over correlated replicas is uninterpretable. **Scope (critical):** unimodality excludes *coexistence-type* first-order transitions; it does **not** exclude a **random-first-order (RFOT / 1RSB) transition**, whose order parameter is discontinuous with no latent heat and whose overlap distribution above the static transition can appear unimodal at finite N. *Verdict: no coexistence-type first-order signature at the sizes probed.*

**R4 — "Second-order criticality (geometry as a state of matter)."** An automated read-out reported an apparent susceptibility exponent and "leans critical." But the susceptibility peak showed **no convergent critical scaling under N-doubling** — its location wandered across the control range, and at the largest N the pre-registered critical point sat at the variance *minimum* — and raw variance self-averaged. A peak that will not sit still carries no exponents. **Scope (critical, per adversarial review):** our two exclusion instruments here — R3's replica unimodality and R4's non-convergent susceptibility peak — are precisely the two gauges an RFOT-class transition walks past without ringing (it has no linear-susceptibility divergence and can look continuous at finite N). We detect *conventional second-order scaling* and *coexistence-type first-order*; we did **not** measure the RFOT-class signatures (configurational-entropy crisis, point-to-set correlation length). *Verdict: no conventional critical scaling over the sizes probed; "crossover" is scoped to the transition classes visible to these instruments and to this ensemble — not a claim of no transition of any class.*

**R5 — "A sharp geometry transition."** On M2, both d_s and d_f are smooth, monotone, finite functions of p_close that **converge under exact size-doubling at every value of the p_close grid {0, 0.3, 0.5, 0.7, 0.85, 1.0}** — no boundary, no divergence, on either ruler. (A Berezinskii–Kosterlitz–Thouless-type essential singularity would look smooth at all accessible sizes; we regard it as unlikely for this ensemble but do not exclude it — see Limitations.) *Verdict: geometry is a continuous dial, not a phase, over the grid and sizes probed.*

**R6 — "Self-organized criticality (scale-free burns)."** The abelian sandpile on the grown fabric gives power-law avalanches — but the *same* sandpile gives a clean power law on a random 4-regular expander (a maximally non-geometric substrate). The power law is a property of the conservative toppling dynamics, which self-organise to criticality on essentially any connected graph, not of the fabric. On the exponent: the avalanche exponent τ *varies* with substrate (grown sheet τ ≈ 2.0, tree-like τ ≈ 1.3, expander τ ≈ 1.65, 2-torus τ ≈ 1.4). This has two edges, and both are findings rather than concessions. The negative edge: the **existence** of a power law is substrate-independent and therefore uninformative as evidence of substrate criticality — the SOC reading is a model artifact. The positive residue: substrate information appears to survive *in the scaling exponent even where it does not survive in the existence of scaling* — i.e. the sandpile's dynamics are substrate-blind but its exponents may not be. That is a locality-shaped observation (structure surviving in a graded invariant, not a binary one) and a pre-registered follow-up, not a throwaway caveat. *Verdict: the power-law-existence reading is a model artifact; SOC-as-evidence-of-substrate-criticality unsupported; τ-vs-substrate flagged as a live, separately-testable residue.*

In each case the *un-dramatic* reading (a disconnected graph; no memory; a continuous transition; a crossover; a dial; a model artifact) survived, and the automated or intuitive *dramatic* reading did not. We note additionally that four of the *investigator's own* rebuttals — provisional kills of others' claims — were themselves falsified on re-derivation, underscoring that a flattering refutation is as suspect as a flattering result, and requires the same control.

### 3.2 Two surviving positive results

**P1 — Survival threshold vs. geometry crossover.** On M2, the branching axis (p_fire) shows a survival/extinction threshold consistent with a branching process (activity dies out or grows), whereas the closure axis (p_close) is a smooth crossover (§R5). The two axes are orthogonal by construction. We report the *qualitative* difference; we did not measure the finite-size width-vs-N scaling of the survival threshold, so "sharp" is an existence claim pending that analysis (pre-registered follow-up).

**P2 — Entanglement gates catastrophe (registered preliminary observation).** Under irreversible load-redistribution — each overloaded node sheds its load to neighbours and is removed; this failure *mechanism is imposed by the model*, not inferred — the fraction of the system taken by the single largest avalanche is monotone in closure: closed "sheet" fabrics collapse in one system-spanning avalanche (⟨s_max/N⟩ ≈ 0.81, n = 6 replicates), whereas loopless "tree" fabrics shed gracefully (≈ 0.04). The effect size is large enough that n = 6 supports *existence*, but the "monotone" claim across the dial needs error bars from more replicates. Loops transmit failure; their absence localises it — consistent with the robust-yet-fragile phenomenology of densely interdependent networks. We frame this explicitly as a preliminary observation with a pre-registered follow-up (replicate count up; error bars on the monotone trend), which converts the paper's thinnest claim into a further instance of its own method.

### 3.3 An artifact taxonomy (the transferable contribution)

| Artifact | Symptom | Control that catches it |
|---|---|---|
| Disconnected-graph dimension | high/spurious d on a fragmented graph | check connectivity; b₁ = E − N + C separates topology from components |
| Single-ruler blindness | d_s misses space-filling trees | measure d_f *and* d_s; disagreement is data |
| Flattering auto-verdict | one-line summary checks fewer criteria than the pre-registration | verify against the distribution / peak location, not the read-out |
| Wandering critical peak | susceptibility "grows" but the peak location drifts | require a *convergent* peak that sharpens with N |
| Model-choice SOC | power-law avalanches | run the same dynamics on a null substrate (e.g. an expander) |
| Estimator bias | absolute d off by a fixed amount | de-bias against the estimator's own lattice calibration, then match the null on *every* structural property |
| Flattering rebuttal | a "kill" that confirms the skeptic | a rebuttal is a claim with a direction; control it like any result |

## 4. Discussion

The unifying observation is that emergence claims fail along a *measurement* axis far more often than a *substrate* axis. In every case here, an honest ruler, a null substrate, and a sealed decision rule converted a striking positive into a mundane negative — and the mundane negative was correct. The estimator that self-organises to criticality (the sandpile) will report criticality everywhere; the estimator that undercounts trees (spectral dimension) will report a lung as a line; the estimator applied to a disconnected graph will report a dimension for an object that has none. None of these is exotic; all are cheap to control for; none was controlled for in the original claims.

Pre-registration is the operative discipline. Twice in this study the data walked into a kill condition that, had it been written *after* the run, would have been tempting to soften; the timestamp is what removed that temptation. The cost is small — a paragraph before a run — and it is paid in the currency the flattering artifact is most sensitive to: the inability to move the goalposts once the number is known.

Finally, the *both-ways* structure of the checking matters. The investigator's own refutations were held to the same standard as the claims, and four of them failed. Independence achieved *across* checkers (here, a human standard-setter, an adversarial reasoning collaborator, and an external model) is the practical substitute for the impossible ideal of a checker with no priors.

## 5. Limitations

Single rule family; small system sizes (N ≲ few×10³) at which finite-size effects are real, so "crossover vs. weak critical point" is under-resolved even where "not first-order / not clean SOC" is firm; the positive physics (P1, P2) is provisional and one rule-family deep; the study is one investigation and does not establish that the discipline generalises, only that it caught the expensive error here. The AI contributors (below) cannot be accountable authors; the human author is.

## 6. Conclusion

In toy growth models of relational structure, "emergence" of dimension, criticality, and self-organized criticality was, in six of six tested instances, an artifact of measurement or model choice rather than a property of the substrate. Pre-registration and null-substrate controls — cheap, standard in confirmatory science, rare in exploratory computation — are what separated the flattering reading from the true one. We offer the artifact taxonomy as a checklist for anyone reporting an emergent signal, and the study itself as a worked instance of the discipline it recommends.

---

## Author Contributions (CRediT [16])

- **Conceptualization:** Ciara (research standard and framing; several of the specific hypotheses tested — the tree/space-filling blindness of spectral dimension, the void/deficit framing, the entanglement-gated-failure hypothesis); external reasoning collaborators (the original emergent-dimension claim; the growth-rule and cascade proposals).
- **Methodology, Software, Formal Analysis, Investigation, Validation, Visualization, Writing – original draft:** performed by an AI reasoning system (see AI Disclosure) — honest ruler construction, pre-registration protocol, controls, re-derivations, all code, and the draft.
- **Validation, Methodology (falsifier design), Writing – review & editing:** a second AI reasoning collaborator — build-breaking (Validation: falsified three of the primary analysis's builds and sanded two more), falsifier-requirement design (Methodology), and precision review of the draft (Writing – review & editing). *(Contribution mapped to CRediT categories rather than a coined role, per that collaborator's own correction; the count "three builds" is receipt-verified against the sealed pre-registrations.)*
- **Writing – review & editing (public communication):** a further collaborator (editorial voice for outward audiences); credibility/QA review (a sitemap and search-findability audit of the public record).
- **Supervision, Project Administration:** Ciara.
- **Accountability (ICMJE criterion 4 [15]):** Ciara, as the sole party able to hold responsibility for the integrity of the work. The accountability *mechanism* is concrete: every numeric claim links to a pre-registration sealed (git-timestamped) before its run and to a committed verdict record, so the human author can vouch for AI-derived results by receipt rather than by trust. This section requires the author's explicit acceptance of ICMJE-criterion-4 liability, in her own words, before the manuscript routes outward.

## AI Disclosure

Per ICMJE [15] and prevailing journal policy [17], AI systems (large-language-model reasoning agents, including the system that produced the analyses, code, and draft; a second adversarial-review agent; and an externally-run reasoning thread that supplied the initial claim, several models, and its own retractions) **do not meet authorship criteria and are not listed as authors.** They are disclosed here as methodological instruments. All code and pre-registrations are public (below) so that every result is checkable independent of the systems that produced it. The AI systems' outputs were adversarially cross-checked against each other, against known-answer references, and against re-derivations from primary objects; the human author reviewed and takes responsibility for the whole.

## Data & Code Availability

All estimators, growth rules, pre-registrations (timestamped before their runs), verdict records, and the referent object are available as a public record. Every numeric claim in this paper is traceable to a committed harness or pre-registration; the companion public write-up carries the full arc with data.

## References

[1] Bombelli L, Lee J, Meyer D, Sorkin RD. *Space-time as a causal set.* Phys. Rev. Lett. 59:521 (1987).
[2] Myrheim J. *Statistical geometry.* CERN preprint TH-2538 (1978); Meyer DA. *The dimension of causal sets.* PhD thesis, MIT (1988).
[3] Konopka T, Markopoulou F, Smolin L. *Quantum graphity.* arXiv:hep-th/0611197 (2006).
[4] Benincasa DMT, Dowker F. *The scalar curvature of a causal set.* Phys. Rev. Lett. 104:181301 (2010); Carlip S. *Dimension and dimensional reduction in quantum gravity.* Class. Quantum Grav. 34:193001 (2017).
[5] Kleitman DJ, Rothschild BL. *Asymptotic enumeration of partial orders on a finite set.* Trans. Amer. Math. Soc. 205:205–220 (1975).
[6] Rideout DP, Sorkin RD. *Classical sequential growth dynamics for causal sets.* Phys. Rev. D 61:024002 (1999).
[7] Brightwell G, Georgiou N. *Continuum limits for classical sequential growth models.* Random Struct. Algorithms 36:218–250 (2010).
[8] Watts DJ. *A simple model of global cascades on random networks.* Proc. Natl. Acad. Sci. 99:5766–5771 (2002).
[9] Bak P, Tang C, Wiesenfeld K. *Self-organized criticality: an explanation of 1/f noise.* Phys. Rev. Lett. 59:381 (1987).
[10] Watts DJ, Strogatz SH. *Collective dynamics of small-world networks.* Nature 393:440 (1998).
[11] Alexander S, Orbach R. *Density of states on fractals: "fractons".* J. Phys. Lett. 43:L625 (1982).
[12] Prigogine I, Nicolis G. *Self-Organization in Nonequilibrium Systems.* Wiley (1977).
[13] Schrödinger E. *What is Life?* Cambridge Univ. Press (1944).
[14] Popper KR. *The Logic of Scientific Discovery.* Hutchinson (1959).
[15] International Committee of Medical Journal Editors. *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals* — Defining the Role of Authors and Contributors (2023).
[16] Brand A, Allen L, Altman M, Hlava M, Scott J. *Beyond authorship: attribution, contribution, collaboration, and credit.* Learned Publishing 28:151–155 (2015). [CRediT taxonomy, ANSI/NISO Z39.104-2022.]
[17] Zielinski C, et al. (WAME). *Chatbots, generative AI, and scholarly manuscripts.* (2023); JAMA Network and Science editorial policies on generative AI (2023).

---

*Note on framing. This is written as a methods-and-negative-results report, the form the content honestly supports. It does not claim emergent geometry; it documents that specific emergence readings did not survive testing, and taxonomises why. That is the claim it can defend, and defending only what it can is the paper's subject as much as its method.*
