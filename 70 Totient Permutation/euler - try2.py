import math
def isperm(a,b):
    x=[0]*10
    y=[0]*10
    while a>0:
        x[a%10]+=1
        a=a//10
    while b>0:
        y[b%10]+=1
        b=b//10
    return x==y
N=10**6
prime=[True for i in range(N)]
print("Init done")
p=set()
P=[]
for i in range(2,N):
    if prime[i]==True:
        p.add(i)
        P.append(i)
        for x in range(2*i,N,i):
            prime[x]=False
print("Primes done")
def pfactors(n):
    ret=[]
    if n in p:
        return ret
    for i in P:
        if n%i==0:
            ret.append(i)
            while n%i==0:
                n=n//i
        if i>n:
            #print("breaking",i,n)
            break
    return ret
def calcPhi(n):
    arr=[1]*n
    arr[0]=0
    for i in pfactors(n):
        if arr[i]==1:
            for x in range(i,n,i):
                arr[x]=0
    '''print(n,"Relatively Prime->")
    for i in range(len(arr)):
        if arr[i]==1:
            print(i,end=' ')
    print("")'''
    return sum(arr)
# Phi=i-1-NumofNumsWithGcdMoreThanOne(i)
mmin=100
for i in range(2,N):
    #print(i,pfactors(i))
    Phi=calcPhi(i)
    if isperm(Phi,i) and i/Phi<mmin:
        mmin=i/Phi
        print(i,Phi,i/Phi)
def isprime(n):
    if n in p:
        return True
    if n<N:
        return False
    x=math.sqrt(n)+1
    i=0
    while P[i]<=x:
        if n%P[i]==0:
            return False
        i=i+1
    p.add(n)
    return True
