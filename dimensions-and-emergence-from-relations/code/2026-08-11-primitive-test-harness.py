"""
PRIMITIVE TEST on the honest ruler.
System-under-test: Ciara/ChatGPT relational-closure model (reconstructed from a
truncated paste; every reconstructed line is flagged >>> RECON).
Ruler: spectral dimension d_s (heat-kernel return prob), validated on lattices,
with the N-companion (does d_s plateau converge or climb with N?) and a
degree-matched null (double-edge-swap, degree sequence preserved).

PRE-REGISTERED PREDICTION (on the wall before the run):
  A non-local closure substrate has no geometric majority to define 'local'
  against -> d_s should DIVERGE (no stable plateau; plateau grows with N) and be
  ~indistinguishable from the degree-matched null. If ball-growth said D~1.5-2.8,
  that is the fooled estimator. Falsifier: a stable finite d_s plateau, flat
  across N, distinct from null.
"""
import numpy as np, networkx as nx, math
rng = np.random.default_rng(7)

# ---------- the honest ruler: spectral dimension via heat kernel ----------
def spectral_dim(G, tmin=1.0, tmax=None, npts=40):
    """d_s from heat-kernel return prob P(t)=(1/N)Σ_k e^{-λ_k t}, λ_k = normalized
    Laplacian eigenvalues. d_s(t) = -2 dlnP/dlnt. Return median d_s over the
    intermediate window + the full d_s(t) curve so divergence (climbing) is visible."""
    G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    n = G.number_of_nodes()
    if n < 20: return np.nan, n, None
    L = nx.normalized_laplacian_matrix(G).toarray()
    lam = np.linalg.eigvalsh(L)
    lam = np.clip(lam, 0, 2)
    if tmax is None: tmax = 2.0/max(lam[1], 1e-6)   # ~mixing time from spectral gap
    ts = np.geomspace(tmin, tmax, npts)
    P = np.array([np.mean(np.exp(-lam*t)) for t in ts])
    lnP, lnt = np.log(P), np.log(ts)
    ds_t = -2*np.gradient(lnP, lnt)
    # intermediate window: drop first/last 20% (local & global regimes)
    a, b = int(0.25*npts), int(0.80*npts)
    ds_mid = np.median(ds_t[a:b])
    return ds_mid, n, (ts, ds_t)

def degree_matched_null(G):
    """degree-preserving null: configuration model on G's degree sequence,
    simplified to a simple graph (robust on dense graphs; no swap-budget failure)."""
    deg = [d for _,d in G.degree()]
    H = nx.configuration_model(deg, seed=7)
    H = nx.Graph(H)              # collapse parallel edges
    H.remove_edges_from(nx.selfloop_edges(H))
    return H

# ---------- VALIDATE the ruler on known answers ----------
def torus(dim, L):
    G = nx.grid_graph([L]*dim, periodic=True); return nx.convert_node_labels_to_integers(G)
print("=== RULER VALIDATION (known answers) ===")
for name, G in [("1D ring N=800", nx.cycle_graph(800)),
                ("2D torus 28x28", torus(2,28)),
                ("3D torus 9x9x9", torus(3,9)),
                ("ER random N=800 <k>=6", nx.gnm_random_graph(800, 800*3, seed=7))]:
    ds,_,_ = spectral_dim(G)
    print(f"  {name:24s} d_s = {ds:5.2f}")
print("  (expect ~1, ~2, ~3, and ER climbing/high = no finite geometry)\n")

# ---------- the relational-closure model (reconstructed, flags marked) ----------
def relational_graph(n, p0=.03, alpha=.15, beta=.8, decay=.08, steps=60, density=.04, seed=0):
    r = np.random.default_rng(seed)
    s = r.choice([-1,1], n)
    W = np.zeros((n,n))
    mask = r.random((n,n)) < p0
    mask = np.triu(mask,1); mask = mask + mask.T
    W[mask] = r.normal(0,.15, int(mask.sum()))
    np.fill_diagonal(W,0)
    for _ in range(steps):
        S = np.outer(s,s)
        closure = W @ W
        deg = np.maximum((W>0).sum(1), 1)
        norm = np.sqrt(np.outer(deg,deg))
        W = (1-decay)*W + alpha*S + beta*closure/norm
        np.fill_diagonal(W,0)              # >>> RECON: no self-loops each step
        # >>> RECON-STABILIZER: pasted model overflows (W@W compounds). Least-opinionated
        # fix: hold W's magnitude at the init scale each step, preserving the *pattern*
        # (which edges are strong) and changing only scale. The real stabilizer is likely
        # in the truncated tail; this is a stand-in, flagged as such.
        sd = W.std()
        if sd > 0: W = W/sd*0.15
    # >>> RECON: truncated tail. Threshold |W| to target edge density, undirected.
    W = (W + W.T)/2                        # >>> RECON: symmetrize (already ~symmetric)
    iu = np.triu_indices(n,1)
    vals = np.abs(W[iu])
    k = int(density*n*(n-1)/2)
    if k < 1: k = 1
    thr = np.partition(vals, -k)[-k]      # >>> RECON: keep top-k |W| edges = density
    G = nx.Graph()
    G.add_nodes_from(range(n))
    sel = vals >= thr
    for a,b in zip(iu[0][sel], iu[1][sel]): G.add_edge(int(a),int(b))
    return G, W

