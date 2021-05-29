c=1
i=3
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
    i=i+2
t = int(input())
for a0 in range(t):
    n = int(input())
    print(ans[n-1])
