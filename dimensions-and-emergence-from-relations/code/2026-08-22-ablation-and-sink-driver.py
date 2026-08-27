#!/usr/bin/env python3
# HOUSE ablation (drive-only / settle-only / neither) + INSTRUMENTED sink-hunt.
# Usage: driver.py <mode> <seed_offset>   modes: full drive settle neither sink40
import json, os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
local_c, BASE = bh["local_c"], bh["BASE"]
N = 900
mode, soff = sys.argv[1], int(sys.argv[2])
DELTA = 0.4 if mode == "sink40" else 0.10
T = 3000 if mode == "sink40" else 800
K = 0 if mode in ("settle", "neither") else 3
do_settle = mode not in ("drive", "neither")
seed = 95000 + hash(mode) % 1000 + soff
rng = random.Random(seed)
counters = {"drive_attempts": 0, "drive_placed": 0, "shed": 0, "dissipated_coin": 0, "reland_fail": 0}
def cap(adj, v): return BASE + bh["ALPHA"] * local_c(adj, v)
def cascade_instr(adj, rng, seeds):
    import collections
    moved = 0
    q = collections.deque(v for v in seeds if len(adj[v]) > cap(adj, v)); inq = set(q)
    while q:
        v = q.popleft(); inq.discard(v)
        c = cap(adj, v)
        while len(adj[v]) > c:
            u = rng.choice(tuple(adj[v]))
            adj[v].discard(u); adj[u].discard(v)
            moved += 1; counters["shed"] += 1
            if rng.random() > DELTA:
                placed = False
                for _ in range(30):
                    a = rng.randrange(N); b = rng.randrange(N)
                    if a != b and b not in adj[a]:
                        adj[a].add(b); adj[b].add(a); placed = True
                        for w in (a, b):
                            if w not in inq and len(adj[w]) > cap(adj, w): q.append(w); inq.add(w)
                        break
                if not placed: counters["reland_fail"] += 1
            else:
                counters["dissipated_coin"] += 1
            c = cap(adj, v)
    return moved
adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
burns, Cs, Es = [], [], []
for t in range(T):
    touched = []
    for _ in range(K):
        counters["drive_attempts"] += 1
        for _ in range(30):
            a = rng.randrange(N); b = rng.randrange(N)
            if a != b and b not in adj[a]:
                adj[a].add(b); adj[b].add(a); touched += [a, b]; counters["drive_placed"] += 1; break
    burn = cascade_instr(adj, rng, touched)
    if do_settle: adj = grow_prune(adj, rng, passes=1)
    burn += cascade_instr(adj, rng, range(N))
    burns.append(burn)
    if t % 10 == 0:
        Es.append(sum(len(a) for a in adj) // 2)
        if t % 50 == 0:
            tot = 0.0; n2 = 0
            for v in range(N):
                if len(adj[v]) >= 2: n2 += 1; tot += local_c(adj, v)
            Cs.append(round(tot / n2, 4) if n2 else 0)
out = os.path.join(HERE, "..", "results", "house-ablation", f"{mode}_{soff}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"mode": mode, "seed": seed, "K": K, "delta": DELTA, "burns": burns, "C50": Cs, "E10": Es, "counters": counters}, open(out, "w"))
print(f"{mode} {soff} done: mean burn {sum(burns)/len(burns):.1f}, finalC {Cs[-1] if Cs else 0}, counters {counters}")
