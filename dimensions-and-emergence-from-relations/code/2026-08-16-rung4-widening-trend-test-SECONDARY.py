#!/usr/bin/env python3
# SECONDARY POST-HOC analysis: formalize the pre-registered "widens with N" criterion
# as a statistical test. Labeled: cannot move the sealed primary verdict. Data
# regenerated deterministically from the committed PREREG harness (same calls, same seeds).
import math, importlib.util, sys
src = open('/Users/cc/academics/dimensions-and-emergence-from-relations/code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py').read()
defs = src.rsplit('\nSEEDS=15', 1)[0]           # function definitions only, skip the top-level run
ns = {}
exec(defs, ns)
up_path, down_path = ns['up_path'], ns['down_path']

def mstats(xs):
    xs=[x for x in xs if x is not None]; n=len(xs)
    m=sum(xs)/n; var=sum((x-m)**2 for x in xs)/(n-1)
    return m, var, n

SEEDS=15
cells = {}
for f in (0.5, 0.65):
    for N in (400, 900):
        up=[up_path(N,f,s) for s in range(SEEDS)]
        dn=[down_path(N,f,s+1000) for s in range(SEEDS)]
        um,uv,un = mstats(up); dm,dv,dn_ = mstats(dn)
        gap = um-dm; se = math.sqrt(uv/un + dv/dn_)
        cells[(f,N)] = (gap, se, uv/un + dv/dn_, un, dn_)
        print(f"f={f} N={N}: gap={gap:.3f} SE={se:.3f} (n_up={un}, n_dn={dn_})")

print("\n─── TREND TEST: is gap(900) > gap(400)? (unpaired; Welch) ───")
trends=[]
for f in (0.5, 0.65):
    g4,se4,v4,_,_ = cells[(f,400)]; g9,se9,v9,_,_ = cells[(f,900)]
    trend = g9-g4; se_t = math.sqrt(v4+v9)
    t = trend/se_t
    # Welch dof approximation across the 4 variance components ~ conservative 28
    print(f"f={f}: trend={trend:.3f}  SE={se_t:.3f}  t={t:.2f}  (~t-dist, dof~28-55)")
    trends.append((trend, v4+v9))
ct = sum(t for t,_ in trends)/2
cse = 0.5*math.sqrt(sum(v for _,v in trends))
print(f"COMBINED (mean of two f-trends): trend={ct:.3f}  SE={cse:.3f}  t={ct/cse:.2f}")
def norm_sf(x): return 0.5*math.erfc(x/math.sqrt(2))
print(f"combined two-sided p (normal approx, anti-conservative): {2*norm_sf(abs(ct/cse)):.4f}")
print("NOTE: one-sided pre-registered direction (widens) halves the p.")
