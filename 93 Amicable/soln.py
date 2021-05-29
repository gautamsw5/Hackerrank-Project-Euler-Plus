def sumoff(n):
    if n==1 or n==0:
        return 0
    i=2
    s=1
    while i*i<n:
        if n%i==0:
            s=s+i+n//i
        i=i+1
    if i*i==n:
        s=s+i
    return s
m=0
el=0
ans=0
'''s=set()
c=0
m=203034
x=sumoff(203034)
s.add(203034)
while True:
    print(x)
    if x<m:
        m=x
    if x in s:
        break
    s.add(x)
    c=c+1
    x=sumoff(x)
    if x>10**6:
        c=0
        break
print(m)'''
for i in range(10**5,10**6+1):
    x=sumoff(i)
    s=set()
    s.add(i)
    s.add(x)
    c=1
    while x>1 and x!=i:
        x=sumoff(x)
        s.add(x)
        if x>10**6:
            c=0
            break
        c=c+1
        if sumoff(x) in s:
            break
        #print(i,x)
    if c>m and x==i:
        m=c
        el=i
        ans=min(s)
print(ans)
