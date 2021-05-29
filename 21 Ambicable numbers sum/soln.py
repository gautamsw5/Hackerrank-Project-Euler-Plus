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
amicable=set()
for i in range(1,10**5):
    x=sumoff(i)
    y=sumoff(x)
    if i==y and i!=x:
        amicable.add(i)
        amicable.add(x)
