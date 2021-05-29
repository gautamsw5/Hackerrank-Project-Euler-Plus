import sys
import time
tx=time.time()
c=1
i=3
ans=[2]
s=[2]
while c<148934:
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
        s.append(s[len(s)-1]+i)
    i=i+2
print(time.time()-tx)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n>=ans[len(ans)-1]:
        print(s[len(s)-1])
    elif n==ans[0]:
        print(ans[0])
    elif n<ans[0]:
        print(0)
    else:
        l=0
        r=len(ans)
        while l<=r:
            m=l+(r-l)//2
            if (n<ans[m+1] and n>ans[m]) or n==ans[m]:
                print(s[m])
                break
            elif n>ans[m]:
                l=m+1
            else:
                r=m-1
