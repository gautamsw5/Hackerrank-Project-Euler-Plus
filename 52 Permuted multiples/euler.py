def count(n):
    arr=[0]*10
    while n>0:
        arr[n%10]+=1
        n=n//10
    return arr
i=1
ans=[]
while i<2000001:
    a,b=count(i),count(2*i)
    if a==b:
        ans.append(i)
    i=i+1
