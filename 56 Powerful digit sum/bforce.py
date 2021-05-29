def ds(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
m=0
arr=[]
for n in range(1,201):
    for a in range(1,n):
        for b in range(1,n):
            x=ds(a**b)
            if x>m:
                m=x
    arr.append(m)
    print(m)
