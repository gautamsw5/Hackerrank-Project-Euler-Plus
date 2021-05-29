N=1001
dp={c:1 for c in range(N+1)}
dp[1]=0
prime=[True]*N
primes=[]
primeset=set()
for i in range(2,N):
    if prime[i]:
        primes.append(i)
        primeset.add(i)
        for k in range(2*i,N,i):
            prime[k]=False
dp={c:0 for c in range(1,N+1)}
dp[0]=1
for coin in primes:
    for k in range(coin,N+1):
        dp[k]+=dp[k-coin]
        #print(str(k),str(k-coin))
t=int(input())
for xyz in range(t):
    n=int(input())
    # print((dp[n])%1000000007)
    print(dp[n])
