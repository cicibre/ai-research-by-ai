#!/usr/bin/env python3
# RESET-NULL per seal 2026-08-22-RESET-NULL-PREREG.md (99830d6).
# Usage: driver.py <arm> <seed_offset>   arms: control capped
import json, os, sys, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(HERE, "2026-08-15-rung4-trajectory-hysteresis-PREREG.py")).read().rsplit("\nSEEDS=15", 1)[0], ns)
rgg, rewire, grow_prune = ns["rgg"], ns["rewire"], ns["grow_prune"]
bh = {"__file__": os.path.join(HERE, "2026-08-19-endogenous-burn-harness.py")}
exec(open(bh["__file__"]).read().split("def run_world")[0].split("if __name__")[0], bh)
local_c, BASE, ALPHA = bh["local_c"], bh["BASE"], bh["ALPHA"]
N, K, DELTA, T = 900, 3, float(os.environ.get("RN_DELTA", "0.10")), int(os.environ.get("RN_T", "3000"))
arm, soff = sys.argv[1], int(sys.argv[2])
CAP = 1500 if arm == "capped" else 10**9   # per-tick shared shed budget
rng = random.Random(97000 + (0 if arm == "control" else 500) + soff)
def cap_v(adj, v): return BASE + ALPHA * local_c(adj, v)
budget = [0]  # sheds spent this tick
def cascade(adj, rng, seeds):
    moved = 0
    q = collections.deque(v for v in seeds if len(adj[v]) > cap_v(adj, v)); inq = set(q)
    while q:
        if budget[0] >= CAP: return moved   # over-capacity nodes wait for next tick
        v = q.popleft(); inq.discard(v)
        c = cap_v(adj, v)
        while len(adj[v]) > c:
            if budget[0] >= CAP: return moved
            u = rng.choice(tuple(adj[v]))
            adj[v].discard(u); adj[u].discard(v)
            moved += 1; budget[0] += 1
            if rng.random() > DELTA:
                for _ in range(30):
                    a = rng.randrange(N); b = rng.randrange(N)
                    if a != b and b not in adj[a]:
                        adj[a].add(b); adj[b].add(a)
                        for w in (a, b):
                            if w not in inq and len(adj[w]) > cap_v(adj, w): q.append(w); inq.add(w)
                        break
            c = cap_v(adj, v)
    return moved
adj = grow_prune(rewire(rgg(N, rng), 0.65, rng), rng)
burns, Es = [], []
for t in range(T):
    budget[0] = 0
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
    if t % 10 == 0: Es.append(sum(len(a) for a in adj) // 2)
out = os.path.join(HERE, "..", "results", os.environ.get("RN_OUT", "reset-null"), f"{arm}_{soff}.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump({"arm": arm, "cap": CAP, "burns": burns, "E10": Es}, open(out, "w"))
print(f"{arm} {soff} done, mean burn {sum(burns)/len(burns):.1f}, max {max(burns)}")
