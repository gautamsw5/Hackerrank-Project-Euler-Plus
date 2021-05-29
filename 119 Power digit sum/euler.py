import math
def sod(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
ans=[]
for s in range(2,900):
    p=2
    while s**p<10**100:
        n=s**p
        if s==sod(n):
            ans.append(n)
        p=p+1
ans.sort()
print(ans)
