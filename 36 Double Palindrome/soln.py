def toB(n,b):
    x=0
    p=1
    while n>0:
        x=x+(n%b)*p
        p=p*10
        n=n//b
    return x
s=0
n,b=map(int,input().split())
for k in range(0,10):
    y=toB(k,b)
    if str(y)==str(y)[::-1] and k<n:
        print(k,y)
        s=s+k
for i in range(1,10000):
    x=int(str(i)+str(i)[::-1])
    y=toB(x,b)
    if str(y)==str(y)[::-1] and x<n:
        print(x,y)
        s=s+x
    for k in range(0,10):
        x=int(str(i)+str(k)+str(i)[::-1])
        y=toB(x,b)
        if str(y)==str(y)[::-1] and x<n:
            print(x,y)
            s=s+x
print(s)
