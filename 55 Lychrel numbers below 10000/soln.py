def palin(n):
    return str(n)==str(n)[::-1]
m=0
dct={}
n=int(input())
for i in range(1,n+1):
    x=i
    for xyz in range(62):
        if palin(x):
            if x in dct:
                dct[x]+=1
            else:
                dct[x]=1
            break
        x=x+int(str(x)[::-1])
ans=0
for i in dct:
    if dct[i]>m:
        m=dct[i]
        ans=i
print(ans,m)
