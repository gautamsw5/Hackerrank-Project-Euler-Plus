import time
import math
p=set()
np=set()
P=[]
tx=time.time()
prime=[True]*20000003
for i in range(2,20000003):
    if prime[i]:
        p.add(i)
        P.append(i)
        for k in range(2*i,20000003,i):
            prime[k]=False
print(time.time()-tx)
def isprime(n):
    if n in p:
        return True
    elif n<P[-1] and not n in p:
        return False
    elif n in np:
        return False
    lim=math.sqrt(n)+2
    for i in P:
        if i>lim:
            break
        if n%i==0:
            np.add(n)
            return False
    p.add(n)
    return True
with open("5.txt","a") as f:
    for a in P[:2262]:
        for b in P[:2262]:
            if a<b and isprime(int(str(a)+str(b))) and isprime(int(str(b)+str(a))):
                for c in P[:2262]:
                    if b<c and isprime(int(str(a)+str(c))) and isprime(int(str(c)+str(a))) and isprime(int(str(c)+str(b))) and isprime(int(str(b)+str(c))):
                        for d in P[:2262]:
                            if c<d and isprime(int(str(a)+str(d))) and isprime(int(str(d)+str(a))) and isprime(int(str(c)+str(d))) and isprime(int(str(d)+str(c))) and isprime(int(str(b)+str(d))) and isprime(int(str(d)+str(b))):
                                for e in P[:2262]:
                                    if d<e and isprime(int(str(a)+str(e))) and isprime(int(str(e)+str(a))) and isprime(int(str(b)+str(e))) and isprime(int(str(e)+str(b))) and isprime(int(str(e)+str(c))) and isprime(int(str(c)+str(e))) and isprime(int(str(e)+str(d))) and isprime(int(str(d)+str(e))):
                                        print(a,b,c,d,e)
                                        f.write(str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+"\n")
print(time.time()-tx)
x=input("Done")
