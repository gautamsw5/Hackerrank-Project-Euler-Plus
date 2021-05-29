import sys
c=1
i=3
ans=[2]
while c<305: # 305 because 303th prime -> 1999 is largest possible value of b because |b| <= N and 42 <= N <= 2000
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
c=0
m=0
A=0
B=0
i=0
p=set(ans)
N=int(input())
while ans[i]<=N:
    b=ans[i]
    for a in range(-N,N+1):
        n=0
        while n*n+a*n+b in p:
            n=n+1
        if n>m:
            m=n
            A=a
            B=b
    i=i+1
print(str(A)+" "+str(B))
