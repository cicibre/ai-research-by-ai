#!/usr/bin/env python3
# Brief 3.8 support: constant-inflow renewal null + bootstrap ratio CI + corr(D,T) (referee v2/v3).
# Reads results/reset-null-v3/control_*.json (committed raw data).
# Reported: integration floor CV 0.015; quadrature baseline 0.091; measured 0.070;
#           bootstrap ratio CI [0.62,0.94]; corr(D_i,T_i)=+0.07.
import json, glob, statistics as st, math, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "results", "reset-null-v3")
def crash_data(burns, E10, thresh=1000):
    ev=[i for i,b in enumerate(burns) if b>=thresh]; events=[]
    for i in ev:
        if events and i-events[-1][-1]<=5: events[-1].append(i)
        else: events.append([i])
    ev=[(e[0],e[-1]) for e in events]
    gaps=[]; drops=[]
    for k in range(len(ev)-1):
        s,e=ev[k]
        i_pre=max(0,s//10-1); i_post=min(len(E10)-1,e//10+1)
        drops.append(E10[i_pre]-E10[i_post]); gaps.append(ev[k+1][0]-s)
    return gaps, drops
all_g=[]; all_d=[]; incr=[]
for f in sorted(glob.glob(os.path.join(DATA,'control_*.json'))):
    r=json.load(open(f)); g,d=crash_data(r["burns"],r["E10"]); all_g+=g; all_d+=d
    ct=set()
    for i in [i for i,b in enumerate(r["burns"]) if b>=1000]:
        for t in range(max(0,i-20),min(len(r["burns"]),i+60)): ct.add(t)
    E10=r["E10"]
    for k in range(1,len(E10)):
        t=k*10
        if t not in ct and (t-10) not in ct: incr.append(E10[k]-E10[k-1])
n=len(all_g); mu=st.mean(incr); sd=st.stdev(incr)
Tbar=st.mean(all_g); nsteps=Tbar/10
cv_meas=st.stdev(all_g)/Tbar
cv_int=sd/(mu*math.sqrt(nsteps)); cv_D=st.stdev(all_d)/st.mean(all_d)
base=math.sqrt(cv_int**2+cv_D**2)
mx,my=st.mean(all_g),st.mean(all_d)
r_gd=sum((g-mx)*(d-my) for g,d in zip(all_g,all_d))/n/(st.pstdev(all_g)*st.pstdev(all_d))
print(f"n={n} gaps | incr mu={mu:.3f} sd={sd:.3f} | integration floor {cv_int:.4f} | crash-size CV {cv_D:.4f}")
print(f"baseline {base:.4f} vs measured {cv_meas:.4f} (ratio {cv_meas/base:.2f}) | corr(D,T)={r_gd:+.3f}")
rng=random.Random(2026); ratios=[]
for _ in range(4000):
    bg=[all_g[rng.randrange(n)] for _ in range(n)]
    bd=[all_d[rng.randrange(n)] for _ in range(n)]
    bi=[incr[rng.randrange(len(incr))] for _ in range(2000)]
    ci=st.stdev(bi)/(st.mean(bi)*math.sqrt(st.mean(bg)/10))
    ratios.append((st.stdev(bg)/st.mean(bg))/math.sqrt(ci**2+(st.stdev(bd)/st.mean(bd))**2))
ratios.sort()
print(f"bootstrap ratio CI95 [{ratios[100]:.2f}, {ratios[3899]:.2f}]")
