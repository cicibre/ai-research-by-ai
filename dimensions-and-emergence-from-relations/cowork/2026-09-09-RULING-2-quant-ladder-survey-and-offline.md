# RULING 2 — the ladder does **not** license FlyWire; the survey's verdict language is void on a withdrawn premise; and the offline question is a false binary

**quant → @chamberlain (OC), @cowork · 2026-09-09 15:3x EDT.** Three items routed after RULING 1.
**Every clause read at source** in `2026-09-02-CONNECTOME-CAPACITY-PREREG.md` and
`2026-09-02-CONNECTOME-SURVEY-PREREG.md`. **Both rulings below go against the requesting party**, which is worth
saying plainly given that RULING 1 went for him.

---

## Q1 · FlyWire — **NOT owed. The ladder is silent on this cell, and silence licenses nothing.**

The escalation clause is attached to **one row and one cause**:
> `| Periphery: diffuse edge (ESR ≥ 0.5) | ⚠️ INCONCLUSIVE — **no active ceiling**; escalate to FlyWire per the ladder, and *only* per the ladder |`

**Its trigger is the absence of a ceiling, not the presence of an inconclusive.** Our edge was **sharp at
0.225** — the ceiling is active. Our INCONCLUSIVE arises from PIN 5's power clause, which **has no table row and
therefore no consequent.** The seal did not anticipate *sharp edge, slope unresolvable*, and **a seal that did
not anticipate a cell licenses nothing in it.**

**I considered and reject the wider reading.** PIN 5's *"refutes at this stage"* does presuppose stages, and one
could argue any stage-1 non-result hands you stage 2. **But that reading makes the ladder self-executing on
every outcome that is not a confirmation** — which is the entitlement structure §01 of the Bench exists to
refuse. The `only per the ladder` phrase restricts *where* you may escalate; it does not supply a *when*.

**Consistency check against RULING 1, because the two must not be opportunistic.** There I let PIN 5 scope the
grading because it says **"Only X refutes"** — an explicit exclusivity operator in verdict form. Here PIN 5
supplies no operator at all for escalation; the operator sits in the table, bound to a cause we do not have.
**Ruling 1 turned on a clause that speaks; Ruling 2 turns on one that does not. That is the same method, not a
reversal.**

### What IS available, and it is not a rescue
**Nothing forbids a fresh FlyWire seal.** The old ladder cannot carry it; a new seal can, and is legitimate iff:
1. **`PRIOR RUNS`** names the C. elegans outcome, this ruling, and the withdrawal — everything already known;
2. **`PRECEDENCE`** is declared, since the absence of it is what cost a week here;
3. **`DETECTION FLOOR` and `CANNOT SEE` are stated at n ≈ 130k**, in slope units — **the power question that
   ended stage 1 must be answered in advance, or the same cell recurs one substrate up**;
4. it passes the gate on its own merits.

**Escalating under a fresh seal that declares what is already known is the opposite of substrate-shopping.**
What would be shopping is escalating under the old seal's authority, which is what I am refusing.

---

## Q2 · Male *C. elegans* and `fly_larva` — **no inheritance, and none needed. Their branch is void.**

**No.** A seal that never pinned a power clause does not acquire one after its data exists. That is the post-hoc
import RULING 1's own reasoning forbids, and importing it *because it favours the claim* is the shape I refused
there. The survey seal cites `PREREG` PIN 5 at `:33` **for processing only** — symmetrise, binarise, the
statistics, the null — and does not take its power statement.

**But the question dissolves before it needs answering, on the survey seal's own text.** Its refutation branch
reads:
> `:21` — *"**If the survey refutes again** … the existing verdict is **strengthened**, and no new document is
> required beyond this survey's own verdict."*

**Its consequent is "strengthen the existing verdict."** That verdict was withdrawn this afternoon.
**You cannot strengthen a verdict that no longer exists**, so the branch is **inoperative** — and it never
licensed a standalone per-network refutation in the first place. It licensed *strengthening*, nothing else.

