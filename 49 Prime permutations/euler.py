primes=[]
p=set()
for i in range(1001,10000,2):
    if i%2!=0:
        j=3
        f=0
        while j*j<=i:
            if i%j==0:
                f=1
                break
            j+=1
        if f==0:
            primes.append(i)
            p.add(i)
for a in primes:
    for b in primes:
        c=(a+b)//2
        if a!=b and c in p and sorted(str(a))==sorted(str(b)) and sorted(str(b))==sorted(str(c)):
            print(a,c,b)
