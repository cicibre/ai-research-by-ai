import numpy as np, networkx as nx
from fiber_bundle import grow, fiber_bundle
print("=== FIBER-BUNDLE, 6 replicas: is 'entangled sheet burns catastrophically, tree sheds' robust? ===",flush=True)
print(f"{'fabric':18s} {'mean max/N':>11} {'mean deadfrac':>13} {'mean #aval':>11} {'catastrophe?':>13}",flush=True)
for pc,name in [(1.0,"sheet p_close=1"),(0.7,"p_close=.7"),(0.5,"mixed p_close=.5"),(0.0,"line p_close=0")]:
    mxn=[];dead=[];nav=[]
    for s in range(6):
        G=grow(1.0,pc,seed=s); av,N,d=fiber_bundle(G,seed=s+50)
        mxn.append((av.max() if len(av) else 0)/N); dead.append(d); nav.append(len(av))
    cat = "YES (giant)" if np.mean(mxn)>0.3 else ("graceful" if np.mean(mxn)<0.1 else "partial")
    print(f"  {name:16s} {np.mean(mxn):>11.3f} {np.mean(dead):>13.2f} {np.mean(nav):>11.0f} {cat:>13}",flush=True)
print("\nhigh max/N (giant avalanche) on the SHEET (entangled/closed) + low on the LINE (tree) =",flush=True)
print("closure/entanglement is what enables catastrophic burn; the tree sheds gracefully.",flush=True)
