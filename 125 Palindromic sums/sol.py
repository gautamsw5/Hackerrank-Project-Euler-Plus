t = int(input())
def pali(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
dp = {}
for xyz in range(t):
    N,d = map(int, input().split())
    if (N,d) in dp:
        print(dp[(N,d)])
        continue
    s = set()
    a = 1
    while a*a < N:
        n = 2
        x = n*a*a + n*a*(n-1)*d + d*d*n*(n-1)*(2*n-1)//6
        while x < N:
            if pali(str(x)):
                s.add(x)
            n += 1
            x = n*a*a + n*a*(n-1)*d + d*d*n*(n-1)*(2*n-1)//6
        a += 1
    ans = sum(s)
    print(ans)
    dp[(N,d)] = ans