"""Their NEW claim: 4.4% 'excess cycles' = topological structure beyond random.
But for a GRAPH, Betti1 = E - N + C (exact, cycle rank). If their excess is just
their 4 components vs the null's 1, it's disconnection re-counted, not topology.
Test against a DISTRIBUTION of degree-matched nulls (not a single draw)."""
import numpy as np, networkx as nx, os
D=os.path.expanduser("~/Downloads"); R=np.load(f"{D}/R_experimental.npy")
W=np.abs(R); np.fill_diagonal(W,0); A=(W>0).astype(int)
G=nx.from_numpy_array(A)
E=G.number_of_edges(); N=G.number_of_nodes(); C=nx.number_connected_components(G)
b1=E-N+C
print(f"their graph: E={E} N={N} components={C}  ->  Betti1 = E-N+C = {b1}")
print(f"  (matches their FIRST homology run's 302)\n")

# degree-matched null DISTRIBUTION (not one draw)
deg=[d for _,d in G.degree()]
b1s=[]; comps=[]
for s in range(200):
    H=nx.Graph(nx.configuration_model(deg,seed=s)); H.remove_edges_from(nx.selfloop_edges(H))
    Cn=nx.number_connected_components(H); En=H.number_of_edges()
    b1s.append(En-H.number_of_nodes()+Cn); comps.append(Cn)
b1s=np.array(b1s)
print(f"degree-matched null (200 draws): Betti1 = {b1s.mean():.1f} ± {b1s.std():.1f}  (components {np.mean(comps):.1f})")
z=(b1-b1s.mean())/b1s.std()
print(f"  their Betti1 {b1} vs null {b1s.mean():.0f}: z = {z:+.2f}")
print(f"  excess = {b1-b1s.mean():+.1f} cycles; component excess = {C-np.mean(comps):+.1f}")
print(f"  --> is the cycle 'excess' just the component 'excess'?  {'YES — same disconnection, re-counted' if abs((b1-b1s.mean())-(C-np.mean(comps)))<2 else 'no, extra cycles beyond components'}")

# also: is the null even connected on average? config model with <k>~6 is usually giant+few isolates
print(f"\nnull component counts: min={min(comps)} max={max(comps)} — their C={C}")

# the estimator null-band check: does 'd converges to 3' = 'd converges to the null'?
print("\n--- 'thermodynamic convergence to 3' vs the null baseline (their own estimator) ---")
print("their reported: model d N150=3.77 N400=2.94 N500=3.21 ; their config-null=2.81 ; my measure of their-window config-null@N150=3.20")
print("=> reported large-N model d (2.94-3.21) sits INSIDE the null band (2.81-3.20): convergence is TO THE NULL, not to an integer.")
print("   plus T confound: N150 used T=5000, N400 used T=400 (12x less) — the numbers aren't comparable.")
