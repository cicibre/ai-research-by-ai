#!/usr/bin/env python3
# MATCHED-BUDGET CHECK — A2x vs B on OUR d_s. Seal: academics amendments file (12:30).
import math
src = open('/Users/cc/academics/dimensions-and-emergence-from-relations/code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py').read()
defs = src.rsplit('\nSEEDS=15', 1)[0]
ns = {}; exec(defs, ns)
sd_, rgg, rewire, grow_prune = ns['spectral_dim'], ns['rgg'], ns['rewire'], ns['grow_prune']
import random as _r
def path_A2x(N, f, seed):
    rng=_r.Random(seed); adj=grow_prune(rewire(rgg(N,rng), f, rng), rng); adj=grow_prune(adj, rng)
    return sd_(adj, seed=seed*7+3)
def path_B(N, f, seed):
    rng=_r.Random(seed)
    adj=grow_prune(rewire(rgg(N,rng), 1.0, rng), rng)
    adj=grow_prune(rewire(adj, f, rng), rng)
    return sd_(adj, seed=seed*7+2)
def stats(xs):
    xs=[x for x in xs if x is not None]; n=len(xs); m=sum(xs)/n
    var=sum((x-m)**2 for x in xs)/(n-1); return m, math.sqrt(var/n), n
print("# MATCHED-BUDGET CHECK  A2x(seeds 5000-5099) vs B(6000-6099)  n=100/arm  our d_s", flush=True)
for f in (0.5, 0.65):
    for N in (900, 1600):
        a2=[path_A2x(N,f,5000+s) for s in range(100)]
        b =[path_B(N,f,6000+s) for s in range(100)]
        am,ae,_=stats(a2); bm,be,_=stats(b)
        diff=bm-am; sem=math.sqrt(ae**2+be**2)
        sign = "DEFENSE (B<A2x)" if diff < -2*sem else ("AMOUNT-ARTIFACT (A2x<B)" if diff > 2*sem else "within noise")
        print(f"f={f:.2f} N={N:>5} | A2x={am:.3f}±{ae:.3f} B={bm:.3f}±{be:.3f} | B-A2x={diff:+.3f} sigma={diff/sem:+.2f} => {sign}", flush=True)
print("# DONE")
