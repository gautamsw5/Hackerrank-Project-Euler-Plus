def curious(n):
    fact=[1,1,2,6,24,120,720,5040,40320,362880]
    x=n
    s=0
    while x>0:
        s=s+fact[x%10]
        x=x//10
    return n==s
def curious2(n):
    fact=[1,1,2,6,24,120,720,5040,40320,362880]
    x=n
    s=0
    while x>0:
        s=s+fact[x%10]
        x=x//10
    return s%n==0
ans=[]
for i in range(10,10**5+1):
    if(curious2(i)):
        ans.append(i)
