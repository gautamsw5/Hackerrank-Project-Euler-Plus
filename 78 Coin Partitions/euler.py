N=10
coins=[i for i in range(1,N+1)]
dp=[0 for c in range(0,N+1)]
dp[0]=1
table=[[0 for i in range(N+1)] for j in range(N+1)]
for coin in coins:
    for k in range(coin,N+1):
        dp[k]=dp[k]+dp[k-coin]
        table[k][coin]=dp[k]
'''for i in range(1,N+1):
    print(table[i])'''
'''
n=1
while n<=N:
    if dp[n]%1000000==0:
        print(n,dp[n])
        break
    n=n+1
'''
