n,k=map(int,input().split())
c=0
fact=[1,1]
for i in range(2,n+1):
    fact.append(i*fact[-1])
for n in range(1,n+1):
    for r in range(n):
        if fact[n]/(fact[r]*fact[n-r])>k:
            c=c+1
print(c)
