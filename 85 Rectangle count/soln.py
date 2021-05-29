def count(m,n):
    c=0
    for i in range(m):
        for j in range(n):
            #print((i+1),(j+1),"->",(m-i)*(n-j))
            c=c+(m-i)*(n-j)
    return c
I=0
J=0
countr=[[0 for i in range(201)] for j in range(201)]
for i in range(1,200):
    for j in range(1,200):
        countr[i][j] = count(i,j)
'''t=int(input())
for xyz in range(t):
    x = int(input())
    
'''
