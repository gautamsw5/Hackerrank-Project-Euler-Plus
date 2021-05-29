import itertools
s=set()
def perm(arr):
    ret=set()
    for i in itertools.permutations(arr):
        su=0
        for j in i:
            su=su*10+j
        ret.add(su)
    return ret
def insert(n,c,i):
    x=str(n)
    x=x[:i]+str(c)+x[i:]
    return int(x)
'''
# n=2 k=1
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
'''
'''
# n=3 k=1
for n in range(10,100):
    for d in range(n+1,100):
        for c in range(1,10):
            for i in range(3):
                x=insert(n,c,i)
                for j in range(3):
                    y=insert(d,c,j)
                    if x!=y and x*d==y*n and x>99 and y>99:
                        s.add((min(x,y),max(x,y)))
'''
'''
# n=3 k=2
for n in range(1,10):
    for d in range(n+1,10):
        for c1 in range(1,10):
            for c2 in range(1,10):
                for x in perm([c1,c2,n]):
                    for y in perm([c1,c2,d]):
                        if x!=y and x*d==y*n and x>99 and y>99:
                            s.add((min(x,y),max(x,y)))
'''
'''
# n=4 k=1
for n in range(100,1000):
    for d in range(n+1,1000):
        for c in range(1,10):
            for i in range(4):
                x=insert(n,c,i)
                for j in range(4):
                    y=insert(d,c,j)
                    if x!=y and x*d==y*n:
                        s.add((min(x,y),max(x,y)))
'''
'''
# n=4 k=2
for n in range(100):
    for d in range(100):
        for c1 in range(1,10):
            for c2 in range(1,10):
                A=n//10
                B=n%10
                C=d//10
                D=d%10
                X=set()
                Y=set()
                X.add(A*1000+B*100+c1*10+c2)
                X.add(A*1000+B*100+c2*10+c1)
                X.add(A*1000+c1*100+B*10+c2)
                X.add(A*1000+c2*100+B*10+c1)
                X.add(A*1000+c1*100+c2*10+B)
                X.add(A*1000+c2*100+c1*10+B)
                X.add(c1*1000+A*100+B*10+c2)
                X.add(c2*1000+A*100+B*10+c1)
                X.add(c1*1000+A*100+c2*10+B)
                X.add(c2*1000+A*100+c1*10+B)
                X.add(c1*1000+c2*100+A*10+B)
                X.add(c2*1000+c1*100+A*10+B)
                Y.add(C*1000+D*100+c1*10+c2)
                Y.add(C*1000+D*100+c2*10+c1)
                Y.add(C*1000+c1*100+D*10+c2)
                Y.add(C*1000+c2*100+D*10+c1)
                Y.add(C*1000+c1*100+c2*10+D)
                Y.add(C*1000+c2*100+c1*10+D)
                Y.add(c1*1000+C*100+D*10+c2)
                Y.add(c2*1000+C*100+D*10+c1)
                Y.add(c1*1000+C*100+c2*10+D)
                Y.add(c2*1000+C*100+c1*10+D)
                Y.add(c1*1000+c2*100+C*10+D)
                Y.add(c2*1000+c1*100+C*10+D)
                for x in X:
                    for y in Y:
                        if not(n==0 and d==0) and x!=y and x*d==y*n and x>999 and y>999:
                            s.add((min(x,y),max(x,y)))
'''
'''
# n=4 k=3
for c1 in range(1,10):
    for c2 in range(1,10):
        for c3 in range(1,10):
            for n in range(1,10):
                for d in range(n+1,10):
                    N=[c1,c2,c3,n]
                    D=[c1,c2,c3,d]
                    for x in perm(N):
                        for y in perm(D):
                            if x!=y and x*d==y*n:
                                s.add((min(x,y),max(x,y)))
'''
n=0
d=0
for i in s:
    n+=i[0]
    d+=i[1]
print(n,d)
x=input()
