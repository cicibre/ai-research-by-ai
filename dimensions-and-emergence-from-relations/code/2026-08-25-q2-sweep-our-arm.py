#!/usr/bin/env python3
# Q2 S-sweep, our arm, per Kimi spec (q2_spec.md) + our disclosure doc. Usage: driver.py <S> <i>
import json, os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune, ov = ns["rgg"], ns["rewire"], ns["grow_prune"], ns["ov"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
cascade, local_c = bh["cascade"], bh["local_c"]
N, K, T = 900, 3, 10000
S, idx = int(sys.argv[1]), int(sys.argv[2])
seed = 700000 + S * 10 + idx
rng = random.Random(seed)
def settle_pass_n(adj, rng, n_triad):
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
adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
burns, C10, E10 = [], [], []
for t in range(T):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = cascade(adj, rng, touched)
    adj = settle_pass_n(adj, rng, S)
    burn += cascade(adj, rng, range(N))
    burns.append(burn)
    if t % 10 == 0:
        C10.append(round(mean_c(adj), 5))
        E10.append(sum(len(a) for a in adj) // 2)
out = os.path.join(HERE, "..", "results", "q2-sweep-v2", f"S{S}_{idx}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"S": S, "seed": seed, "burns": burns, "C10": C10, "E10": E10}, open(out, "w"))
print(f"S={S} i={idx} done max={max(burns)}", flush=True)
