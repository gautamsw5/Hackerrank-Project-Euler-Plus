t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3=0
    n5=0
    n15=0
    if n>3:
        m=(n-1)//3
        n3=3*m*(m+1)//2
    if n>5:
        m=(n-1)//5
        n5=5*m*(m+1)//2
    if n>15:
        m=(n-1)//15
        n15=15*m*(m+1)//2
    ans=n3+n5-n15
    print(ans)
