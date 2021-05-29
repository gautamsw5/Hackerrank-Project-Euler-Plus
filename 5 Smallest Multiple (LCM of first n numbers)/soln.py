import sys

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
lcm={}
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=1
    if n in lcm:
        print(lcm[n])
    else:
        for i in range(1,n+1):
            lcm[i]=(x*i)//(gcd(x,i))
            x=(x*i)//(gcd(x,i))
        print(lcm[n])
