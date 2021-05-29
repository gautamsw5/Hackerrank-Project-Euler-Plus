def getsummation(N):
    coins=[i for i in range(1,N)]
    dp={c:1 for c in range(N+1)}
    for coin in coins[1:]:
        for k in range(coin,N+1):
            dp[k]+=dp[k-coin]
    return dp[N]
t=int(input())
for xyz in range(t):
    n=int(input())
    print(getsummation(n)%1000000007)
