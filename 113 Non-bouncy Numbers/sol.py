arr = [0]
N = 10**5+1
mod = 10**9 + 7
def bouncy(n):
    ret = 0
    for i in range(1,n):
        x = list(str(i))
        if x == sorted(x) or x[::-1] == sorted(x):
            ret += 1
    return ret
def C(n, r):
    if r<0 or r>n:
        return 0
    if r==0 or r==n:
        return 1
    ans = n
    for i in range(1, r):
        ans *= (n-i)
    for i in range(1, r+1):
        ans = ans//i
    return ans
for k in range(1, N):
    s = arr[-1]+9
    for r in range(1, min(9, k)):
        s = (s + C(9, r+1)*C(k-1, r))%mod
    for r in range(1, min(10, k)):
        s = (s + C(10, r+1)*C(k-1, r))%mod
        #print(k,"digits,",r,"pivots",2*C(9, r+1)*C(k-1, r))
    arr.append(s)
#print(arr[:20])
t = int(input())
for xyz in range(t):
    print(arr[int(input())])
