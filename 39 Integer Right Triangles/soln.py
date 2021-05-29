import sys
import math
def nos(p):
    c=0
    for a in range(1,p):
        s=p-a
        prod=(s*s-a*a)/2
        if(s*s>4.0*prod):
            D=math.sqrt(s*s-4.0*prod)
            if(math.floor(D)==math.ceil(D) and s+D>0 and s-D>0 and int(D)%2==int(s)%2):
                c=c+1
                #print(a,int(s+D)//2,int(s-D)//2)
    return c
m=0
ii=0
i=720720
ans=[12, 60, 120, 240, 420, 720, 840, 1680, 2520, 4620, 5040, 9240, 18480,
27720, 55440, 110880, 120120, 166320, 180180, 240240, 360360,  720720, 1081080,
1441440, 2042040, 2162160, 2882880, 3603600, 4084080]
brr=[1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 16, 20, 25, 31, 40, 46, 50, 51, 53, 64, 80, 104, 105, 124, 130, 135, 142, 158, 168]

n=int(input())
while i<n+1:
    x=nos(i)
    if x>m:
        d=ii
        print(i,x,i//12)
        ans.append(i)
        m=x
        ii=i
    i=i+120120
print(ii,m)
