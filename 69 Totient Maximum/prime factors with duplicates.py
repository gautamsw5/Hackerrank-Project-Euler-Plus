import math
N=10**6+1
prime=[[] for i in range(N)]
p=set()
P=[]
for i in range(2,N):
    if len(prime[i])==0:
        pr=i*i
        x=1
        while pr<N:
            for prr in range(pr,N,pr):
                prime[prr]+=[i]*x
            pr=pr*i
            x=x+1
for i in range(2,N):
    if len(prime[i])==0:
        p.add(i)
        P.append(i)
        for pr in range(2*i,N,i):
            prime[pr].append(i)
def isprime(n):
    if n in p:
        return True
    if n<N:
        return False
    x=math.sqrt(n)+1
    i=0
    while P[i]<=x:
        if n%P[i]==0:
            return False
        i=i+1
    p.add(n)
    return True
