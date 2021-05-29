import time
tx=time.time()
primes=[True]*2000005    #2000005
pfactors=[]
for i in range(2000005):
    pfactors.append(set())
# Generate primes and pfactors
i=2
while i<2000005:
    if primes[i]:
        j=2
        while j*j<=i:
            if i%j==0:
                pfactors[i].add(j)
                pfactors[i].add(i//j)
                primes[i]=False
            j+=1
        if primes[i]:
            for k in range(2*i,2000005,i):
                primes[k]=False
                pfactors[k].add(i)
    i+=1
print(time.time()-tx)
# input
N=2000000
#K=4

# main thing
def four():
    i=2
    k=0
    ans4=[]
    while i<=N:
        if len(pfactors[i])==4 and len(pfactors[i+1])==4 and len(pfactors[i+2])==4 and len(pfactors[i+3])==4:
            ans4.append(i)
        i+=1
    print(ans4)
def three():
    i=2
    k=0
    ans3=[]
    while i<=N:
        if len(pfactors[i])==3 and len(pfactors[i+1])==3 and len(pfactors[i+2])==3:
            ans3.append(i)
        i+=1
    print(ans3)
def two():
    i=2
    k=0
    ans2=[]
    while i<=N:
        if len(pfactors[i])==2 and len(pfactors[i+1])==2:
            ans2.append(i)
        i+=1
    print(ans2)
