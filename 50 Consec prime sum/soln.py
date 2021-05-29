# Max chain length -> 379324 Min -> 2
# Discoverd from somewhwere that start <=131 for any Prime <=10**12 (Not used this fact for this soln but used to get to N=5477083)
# Sum form 131 upto 5477083 just greater than 10**12
# Sliding window approach with max L precomputed
import math
N=5477090
prime=[True]*(N)
p=set()
P=[]
for i in range(2,N):
    if prime[i]==True:
        p.add(i)
        P.append(i)
        for pr in range(2*i,N,i):
            prime[pr]=False
def isprime(n):
    x=math.sqrt(n)+1
    i=0
    while P[i]<=x:
        if n%P[i]==0:
            return False
        i=i+1
    p.add(n)
    return True
t=int(input())
for xyz in range(t):
    n=int(input())
    if n<5:
        print(2,1)
    else:
        L=0
        s=0
        while L<len(P) and s<=n:
            s=s+P[L]
            L=L+1
        for k in range(L,1,-1):
            s=0
            f=0
            for i in range(k):
                s=s+P[i]
            if s<=n and (s in p or isprime(s)):
                print(s,k)
                break
            else:
                i=k
                while i<len(P) and s<=n:
                    s=s+P[i]-P[i-k]
                    if s<=n and (s in p or isprime(s)):
                        print(s,k)
                        f=1
                        break
                    i+=1
                if f==1:
                    break
