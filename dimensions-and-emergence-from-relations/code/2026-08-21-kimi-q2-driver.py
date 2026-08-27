#!/usr/bin/env python3
# KIMI Q2 driver — settling-intensity sweep, our arm, per preserved seal 4c378f3.
# Usage: driver.py <S_triad> <seed_offset>
import json, os, sys, random, math
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune, ov = ns["rgg"], ns["rewire"], ns["grow_prune"], ns["ov"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
cascade, local_c = bh["cascade"], bh["local_c"]

N, T, K = 900, 10000, 3
S_triad, soff = int(sys.argv[1]), int(sys.argv[2])
seed = 81000 + S_triad * 20 + soff
rng = random.Random(seed)

def settle_pass_n(adj, rng, n_triad):
    # single pass of grow_prune's two-step, parameterized (the experiment's knob):
    nodes = list(range(N)); rng.shuffle(nodes); added = 0
    for u in nodes[:n_triad]:
        nb = list(adj[u])
        if len(nb) < 2: continue
        x, y = rng.sample(nb, 2)
        if y not in adj[x]: adj[x].add(y); adj[y].add(x); added += 1
    edges = [(min(a, b), max(a, b)) for a in range(N) for b in adj[a] if a < b]
    edges.sort(key=lambda e: ov(adj, e[0], e[1])); pr = 0
    for a, b in edges:
        if pr >= added: break
        if b in adj[a] and len(adj[a]) > 2 and len(adj[b]) > 2:
            adj[a].discard(b); adj[b].discard(a); pr += 1
    return adj

def mean_c(adj):
    tot = 0.0; n2 = 0
    for v in range(N):
        if len(adj[v]) >= 2: n2 += 1; tot += local_c(adj, v)
    return tot / n2 if n2 else 0.0

adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)   # standard init (S=225 six-pass)
burns, Cs = [], []
for t in range(T):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = cascade(adj, rng, touched)
    adj = settle_pass_n(adj, rng, S_triad)
    burn += cascade(adj, rng, range(N))
    burns.append(burn)
    if t % 10 == 0: Cs.append(round(mean_c(adj), 5))
out = os.path.join(HERE, "..", "results", "kimi-q2", f"S{S_triad}_{soff}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"S": S_triad, "seed": seed, "burns": burns, "C10": Cs}, open(out, "w"))
print(f"S={S_triad} seed={seed} done max={max(burns)} finalC={Cs[-1]}")
