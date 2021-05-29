import math
N=5477083
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
dct={1:2}
m=1
'''for i in range(32):
    c=1
    s=P[i]
    j=i+1
    while j<len(P) and s<=10**12:
        s=s+P[j]
        c=c+1
        if (s in p or isprime(s)):
            if (c in dct and dct[c]>s or not c in dct):
                #print(s)
                dct[c]=s
        j=j+1
    print("done",P[i])
print(dct)'''
