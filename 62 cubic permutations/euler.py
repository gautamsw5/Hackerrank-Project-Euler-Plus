def count(n):
    arr=[0]*10
    while n>0:
        arr[n%10]+=1
        n=n//10
    return tuple(arr)
i=100
dct={}
while i<10**4:
    x=count(i**3)
    if x in dct:
        dct[x]+=1
        if dct[x]==5:
            print(x)
    else:
        dct[x]=1
    i=i+1
