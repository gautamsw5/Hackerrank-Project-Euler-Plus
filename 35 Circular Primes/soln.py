c=1
i=3
ans=set()
ans.add(2)
while c<100111:
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
        ans.add(i)
    i=i+2
def prime(n):
    '''i=2
    while i*i<n:
        if n%i==0:
            return False
    return True'''
    return n in ans
def circularprime(n):
    x=str(n)
    if not prime(n):
        return False
    for i in range(1,len(x)):
        x=x[len(x)-1]+x[:len(x)-1]
        if not prime(int(x)):
            return False
    return True
Ans=[]
for i in range(2,10**6+1):
    if circularprime(i):
        Ans.append(i)
print(Ans)
