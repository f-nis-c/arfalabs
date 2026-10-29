def sm(r,n,k):
    m=[None]*n;q=[];f=0;g=[]
    for i,x in enumerate(r):
        if x in m:
            s="h"
            if k==1:q.remove(x);q.append(x)
        else:
            f+=1;s="f"
            if None in m:j=m.index(None)
            else:
                t=r[i+1:]
                v=max(q,key=lambda y:t.index(y) if y in t else len(t)+1) if k==2 else q[0]
                q.remove(v);j=m.index(v)
            m[j]=x;q.append(x)
        g.append((m[:],s))
    return g,f
def pr(h,r,n,k):
    g,f=sm(r,n,k)
    print(f"\n{h}")
    print("Pg   |"+"".join(f"{x:>3}" for x in r))
    print("-----+"+"---"*len(r))
    for j in range(n-1,-1,-1):
        print(f"Fr {j+1}|"+"".join(f"{c[0][j] if c[0][j] is not None else '.':>3}" for c in g))
    print("-----+"+"---"*len(r))
    print("     |"+"".join(f"{c[1]:>3}" for c in g))
    print(f"f={f} h={len(r)-f}")
    return f
r=list(map(int,input("Pages: ").split()))
n=int(input("Frames: "))
a=[(h,pr(h,r,n,k)) for h,k in(("FIFO",0),("LRU",1),("OPT",2))]
print("\nAlgo  f  h")
for h,f in a:print(f"{h:<5}{f:>3}{len(r)-f:>3}")
