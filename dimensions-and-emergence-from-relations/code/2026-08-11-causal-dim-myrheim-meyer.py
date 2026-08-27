"""Independent re-derivation of their SECTION 4 (Myrheim-Meyer causal-set dimension).
Sprinkle points UNIFORMLY (Poisson) in an Alexandrov interval of d-dim Minkowski,
give the estimator ONLY the causal relation (hide coordinates), recover d.
This is the setting where they just fixed a 'non-uniform sampling' bug — so I sample
uniform-in-the-interval by rejection (the correct measure) and check the numbers."""
import numpy as np
from scipy.special import gamma
from scipy.optimize import brentq

def myrheim_meyer_r(d):
    return gamma(d+1)*gamma(d/2)/(2*gamma(3*d/2))

def sprinkle_interval(d, n_target, seed):
    """uniform sprinkle in Alexandrov interval between origin and top=(T,0,..0), T=1.
    x=(t, y_1..y_{d-1}) is IN the interval iff origin<x<top:
      future of origin: t > |y|         (timelike separated, t>0)
      past of top:      (T-t) > |y|      (top in future of x)
    rejection-sample uniformly in the bounding box -> uniform in the interval."""
    r = np.random.default_rng(seed); T=1.0; pts=[]
    while len(pts) < n_target:
        m = (n_target-len(pts))*4
        t = r.uniform(0, T, m)
        y = r.uniform(-T/2, T/2, (m, d-1))
        ry = np.sqrt((y**2).sum(1))
        ok = (t > ry) & ((T-t) > ry)
        for i in np.where(ok)[0]:
            pts.append(np.concatenate([[t[i]], y[i]]))
    return np.array(pts[:n_target])

def related_fraction(pts):
    """fraction of pairs that are causally related, from the RELATION ONLY.
    x<y iff dt>0 and dt^2 > |dspatial|^2 (future-timelike)."""
    n=len(pts); t=pts[:,0]; y=pts[:,1:]
    cnt=0
    for i in range(n):
        dt = t - t[i]
        dsp2 = ((y - y[i])**2).sum(1)
        rel = (dt>0) & (dt**2 > dsp2)   # y in future cone of x
        cnt += rel.sum()
    return cnt / (n*(n-1)/2)

print(f"{'true d':>6} {'measured r':>11} {'formula r':>10} {'recovered d':>12}")
for d in [2,3,4]:
    pts = sprinkle_interval(d, 1400, seed=7)
    r_meas = related_fraction(pts)
    r_form = myrheim_meyer_r(d)
    # invert: find d' with mm(d')=r_meas
    try: d_rec = brentq(lambda x: myrheim_meyer_r(x)-r_meas, 0.5, 12)
    except ValueError: d_rec = float('nan')
    print(f"{d:>6} {r_meas:>11.4f} {r_form:>10.4f} {d_rec:>12.2f}")
print("\n(estimator saw only the causal relation table; coordinates hidden. their §4: 2.00/3.03/3.99)")
