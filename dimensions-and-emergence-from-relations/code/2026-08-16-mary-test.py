#!/usr/bin/env python3
# MARY TEST — recognition by surviving relations (edge-set Jaccard). Seal 1053a7b, pre-read.
# Deterministic re-generation of the same 40 worlds; adds edge-set channel to the Thomas design.
import math, random
src = open('/Users/cc/academics/dimensions-and-emergence-from-relations/code/2026-08-15-rung4-trajectory-hysteresis-PREREG.py').read()
ns = {}; exec(src.rsplit('\nSEEDS=15',1)[0], ns)
rgg, rewire, grow_prune = ns['rgg'], ns['rewire'], ns['grow_prune']
N, M, F = 900, 40, 0.65
def edges(adj): return frozenset((a,b) for a in range(N) for b in adj[a] if a<b)
pre_e, post_e = [], []
for i in range(M):
    rng=random.Random(12000+i)
    adj=grow_prune(rewire(rgg(N,rng),1.0,rng),rng)
    pre_e.append(edges(adj))
    adj=grow_prune(rewire(adj,F,rng),rng)
    post_e.append(edges(adj))
def jac(a,b):
    u=len(a|b); return len(a&b)/u if u else 0
hits=sum(1 for i in range(M) if max(range(M), key=lambda j: jac(post_e[i], pre_e[j]))==i)
acc=hits/M
within=sum(jac(post_e[i],pre_e[i]) for i in range(M))/M
cross=sum(jac(post_e[i],pre_e[(i+1)%M]) for i in range(M))/M
verdict = "EDGE-CARRIES (Mary confirmed)" if acc>=0.25 else ("weak" if acc>=0.10 else "chance")
print(f"edge-overlap matching: {hits}/{M} = {acc:.0%} | mean self-Jaccard={within:.3f} vs cross={cross:.3f} | {verdict}")
