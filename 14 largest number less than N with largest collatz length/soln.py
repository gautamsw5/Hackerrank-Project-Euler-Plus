import time
import math
m=0
ans=0
dct=[0]*5000001
dct2=[0]*5000001
dct[1]=0
dct2[1]=0
tx=time.time()
for i in range(2,5000001):
    c=0
    if dct[i]==0:
        c=0
        x=i
        while x>1:
            if x<5000001 and dct[x]!=0:
                c=c+dct[x]
                break
            elif x%2==0:
                x=x>>1
            else:
                x=3*x+1
            c=c+1
        dct[i]=c
        if i<2500001:
            dct[2*i]=c+1
        if i%2==1 and i<1666667:
            dct[3*i+1]=c-1
    else:
        c=dct[i]
    if c>=m:
        m=c
        ans=i
    dct2[i]=max(dct2[i-1],ans)
print(time.time()-tx)
t=int(input())
for i in range(t):
    n=int(input())
    print(dct2[n-1])
'''def coletz(i,dct):
    c=0
    while i>1:
        if i in dct:
            c=c+dct[i]
            break
        elif i%2==0:
            i=i//2
        else:
            i=3*i+1
        c=c+1
    return c
#n=int(input())
m=0
ans=0
dct={1:0}
dct2={1:0}
dct3={1:0}
tx=time.time()
for i in range(2,14**6+1):
    c=0
    if not i in dct:
        c=coletz(i,dct)
        dct[i]=c
        dct[2*i]=c+1
        if i%2==1:
            dct[3*i+1]=c-1
    else:
        c=dct[i]
    if c>=m:
        m=c
        ans=i
        dct3[c]=ans
    dct2[i]=max(dct2[i-1],ans)
print(time.time()-tx)
t=int(input())
for i in range(t):
    n=int(input())
    print("Number that has longest chain ",dct2[n-1])
    print("Chain length ",coletz(dct2[n-1],dct))
for i in range(1000000,5000001):
    if dct2[i-1]!=dct2[i]:
        print(i,dct2[i])'''
'''def coletz(i,dct):
    c=0
    while i>1:
        if i in dct:
            c=c+dct[i]
            break
        elif i%2==0:
            i=i//2
        else:
            i=3*i+1
        c=c+1
    return c
def printcoletz(i):
    c=0
    s=str(i)+"->"
    while i>1:
        if i%2==0:
            i=i//2
            s=s+str(i)+"->"
        else:
            i=3*i+1
            s=s+str(i)+"->"
        c=c+1
    return s
n=int(input())
m=0
ans=0
dct={1:0}
arr=[(1,0)]
for i in range(2,n+1):
    c=0
    if not i in dct:
        c=coletz(i,dct)
        dct[i]=c
        dct[2*i]=c+1
        if i%2==1:
            dct[3*i+1]=c-1
    else:
        c=dct[i]
    if c>=m:
        m=c
        ans=i
    arr.append((ans,m))
print(arr[n-1][0])
t=int(input())
dct={}
dct2={}
for t0 in range(t):
    n=int(input())
    m=0
    for i in range(1,n+1):
        c=0
        if not i in dct:
            c=coletz(i)
            dct[i]=c
            if c in dct2:
                dct2[c]=max(dct2[c],i)
            else:
                dct2[c]=i
        else:
            c=dct[i]
        m=max(m,c)
    print(dct2[m])'''
