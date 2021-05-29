import sys
import math
dct={}
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m=-1
    #print (n, file=sys.stderr)
    if n in dct:
        m=dct[n]
    else:
        for a in range(1,n):
            s=1.0*n-1.0*a
            prod=(s*s-1.0*a*a)/2.0
            if(s*s>4.0*prod and 1.0*a*prod>1.0*m):
                D=math.sqrt(s*s-4.0*prod)
                if(math.floor(D)==math.ceil(D) and s+D>0 and s-D>0):
                    m=int(a*prod)
        dct[n]=m
    print(m)
def bforce(n):
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        m=-1
        #print (n, file=sys.stderr)
        if n in dct:
            m=dct[n]
        else:
            for a in range(n//3,n-2):
                x=n-a
                for b in range(x//2,x-1):
                    c=n-(a+b)
                    #print(a,b,c)
                    if a**2==b**2+c**2 and c!=b:
                        m=max(m,a*b*c)
            dct[n]=m
        print(m)
