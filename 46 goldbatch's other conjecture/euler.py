import math
c=1
i=3
anss=set()
ans=[2]
while c<10001:
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
        ans.append(i)
        anss.add(i)
    i=i+2
for n in range(9,10**4,2):
    i=0
    f=0
    while ans[i]<n:
        x=math.sqrt((n-ans[i])//2)
        #print(x,n,ans[i])
        if math.floor(x)==math.ceil(x):
            f=1
            break
        i=i+1
    if f==0 and not n in anss:
        print(n)
        
