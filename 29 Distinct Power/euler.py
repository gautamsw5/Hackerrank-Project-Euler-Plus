n=100
ans=set()
for a in range(2,n+1):
    ans.add(a**a)
    for b in range(a+1,n+1):
        ans.add(a**b)
        ans.add(b**a)
print(len(ans))
