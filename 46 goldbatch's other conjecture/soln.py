import math
#import time
#tx=time.time()
c=1
i=3
anss=set()
ans=[]
while i<5*(10**5)+1:
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
dct=[0]*250000
#print("Latest Prime: ",ans[-1])
def nos(n):
    i=0
    while ans[i]<n:
        x=math.sqrt((n-ans[i])//2)
        #print(x,n,ans[i])
        if math.floor(x)==math.ceil(x):
            dct[(n-9)//2]+=1
            print(n,ans[i],x)
        #print(dct[n])
        i=i+1
    return dct[(n-9)//2]
for p in ans:
    k=1
    while p+2*k*k<5*(10**5):
        n=p+2*k*k
        if not n in anss:
            dct[(n-9)//2]+=1
        k=k+1
t=int(input())
for xyz in range(t):
    n=int(input())
    print(dct[(n-9)//2])
#print(time.time()-tx)
'''for n in range(9,5*(10**5)+1,2):
    if not n in anss:
        nos(n)'''
'''for n in range(9,100,2):
    if not n in anss:
        nos(n)'''
