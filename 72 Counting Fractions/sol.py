# with open('tmp.txt','w'): pass
# file = open('tmp.txt','w')
'''

phi[n] means number of i <= n, such that gcd(i,n) = 1

Properties of phi:

phi[p] = p-1,   p is prime

phi[p**k] = p**k - p**(k-1),   k e I

phi[a*b] = phi[a]*phi[b]*gcd(a,b)//phi[gcd(a,b)],   a,b e I

'''
import math
N = 10**6+1
fact = [[] for i in range(N)]
phi = [0 for i in range(N)]
phi[1] = 1
phi[2] = 1
for i in range(4,N,2):
    fact[i].append(2)
for i in range(3, N, 2):
    if len(fact[i])==0:
        phi[i] = i-1
        for j in range(2*i, N, i):
            fact[j].append(i)
        t = i*i
        while t < N:
            phi[t] = t - t//i
            t = t*i
def getPhi(n):
    if phi[n]!=0:
        return phi[n]
    for f in fact[n]:
        d = math.gcd(f, n//f)
        phi[n] = getPhi(f)*getPhi(n//f)*d//getPhi(d)
    return phi[n]
dp = [0]*N
for i in range(2,N):
    dp[i] += dp[i-1] + getPhi(i)
print("Pre-computation done")
t = int(input())
for xyz in range(t):
    q = int(input())
    print(dp[q])
# file.write(str(dp))
