import math
#import time
#tx=time.time()
c=1
i=3
anss=set()
anss.add(2)
ans=[2]
while i<5*(10**5)+1:
    prime=True
    if i%2==0:
        prime=False
    else:
        j=3
        while j*j<=i:
            if i%j==0:
                prime=False
                break
            j=j+2
    if prime:
        c=c+1
        ans.append(i)
        anss.add(i)
    i=i+2
k=4
def Pfactors(n):
    ret=set()
    i=2
    while i*i<=n:
        if n%i==0:
            if i in anss:
                ret.add(i)
            if n//i in anss:
                ret.add(n//i)
            if len(ret)>k:
                break
        i=i+1
    return list(ret)
k=2
ans2=[]
for n in range(10**5,2*10**6+1):
    if len(Pfactors(n))==k and len(Pfactors(n+1))==k:# and len(Pfactors(n+2))==k:# and len(Pfactors(n+3))==k:
        ans2.append(n)
print("ANS 2 \n\n")
print(ans2)
k=3
ans3=[]
for n in range(10**5,2*10**6+1):
    if len(Pfactors(n))==k and len(Pfactors(n+1))==k and len(Pfactors(n+2))==k:# and len(Pfactors(n+3))==k:
        ans3.append(n)
print("ANS 3 \n\n")
print(ans3)
k=4
ans4=[]
for n in range(10**5,2*10**6+1):
    if len(Pfactors(n))==k and len(Pfactors(n+1))==k and len(Pfactors(n+2))==k and len(Pfactors(n+3))==k:
        ans4.append(n)
print("ANS 4 \n\n")
print(ans4)
