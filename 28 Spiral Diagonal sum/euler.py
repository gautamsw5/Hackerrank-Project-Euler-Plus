n=int(input())
Y=(n+1)//2
x=1
i=1
d=2
s=n*n
while i<n*n:
    for t in range(4):
        s=s+i
        i=i+d
    d=d+2
