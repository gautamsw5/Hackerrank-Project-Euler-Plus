N,k=map(int,input().split())
numPrimeFactors=[0]*(N+5)
numPrimeFactors[0]=1
numPrimeFactors[1]=1
for i in range(2,N+5):
    if numPrimeFactors[i]==0:
        for p in range(2*i,N+5,i):
            numPrimeFactors[p]+=1
if k==2:
    i=2
    while i<=N:
        if numPrimeFactors[i]==4 and numPrimeFactors[i+1]==4 and numPrimeFactors[i+2]==4 and numPrimeFactors[i+3]==4:
            print(i)
        i+=1
elif k==3:
    i=2
    while i<=N:
        if numPrimeFactors[i]==3 and numPrimeFactors[i+1]==3 and numPrimeFactors[i+2]==3:
            print(i)
        i+=1
else:
    i=2
    while i<=N:
        if numPrimeFactors[i]==2 and numPrimeFactors[i+1]==2:
            print(i)
        i+=1
