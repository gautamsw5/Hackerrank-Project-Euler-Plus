# import math
# N = 10**6 + 1
# N = 101
# dp = [0]*N
# for i in range(5, N):
#     maxi = 0
#     maxx = 0
#     for x in range(1, i+1):
#         if pow(i/x, x) > maxi:
#             maxi = pow(i/x, x)
#             maxx = x
#     # print(i,"->",maxi," => ","("+str(i)+"/"+str(maxx)+")^"+str(maxx)," ",maxx,int(i//math.e))
#     dp[i] = maxx

import math
N = 10**6 + 1
def check(n):
    while n%10==0 and n>0:
        n = n//10
    while n%2==0 and n>0:
        n = n//2
    while n%5==0 and n>0:
        n = n//5
    return n==1
D = [0]*(N)
for n in range(5, N):
    D[n] = D[n-1]
    x = int(n//math.e)
    if x*math.log(n/x) < (x+1)*math.log(n/(x+1)):
        x = x+1
    if check(x//math.gcd(n, x)):
        D[n] -= n
    else:
        D[n] += n
    # print(n,x,dp[n])
q = int(input())
for i in range(q):
    print(D[int(input())])