def graph_pernode_topk(W, k=6):
    """ALT reconstruction of the truncated tail = Ciara's stated rule: 'each node
    retains its strongest k relationships'. Per-node top-k -> sparse, bounded degree.
    She flagged this rule as imposed locality; this is the variant that tests it."""
    n = W.shape[0]; A = np.abs(W).copy(); np.fill_diagonal(A, -1)
    G = nx.Graph(); G.add_nodes_from(range(n))
    idx = np.argsort(-A, axis=1)[:, :k]
    for i in range(n):
        for j in idx[i]:
            if A[i,j] > 0: G.add_edge(i, int(j))   # union (mutual not required)
    return G

# ---------- N-COMPANION: bracket model between geometry anchor & its own null ----------
def climb(curve):
    """is d_s(t) rising through the intermediate window? (expander tell)"""
    ts, ds = curve; a,b = int(0.25*len(ts)), int(0.80*len(ts))
    return ds[b-1]-ds[a]   # >0 climbing, ~0 plateau
print("=== PRIMITIVE TEST: relational-closure model on the honest ruler ===")
print("  (with RECON-STABILIZER; measured identically to a 2D-torus anchor & the model's own degree-matched null)")
print("  A = global density-threshold tail (mine).  B = per-node top-k tail (Ciara's stated rule).")
print(f"{'N':>6} {'2Dtor':>6} | {'A d_s':>6} {'clmb':>5} {'nullA':>6} {'<k>A':>6} | {'B d_s':>6} {'clmb':>5} {'nullB':>6} {'<k>B':>6}")
dsA, dsB = [], []
for N in [400, 800, 1600]:
    GA, W = relational_graph(N, seed=7)
    gA = GA.subgraph(max(nx.connected_components(GA), key=len)).copy()
    ds_a, na, ca = spectral_dim(GA); dsA.append(ds_a)
    nA,_,_ = spectral_dim(degree_matched_null(gA))
    kA = 2*gA.number_of_edges()/max(gA.number_of_nodes(),1)
    GB = graph_pernode_topk(W, k=6)
    gB = GB.subgraph(max(nx.connected_components(GB), key=len)).copy()
    ds_b, nb, cb = spectral_dim(GB); dsB.append(ds_b)
    nB,_,_ = spectral_dim(degree_matched_null(gB))
    kB = 2*gB.number_of_edges()/max(gB.number_of_nodes(),1)
    Ltor = int(round(math.sqrt(N))); ds_t,_,_ = spectral_dim(torus(2, Ltor))
    clA = climb(ca) if ca else float('nan'); clB = climb(cb) if cb else float('nan')
    ncompB = nx.number_connected_components(GB); gcB = 100*nb/N
    print(f"{N:>6} {ds_t:>6.2f} | {ds_a:>6.2f} {clA:>+5.1f} {nA:>6.2f} {kA:>6.0f} | {ds_b:>6.2f} {clB:>+5.1f} {nB:>6.2f} {kB:>6.1f}  [B giantCC {gcB:>3.0f}% in {ncompB} comps]")

def read(tag, ds):
    if any(np.isnan(ds)): return f"  {tag}: no giant component -> collapsed"
    d = ds[-1]-ds[0]
    verd = "CLIMBS w/N = NO finite geometry" if d>0.5 else "FLAT w/N = candidate finite geometry"
    return f"  {tag} d_s across N = {[round(v,2) for v in ds]} (drift {d:+.2f}) -> {verd}"
print("\nVERDICT (N-companion is the decider; compare each to its own degree-null):")
print(read("A global-threshold", dsA))
print(read("B per-node-topk   ", dsB))
