import itertools
primes=[]
p=set()
for i in range(1001,1000001,2):
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
print("done")
def perm(n): # perms of n that are greater than n and are prime 
    ret=set()
    for i in itertools.permutations(str(n)):
        s=0
        for d in i:
            s=s*10+ord(d)-ord('0')
        if s>n and s in p:
            ret.add(s)
    return ret
# k=3
#'''
for a in primes:
    for b in perm(a):
        c=(a+b)//2
        if a<b and c in p and sorted(str(a))==sorted(str(b)) and sorted(str(b))==sorted(str(c)):
            print(a,c,b)
#'''
# k=4
'''
for a in primes:
    for b in perm(a):
        c=(a+b)//2
        d=b+c-a
        if c in p and d in p and sorted(str(b))==sorted(str(c)) and sorted(str(c))==sorted(str(d)):
            print(a,c-a)
'''
'''
s=set()
while True:
    y=input()
    if y=="done":
        break
    x=tuple(map(int,y.split()))
    s.add(x)
z=list(s)
z.sort()
print(z)
'''
