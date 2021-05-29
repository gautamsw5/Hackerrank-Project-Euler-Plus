# ans[(N,K,L)] ==> N digit number, L prime family, replacing K digits with same digit (may or may not be adjacent)
# N -> 2 to 7
# K -> 1 to N
# L -> 1 to 8
# Warning: could take more than 30 min to execute
import time
import math
import itertools
def perm(n): # perms of n that are greater than n and are prime 
    ret=set()
    for i in itertools.permutations(str(n)):
        s=0
        for d in i:
            s=s*10+ord(d)-ord('0')
        if s>n and s in p:
            ret.add(s)
    return ret
def ntoArr(n):
    arr=[]
    while n>0:
        arr=[n%10]+arr
        n=n//10
    return arr
def arrtoN(arr):
    s=0
    for i in arr:
        s=s*10+i
    return s
def compare(a,b):
    if len(a)==0:
        return b
    if len(b)==0:
        return a
    i=0
    while i<len(a) and i<len(b):
        if a[i]>b[i]:
            return b
        if a[i]<b[i]:
            return a
        i=i+1
    if len(a)>len(b):
        return a
    return b
tx=time.time()
#ans={}
ans = [ [ [ [ ] for b in range(10)] for c in range(10)] for d in range(10)]
def check(n):
    dct={}
    for i in str(n):
        if i in dct:
            dct[i]+=1
            if dct[i]==3:
                return True
        else:
            dct[i]=1
    return False
primes = [True]*10000005    # 10000005
primes[0]=False
primes[1]=False
p=set()
P=[]
for i in range(2,10000005):
    if primes[i]:
        p.add(i)
        P.append(i)
        for k in range(2*i,10000005,i):
            primes[k]=False
print(time.time()-tx)
abc=0
for num in P:
    if num>=10**abc:
        print(abc)
        if abc==7:
            break
        abc+=1
    X=list(ntoArr(num))
    if X[0]==1:
        N=len(X)
        for k in range(1,N+1):
            arr=[i for i in range(N)]
            for comb in list(itertools.combinations(arr,k)):
                #print(num,k,arr,comb)
                if 0 in comb:
                    #print(num,comb)
                    xrr=set()
                    for i in range(1,10):
                        x=list(X)
                        for c in comb:
                            x[c]=i
                        if arrtoN(x) in p:
                            xrr.add(arrtoN(x))
                    xrr=list(xrr)
                    xrr.sort()
                    L=len(xrr)
                    #print(num,N,k,L,ans[N][k][L])
                    ans[N][k][L]=compare(ans[N][k][L],xrr)
                    #print(ans[N][k][L])
                else:
                    #print(num,comb)
                    xrr=set()
                    for i in range(10):
                        x=list(X)
                        for c in comb:
                            x[c]=i
                        #print(x)
                        if arrtoN(x) in p:
                            xrr.add(arrtoN(x))
                            #print(num,arrtoN(x))
                    xrr=list(xrr)
                    xrr.sort()
                    L=len(xrr)
                    #print(num,N,k,L,ans[N][k][L])
                    ans[N][k][L]=compare(ans[N][k][L],xrr)
                    #print(ans[N][k][L])
