def ds(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
m=0
for a in range(1,100):
    for b in range(1,100):
        x=ds(a**b)
        if x>m:
            m=x
    print(m)
