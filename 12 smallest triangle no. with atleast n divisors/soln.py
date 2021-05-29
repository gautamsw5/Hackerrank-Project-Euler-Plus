import sys
def factorcnt(n):
    i=2
    c=2
    while i*i<n:
        if n%i==0:
            c=c+2
        i=i+1
    if i*i==n:
        c=c+1
    return c
def factorset(n):
    i=1
    c=0
    s=set()
    while i*i<n:
        if n%i==0:
            c=c+2
            s.add(n//i)
            s.add(i)
        i=i+1
    if i*i==n:
        c=c+1
        s.add(i)
    return s
dct={}
dct[1]=1
dct[2]=3
i=3
a=0
b=0
while a*b<1000:
    x=(i*(i+1))//2
    if i%2==0:
        a=factorcnt(i//2)
        b=factorcnt(i+1)
    else:
        a=factorcnt((i+1)//2)
        b=factorcnt(i)
    '''if(a*b!=factorcnt(x)):
        print(i,x,a,b)'''
    if not a*b in dct:
        dct[a*b]=x
    i=i+1
t=int(input())
for t0 in range(0,t):
    n=int(input())
    m=10**20
    for i in dct:
        if i>n and dct[i]<m:
            m=dct[i]
    print(m)
