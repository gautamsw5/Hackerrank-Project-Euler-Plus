import math
def sqrt(n):
    p=1
    r=n
    while p<=r:
        m=(p+r)//2
        if m*m==n:
            return m
        elif m*m<n and (m+1)*(m+1)>n:
            return -1
        elif m*m<n:
            p=m+1
        else:
            r=m-1
'''
if mx<sqrt(1+D*y*y):
    mx=sqrt(1+D*y*y)                
'''
mx=0
for D in range(10**4+1):
    if sqrt(D)==-1:
        y=1
        while True:
            mx=sqrt(1+D*y*y)
            if mx!=-1:
                print(D,mx)
                break
            y=y+1
