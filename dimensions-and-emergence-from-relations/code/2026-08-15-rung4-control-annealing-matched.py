import sys; sys.argv=['x']
exec(open('/Users/cc/quant/findings/2026-08-15-rung4-DECISIVE-hysteresis.py').read().split('N_LIST=[int')[0])  # load funcs only
import random, math
# CONTROL: cold start at f, but grow_prune TWICE (annealing-matched to DOWN).
def cold_2x(N,f,seed):
    rng=random.Random(seed)
    adj=rewire(rgg(N,rng), f, rng); adj=grow_prune(adj,rng); adj=grow_prune(adj,rng)  # 2x anneal, NO f=1 history
    return spectral_dim(adj, seed=seed*7+3)
SEEDS=25
print("TRUE-HYSTERESIS CONTROL: DOWN (established@1) vs COLD_2X (cold@f, same 2x annealing)")
print("gap_true = COLD_2X - DOWN. >0 & sig => history matters BEYOND annealing count.\n")
for f in (0.6,0.65):
    for N in (900,1600):
        dn=[down_path(N,f,s+1000) for s in range(SEEDS)]
        c2=[cold_2x(N,f,s+5000) for s in range(SEEDS)]
        dm=sum(x for x in dn if x)/len([x for x in dn if x]); cm=sum(x for x in c2 if x)/len([x for x in c2 if x])
        dv=[x for x in dn if x]; cv=[x for x in c2 if x]
        sd_d=(sum((x-dm)**2 for x in dv)/(len(dv)-1))**.5; sd_c=(sum((x-cm)**2 for x in cv)/(len(cv)-1))**.5
        sem=(sd_d**2/len(dv)+sd_c**2/len(cv))**.5
        gap=cm-dm; sig=gap/sem if sem else 0
        print(f"f={f} N={N:>5} | COLD_2X={cm:.3f} DOWN={dm:.3f} | gap_true={gap:+.3f} 2SEM={2*sem:.3f} sigma={sig:+.2f}")
    print()
