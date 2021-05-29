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
prime=[set() for i in range(N)]
print("Primeset built")
p=set()
P=[]
num=6
phi=2
for i in range(2,N):
    if len(prime[i])==0:
        for x in range(2*i,N,i):
            prime[x].add(i)
print("Primefactors done")
mmin=100
for i in range(2,N):
    for x in set(prime[i]):
        for k in range(2*x,i,x):
            prime[i].add(k)
    '''if i==10 or i==100 or i==1000 or i==10000 or i==100000 or i==1000000:
        print(i)'''
    prime[i]=len(prime[i])
    Phi=i-1-prime[i]
    '''if num*Phi<phi*i:
        num=i
        phi=Phi
        print(num)'''
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
