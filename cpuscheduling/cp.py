def sm(p,k):
    q={x[0]:x[2] for x in p};t=0;d={};g=[]
    while len(d)<len(p):
        a=[x for x in p if x[0] not in d and x[1]<=t]
        if not a:
            t=min(x[1] for x in p if x[0] not in d);continue
        x=min(a,key=lambda y:(y[1] if k==1 else q[y[0]] if k in(2,3) else y[3],y[1]))
        u=1 if k in(3,5) else q[x[0]]
        g.append((x[0],t,t+u));t+=u;q[x[0]]-=u
        if q[x[0]]==0:d[x[0]]=t
    return d,g
def rr(p,u):
    p=sorted(p,key=lambda x:x[1]);q={x[0]:x[2] for x in p};t=0;i=0;w=[];d={};g=[]
    while len(d)<len(p):
        while i<len(p) and p[i][1]<=t:w.append(p[i][0]);i+=1
        if not w:
            t=p[i][1];continue
        c=w.pop(0);e=min(u,q[c]);g.append((c,t,t+e));t+=e;q[c]-=e
        while i<len(p) and p[i][1]<=t:w.append(p[i][0]);i+=1
        if q[c]:w.append(c)
        else:d[c]=t
    return d,g
def ot(h,p,d,g,v):
    m=[]
    for c,a,b in g:
        if m and m[-1][0]==c and m[-1][2]==a:m[-1][2]=b
        else:m.append([c,a,b])
    tt=tw=0
    if v:
        print(f"\n{h}\n"+" ".join(f"|{c} {a}-{b}" for c,a,b in m)+"|")
        print("ID\tAT\tBT\tPR\tCT\tTAT\tWT")
    for i,a,b,r in p:
        z=d[i]-a;tt+=z;tw+=z-b
        if v:print(f"{i}\t{a}\t{b}\t{r}\t{d[i]}\t{z}\t{z-b}")
    n=len(p)
    if v:print(f"Avg TAT={tt/n:.2f} WT={tw/n:.2f}")
    return tt/n,tw/n
n=int(input("Procs: "))
p=[]
print("Enter id at bt pri (low pri = first):")
for _ in range(n):
    i,a,b,c=input().split();p.append([i,int(a),int(b),int(c)])
L=[("FCFS",1),("SJF",2),("SRTF",3),("Pri",4),("PriP",5),("RR",6),("All",7)]
for k,h in enumerate(L,1):print(f"{k} {h[0]}")
o=int(input("Pick: "))
u=int(input("Quantum: ")) if o in(6,7) else 0
def go(h,k,v):
    d,g=rr(p,u) if k==6 else sm(p,k)
    return ot(h,p,d,g,v)
if o<7:go(L[o-1][0],o,1)
else:
    print("\nAlgo\tTAT\tWT")
    for h,k in L[:6]:
        x,y=go(h,k,0);print(f"{h}\t{x:.2f}\t{y:.2f}")
