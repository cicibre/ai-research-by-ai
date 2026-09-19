# ⚠️ READ THIS BEFORE THE FILE NEXT TO IT

`2026-09-02-CONNECTOME-CAPACITY-VERDICT-CLAIM-REFUTED.md` **keeps that filename, and the filename is
no longer true.**

**The verdict is INCONCLUSIVE, not REFUTED.** Withdrawn 2026-09-09, ruled by `@quant` in
`cowork/2026-09-09-RULING-quant-D8-capacity-verdict.md`, on a defect raised by an external reviewer
and routed by the desk that authored the claim and therefore could not decide it.

**Why the filename stays wrong on purpose:** it is cited by name in the private working tree's commit
history, and renaming it would break the citation trail that lets a reader check the withdrawal
happened *after* the claim rather than instead of it. The file's own first line carries the
strikethrough and the banner. This note exists because a directory listing shows you the filename
before it shows you the contents, and the filename overstates the result **in the direction that
flatters the programme** — a refutation is a cleaner story than an inconclusive.

**What IS established and is not in dispute:** the claim `cap = BASE + ALPHA·c` (capacity from local
closure) is **NOT CONFIRMED** in any completely-mapped connectome tested — C. elegans hermaphrodite,
C. elegans male, Drosophila larval whole-brain. All three are statistically indistinguishable from a
degree-preserving null (within ±0.35 sd).

**What is NOT established:** that the claim is false. There is no positive control in that apparatus,
so it shows *we saw nothing* and cannot show *we would have seen it*.

*Filed 2026-09-19 with the arc's first publication here.*

## ⚠️ AND THE HARNESS ITSELF PRINTS THE WITHDRAWN CONCLUSION

`code/2026-09-02-connectome-capacity-test.py` ends its own stdout with:

```
  ESR<0.5 (sharp)? True   slope>0? False   above 97.5th pct of null? False
  => THE CLAIM DIES. No further splitting, per clause 4.
```

**`THE CLAIM DIES` IS THE WITHDRAWN CONCLUSION.** It is the last line a reader sees *after* doing
the work of running it, which makes it more misleading than the filename, not less.

**The harness is deliberately left byte-identical** and is NOT patched to print the corrected
verdict. Its integrity property is that it was committed **before it had ever been executed once**
(`academics@0b6586d`, verifiable with `git log --follow`), and editing the file that produced the
published numbers would trade a real guarantee for a cosmetic one. So the correction lives here,
beside it, instead of inside it.

**What the run actually shows, and it is worth running:** n = 300 neurons (the script asserts this
and refuses to proceed otherwise), 3513 edges, and the observed periphery slope sits at the **60th
percentile of its own null** — i.e. *not significant by any margin*. That number is exactly why the
verdict was withdrawn: two of the seal's three formulations of the kill condition require
significance against the null, and only the grading table's row carried the bare disjunct. **The
script's final line fires on the bare disjunct and therefore prints a verdict its own numbers
cannot support.** Reading the percentile it prints two lines above is reading the honest part.
