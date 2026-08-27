"""compressibility(f) as order parameter + order of the f_crit transition.
Pre-registered: findings/2026-08-11-compressibility-order-parameter-PREREG.md
Primary = RCM-reordered adjacency, zlib bits (permutation charged). Cross-check =
von Neumann spectral entropy. Order verdict = replica DISTRIBUTION (bimodal=1st order).
"""
import numpy as np, networkx as nx, zlib, math
from numpy.linalg import eigvalsh
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.sparse import csr_matrix

def rgg_frac(N, f, kbar=6, seed=0):
    """2D random-geometric graph, each edge rewired to random endpoints w.p. (1-f)."""
    r = np.random.default_rng(seed)
    # radius for mean degree ~kbar in unit square: kbar = N*pi*rad^2 -> rad
    rad = math.sqrt(kbar/(N*math.pi))
    pos = r.random((N,2))
    G = nx.random_geometric_graph(N, rad, pos={i:pos[i] for i in range(N)})
    edges = list(G.edges())
    for (u,v) in edges:
        if r.random() > f:  # rewire with prob (1-f)
            G.remove_edge(u,v)
            while True:
                a,b = int(r.integers(N)), int(r.integers(N))
                if a!=b and not G.has_edge(a,b): G.add_edge(a,b); break
    return G

def compression_bits(G):
    """RCM-reorder -> upper-tri adjacency bitstream -> zlib. Charge permutation."""
    N = G.number_of_nodes()
    A = nx.to_scipy_sparse_array(G, format='csr', dtype=np.int8)
    perm = reverse_cuthill_mckee(csr_matrix(A))
    Ad = nx.to_numpy_array(G)[np.ix_(perm,perm)].astype(np.uint8)
    iu = np.triu_indices(N,1)
    bits = np.packbits(Ad[iu])
    comp = len(zlib.compress(bits.tobytes(), level=9))*8   # compressed adjacency bits
    perm_bits = math.lgamma(N+1)/math.log(2)               # log2(N!) permutation cost
    E = G.number_of_edges()
    return comp, comp+perm_bits, comp/max(E,1)             # (adj-only, +perm, bits/edge)

def vn_entropy(G):
    """von Neumann entropy of rho=L/tr(L), normalized by log N."""
    N = G.number_of_nodes()
    L = nx.laplacian_matrix(G).toarray().astype(float)
    tr = np.trace(L)
    if tr<=0: return np.nan
    mu = np.clip(np.sort(eigvalsh(L))/tr, 1e-12, 1)
    S = -np.sum(mu*np.log(mu))
    return S/math.log(N)

# ---------- VALIDATION (must order lattices vs random or run is void) ----------
def torus(dim,L): return nx.grid_graph([L]*dim, periodic=True)
print("=== VALIDATION (compression must order lattice << random) ===")
print(f"{'graph':22s} {'adjbits/edge':>12} {'vN entropy':>11}")
for name,G in [("2D torus 20x20", torus(2,20)),
               ("3D torus 8x8x6", torus(3,8) if False else nx.grid_graph([8,8,6],periodic=True)),
               ("ER random N400 k6", nx.gnm_random_graph(400,1200,seed=1)),
               ("RGG N400 (geom)", rgg_frac(400,1.0,seed=1))]:
    G = nx.convert_node_labels_to_integers(G)
    _,_,bpe = compression_bits(G); S = vn_entropy(G)
    print(f"{name:22s} {bpe:>12.2f} {S:>11.3f}")
print("  expect: torus low bits/edge (compressible), ER high (incompressible)\n")

# ---------- f-SWEEP with REPLICAS (distribution = order verdict) ----------
def bimodality_coeff(x):
    x=np.asarray(x); n=len(x)
    if n<4 or np.std(x)==0: return np.nan
    m=np.mean(x); s=np.std(x)
    g=np.mean(((x-m)/s)**3); k=np.mean(((x-m)/s)**4)-3
    return (g**2+1)/(k + 3*(n-1)**2/((n-2)*(n-3)))   # BC>0.555 hints bimodal

FS = [0.50,0.60,0.65,0.68,0.70,0.72,0.74,0.76,0.80,0.90]
REPS = 30
print("=== f-SWEEP: bits/edge distribution across replicas (BC>0.555 hints bimodal=1st-order) ===")
for N in [400, 800]:
    print(f"\n--- N={N} ---")
    print(f"{'f':>5} {'mean bpe':>9} {'std':>6} {'BC':>6} {'vN mean':>8} {'range[min,max]':>16}")
    prev=None
    for f in FS:
        bpes=[]; Ss=[]
        for s in range(REPS):
            G=rgg_frac(N,f,seed=1000*int(f*100)+s)
            _,_,bpe=compression_bits(G); bpes.append(bpe); Ss.append(vn_entropy(G))
        bpes=np.array(bpes); bc=bimodality_coeff(bpes)
        jump = f"  <-- Δmean {bpes.mean()-prev:+.2f}" if prev is not None else ""
        print(f"{f:>5.2f} {bpes.mean():>9.2f} {bpes.std():>6.2f} {bc:>6.3f} {np.mean(Ss):>8.3f} [{bpes.min():>6.1f},{bpes.max():>6.1f}]{jump}")
        prev=bpes.mean()
print("\nVERDICT KEYS: bimodal (BC>0.555) near f_crit=0.72 sharpening with N -> FIRST-ORDER (rent gap).")
print("             unimodal, derivative-peak growing with N -> SECOND-ORDER -> demote crystallization to metaphor.")
