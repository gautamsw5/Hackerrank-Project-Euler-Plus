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
primes = [True]*1000001
primes[0]=False
primes[1]=False
p=set()
for i in range(2,1000001):
    if primes[i]:
        p.add(i)
        for k in range(2*i,1000001,i):
            primes[k]=False
print(primes[17])
for i in p:
    if len(str(i))==5 and str(i)[4]=='1' and check(i):# and str(i)[1]==str(i)[2] and str(i)[2]==str(i)[3] and str(i)[0]=='9':
        print(i)
