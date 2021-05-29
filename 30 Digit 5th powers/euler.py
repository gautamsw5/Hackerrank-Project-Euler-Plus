def sod5(n):
    s=0
    while n>0:
        s=s+(n%10)**5
        n=n//10
    return s
ans=0
for i in range(2,10**7):
    if i==sod5(i):
        ans+=i
print(ans)
