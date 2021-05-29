def count(m,n):
    c=0
    for i in range(m):
        for j in range(n):
            #print((i+1),(j+1),"->",(m-i)*(n-j))
            c=c+(m-i)*(n-j)
    return c
mind = 2*10**6
I=0
J=0
for i in range(1,100):
    for j in range(1,100):
        x = count(i,j)
        if abs(2*10**6-x)<mind:
            mind=abs(2*10**6-x)
            I=i
            J=j
