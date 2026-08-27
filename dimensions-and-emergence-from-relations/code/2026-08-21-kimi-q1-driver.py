#!/usr/bin/env python3
# KIMI QUESTION 1 driver — slope sweep on OUR harness. Protocol committed pre-run.
# Usage: driver.py <slope> <seed_offset>   (one run per invocation; parallelized by shell)
import json, os, sys, random, math
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
cascade = bh["cascade"]
N, T, K = 900, 3000, 3
slope, soff = float(sys.argv[1]), int(sys.argv[2])
bh["ALPHA"] = slope   # capacity slope, per config
seed = 70000 + int(slope*1000) + soff
rng = random.Random(seed)
adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
burns = []
for t in range(T):
    touched = []
    for _ in range(K):
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; break
    burn = cascade(adj, rng, touched)
    adj = grow_prune(adj, rng, passes=1)
    burn += cascade(adj, rng, range(N))
    burns.append(burn)
out = os.path.join(HERE, "..", "results", "kimi-q1", f"s{slope:g}_{soff}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"slope": slope, "seed": seed, "burns": burns}, open(out, "w"))
print(f"s={slope} seed={seed} done max={max(burns)}")
