import math
N = 5*10**6+1
count = [0]*N
dp = [0]*N
for m in range(1, 1583):
    n = 1+m%2
    while n<m and 2*m*m + 2*m*n < N:
        if math.gcd(n,m)==1:
            k = 1
            while 2*k*m*m + 2*k*m*n < N:
                count[2*k*m**2 + 2*k*m*n] += 1
                k += 1
        n += 2
for i in range(1, N):
    dp[i] = dp[i-1]
    if count[i]==1:
        dp[i]+=1
t = int(input())
for xyz in range(t):
    print(dp[int(input())])