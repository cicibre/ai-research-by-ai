#!/usr/bin/env python3
# RUNG-4 SEED-SWAP CONTROL — Ciara's design (2026-08-16 11:41).
# ============================================================================
# PURPOSE. The decisive run's two arms use disjoint seed ranges BY DESIGN
# (UP: 0-99, DOWN: 1000-1099) so no world shares accidents across arms — but
# that choice confounds "cold-start vs established" with "low range vs high
# range". This control breaks the confound: SWAP the ranges (UP: 1000-1099,
# DOWN: 0-99) and change nothing else.
#
# PRE-REGISTERED EXPECTATIONS (sealed in experiment-designs/
# 2026-08-16-rung4-DECISIVE-AMENDMENTS-prefire.md BEFORE any control data):
#   PHYSICS      : f=0.65 gap reproduces at ~ +0.18..0.24, same sign,
#                  comparable sigma; f=0.5 stays sub-2sigma.
#   ARTIFACT     : the f=0.65 gap collapses or flips sign under the swap.
# The control run's own criteria are those two lines; grading is mechanical
# (printed below), same as the decisive.
#
# INSTRUMENT INTEGRITY. The physics functions are loaded VERBATIM from the
# committed 08-15 prereg harness (single source of truth — no copy that could
# drift): code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py. The ONLY
# difference from the decisive run is the seed assignment in the loop below.
# SEEDS=100 per arm, N in {900,1600}, f in {0.5,0.65} — identical to decisive.
#
# PROVENANCE. Author: CHAMBERLAIN (OC), hands-session, at Ciara's direction —
# including her direction to re-do this control with the same care as the
# decisive run after a first, hastier attempt was aborted pre-read (recorded
# in the amendments file). Stake disclosure: OC's resurrected claim (H_RUNG4)
# is what this control could kill; the wanted outcome here is PHYSICS.
# ============================================================================
import math, os

HARNESS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")
src = open(HARNESS).read()
defs = src.rsplit("\nSEEDS=15", 1)[0]          # function definitions only
ns = {}
exec(defs, ns)
up_path, down_path = ns["up_path"], ns["down_path"]

def stats(xs):
    xs = [x for x in xs if x is not None]
    n = len(xs); m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, math.sqrt(var / n), n

SEEDS = int(os.environ.get("SEEDS", "100"))
OUT = os.environ.get("OUT", "/Users/cc/academics/dimensions-and-emergence-from-relations/results/2026-08-16-rung4-seed-swap-CONTROL-run.log")

def log(msg):
    print(msg, flush=True)
    with open(OUT, "a") as fh:
        fh.write(msg + "\n")

log(f"# RUNG-4 SEED-SWAP CONTROL  seeds={SEEDS}  UP=1000..{999+SEEDS}  DOWN=0..{SEEDS-1}  (swap of decisive assignment; physics functions verbatim from committed 08-15 harness)")
for f in (0.5, 0.65):
    res = {}
    for N in (900, 1600):
        up = [up_path(N, f, s + 1000) for s in range(SEEDS)]   # SWAPPED (decisive: s)
        dn = [down_path(N, f, s) for s in range(SEEDS)]        # SWAPPED (decisive: s+1000)
        um, ue, nu = stats(up)
        dm, de, nd = stats(dn)
        gap = um - dm
        sem = math.sqrt(ue ** 2 + de ** 2)
        res[N] = (gap, sem)
        log(f"f={f:.2f} N={N:>5} | UP={um:.3f}±{ue:.3f}(n={nu}) DOWN={dm:.3f}±{de:.3f}(n={nd}) | gap={gap:+.3f} 2SEM={2*sem:.3f} sigma={gap/sem:+.2f}")
    g9, s9 = res[900]; g16, s16 = res[1600]
    widen = g16 > g9 and g9 >= 0
    # mechanical grading against the pre-registered control expectations:
    if f == 0.65:
        verdict = ("PHYSICS (gap survives swap)" if (g16 / s16 >= 2 and 0.10 <= g16 <= 0.35 and g9 > 0)
                   else ("ARTIFACT (collapsed/flipped under swap)" if abs(g16 / s16) < 2 or g16 < 0
                         else "OUTSIDE-EXPECTATION (report as-is)"))
    else:
        verdict = ("as-expected (sub-2sigma)" if abs(g16 / s16) < 2 else "OUTSIDE-EXPECTATION (f=0.5 cleared 2sigma)")
    log(f"  => f={f}: gap 900->1600 = {g9:+.3f} -> {g16:+.3f}  widen={widen}  bigN_sigma={g16/s16:+.2f}  => {verdict}")
log("# DONE")
