import math
def pent(k):
    x=math.sqrt(1+24*k)
    if math.floor(x)==math.ceil(x) and int(x)>4 and int(x+1)%6==0:
        return True
    return False
D=10**100
for a in range(1,3000):
    for b in range(1,2000):
        s=(a*(3*a-1))//2+(b*(3*b-1))//2
        d=abs((b*(3*b-1))//2-(a*(3*a-1))//2)
        if pent(d) and pent(s):
            print(a,b)
            if d<D:
                D=d
print(D)
