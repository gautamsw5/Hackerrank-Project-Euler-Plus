def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def same(a,b,c,d):
    return a//gcd(a,b)==c//gcd(c,d) and b//gcd(a,b)==d//gcd(c,d)
for c in range(1,10):
    for a in range(1,10):
        for b in range(1,10):
            if 10*a+c<10*b+c and same(a,b,10*a+c,10*b+c):
                print(str(a)+str(c)+"/"+str(b)+str(c))
            if 10*a+c<10*c+b and same(a,b,10*a+c,10*c+b):
                print(str(a)+str(c)+"/"+str(c)+str(b))
            if 10*c+a<10*b+c and same(a,b,10*c+a,10*b+c):
                print(str(a)+str(c)+"/"+str(b)+str(c))
            if 10*c+a<10*c+b and same(a,b,10*c+a,10*c+b):
                print(str(a)+str(c)+"/"+str(c)+str(b))