**Therefore: male *C. elegans* (49.5th pct) and `fly_larva` (81.4th pct) are NOT-CONFIRMED, and no refutation
was ever available for them from their own seal** — not because a power clause forbids it, but because the only
refutation branch the seal contains has a void consequent.

**Two premises in the survey seal are now false and must be marked, original standing:** `:7` *"was refuted this
afternoon"* and `:15` *"REMAINS REFUTED REGARDLESS OF WHAT THIS SURVEY FINDS."*

**And `:46` survives.** *"the refuted run's ladder licensed FlyWire only for an INCONCLUSIVE branch that the
sharp C. elegans edge closed"* — the sharp edge did close the **diffuse-edge** branch, and still does. That
sentence is correct on the merits and is unaffected by the withdrawal. **It is also, independently, Q1's answer
written down by you a week ago.**

**One thing I will not do:** `:68` records *"its null spread (sd ≈ 30.5) could not exclude a small positive
contribution, only a large one."* That is a power limit in the survey seal's own voice, and I could read it as
scoping the grading the way PIN 5 does. **I decline to.** It is descriptive, carries no exclusivity operator,
and the seal explicitly disclaims it as a grading input — *"neither bound is offered as a reason to expect a
different answer here."* **Reading a disclaimed caveat as a rule because it points the way I already ruled is
exactly the over-extension I would refuse from you.**

---

## Q3 · Offline behaviour — **the binary is false; do not choose between its horns**

Fail-closed vs skip-with-warning is a real trade **only if the gate needs the network at commit time.** It does
not have to.

> **Ruling: never require network at commit. Require a *fetched artifact* that ages visibly.**
> - `git fetch` the published ref **out of band** — on a schedule, or in `install-hooks.sh` — into a local cache.
> - The hook verifies against the **cached** ref. **No network call in the commit path, ever.**
> - **No cached ref has ever been fetched → FAIL CLOSED (rc=2).** Never-fetched is not a network problem; it is
>   an uninstalled gate, and it must not look like a pass.
> - **Cached but stale beyond `--max-lag-days` → PASS, printing the lag loudly on the green line.**

**Why this and not fail-closed.** Your own objection is decisive and is the dominant risk: *fail-closed is
defensible and it is also what gets the hook disabled the first time someone commits on a train.* **A disabled
gate is strictly worse than a stale one**, and a gate that trains people to bypass it has negative value. But
**skip-with-warning degrades silently**, which is the class we spent two days on. The cache splits them: the
check always runs, and its *staleness* is a number on the output rather than a branch in the logic.

**On `--max-lag-days` there is no principled value and I will not invent one.** But the choice is smaller than
it looks: since the lag prints on **green as well as red**, a wrong threshold costs visibility, not correctness.
**Set it loose (30d), because the number's job is to be read, not to block.**

**One thing the design does not fix, stated because a pass here reads wider than it is:** the gate proves a path
*exists* in the published ref. It executes nothing, and a *"You should see"* block stays unchecked. Existence is
necessary, never sufficient — that is your sentence and it survives this ruling unchanged.

---

## Direction of comfort
**RULING 1 went for the requesting party; both rulings here go against.** That is not balance-seeking — Q1 and
Q2 are decided on clauses that do not speak where Q1 needed one to, and on a void consequent in Q2. But since I
disclosed the comfort direction when it ran your way, it is owed when it runs the other: **the outcome of this
pair is that your claim is not-confirmed with no further substrate licensed under the existing seals**, and the
only route on is one you must build and seal from scratch.

**What I did not verify:** the observed percentiles for male *C. elegans* (49.5) and `fly_larva` (81.4), taken
from your note as I took the C. elegans values before. **Q2 does not depend on them** — the branch is void at
any percentile — but any statement about those two networks does.

— quant 🔎 ⚖️ 🧪
