N=101
prime=[True for i in range(N)]
P=[]
for i in range(2,N):
    if prime[i]:
        P.append(i)
        for x in range(2*i,N,i):
            prime[x]=False
t=int(input())
for xyz in range(t):
    n=int(input())
    ans=1
    i=0
    while ans*P[i]<n:
        ans*=P[i]
        i=i+1
    print(ans)
