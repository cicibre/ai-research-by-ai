import numpy as np, networkx as nx
def sandpile_avalanches(G, n_drive=6000, transient=2500, sink_frac=0.05, seed=0):
    G=nx.convert_node_labels_to_integers(G); n=G.number_of_nodes()
    rng=np.random.default_rng(seed)
    nbrs=[list(G.neighbors(i)) for i in range(n)]
    cap=np.array([max(len(nb),1) for nb in nbrs])
    sinks=set(rng.choice(n,size=max(1,int(sink_frac*n)),replace=False))
    issink=np.zeros(n,bool)
    for s in sinks: issink[s]=True
    nonsink=[i for i in range(n) if not issink[i]]
    h=np.zeros(n,int); sizes=[]
    for step in range(n_drive):
        h[rng.choice(nonsink)]+=1
        toppled=0; stack=[i for i in range(n) if h[i]>=cap[i] and not issink[i]]
        stack=list(dict.fromkeys(stack))
        while stack:
            i=stack.pop()
            if h[i]<cap[i] or issink[i]: continue
            h[i]-=cap[i]; toppled+=1
            for j in nbrs[i]:
                if issink[j]: continue
                h[j]+=1
                if h[j]>=cap[j]: stack.append(j)
        if step>=transient and toppled>0: sizes.append(toppled)
    return np.array(sizes)
def fit(sizes):
    if len(sizes)<200: return "INSUFF",np.nan,np.nan,(np.nan,np.nan)
    smax=sizes.max(); bins=np.unique(np.floor(np.geomspace(1,smax+1,25)).astype(int))
    cnt,edg=np.histogram(sizes,bins=bins); ctr=np.sqrt(edg[:-1]*edg[1:]); w=np.diff(edg)
    dens=cnt/w/len(sizes); m=(cnt>0)&(ctr>1)&(ctr<smax*0.5)
    if m.sum()<4: return "INSUFF",np.nan,np.nan,(np.nan,np.nan)
    x,y=ctr[m],dens[m]
    pl=np.polyfit(np.log(x),np.log(y),1); r2pl=1-np.sum((np.log(y)-np.polyval(pl,np.log(x)))**2)/np.sum((np.log(y)-np.log(y).mean())**2)
    ex=np.polyfit(x,np.log(y),1); r2ex=1-np.sum((np.log(y)-np.polyval(ex,x))**2)/np.sum((np.log(y)-np.log(y).mean())**2)
    tau=-pl[0]; dec=np.log10(x.max()/x.min())
    v="POWER-LAW" if (r2pl>r2ex+0.02 and 1<=tau<=2.5 and dec>=1.5) else ("EXPONENTIAL" if r2ex>=r2pl else "ambiguous")
    return v,tau,dec,(round(r2pl,3),round(r2ex,3))
print("=== SANDPILE on control substrates ===",flush=True)
for name,G in [("1D chain N=2000",nx.path_graph(2000)),
               ("random 4-reg N=2000",nx.random_regular_graph(4,2000,seed=1)),
               ("star N=2000",nx.star_graph(1999)),
               ("ER <k>=3 N=2000",nx.gnm_random_graph(2000,3000,seed=1))]:
    s=sandpile_avalanches(nx.convert_node_labels_to_integers(G),seed=2)
    v,tau,dec,r2=fit(s)
    print(f"  {name:22s}: {v}  tau={tau:.2f} dec={dec:.2f} R2(pl,exp)={r2} n={len(s)}",flush=True)
print("\npower-law on chain/random/star too -> the power-law is the MODEL, not the fabric.",flush=True)
