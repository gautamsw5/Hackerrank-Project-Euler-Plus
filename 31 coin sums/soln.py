# Enter your code here. Read input from STDIN. Print output to STDOUT
# Got this from YouTube
coins=[1,2,5,10,20,50,100,200]
N=10**5
dp={c:0 for c in range(N+1)}
dp[0]=1
for coin in coins:
    for k in range(coin,N+1):
        dp[k]+=dp[k-coin]
t=int(input())
for xyz in range(t):
    n=int(input())
    # print((dp[n])%1000000007)
    print(dp[n])
