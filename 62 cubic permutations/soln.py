def count(n):
    arr=[0]*10
    while n>0:
        arr[n%10]+=1
        n=n//10
    return tuple(arr)
i=1
dct={}
dct2={}
n,k=map(int,input().split())
while i<n:
    x=count(i**3)
    if x in dct:
        dct[x]+=1
    else:
        dct[x]=1
        dct2[x]=i
    i=i+1
for i in dct:
    if dct[i]==k:
        print(dct2[i]**3)
