import random
#n = int(input("Enter the number ").strip())
m=-1
#print (n, file=sys.stderr)
def gettriplets(n):
    s=set()
    for a in range(2*n//3,n-1):
        x=n-a
        for b in range(x//2-1,x-1):
            c=n-(a+b)
            if c>0 and a!=b and a!=c and b!=c and a*a==b*b+c*c:
                s.add(tuple(sorted([a,b,c])))
    return s
def triplets(n):
    s=set()
    for a in range(1,n):
        for b in range(1,n):
            c=n-(a+b)
            if c>0 and a!=b and a!=c and b!=c and (a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a):
                s.add(tuple(sorted([a,b,c])))
    return s
for xyz in range(0,1000):
    n=random.randint(1,100)
    if list(sorted(list(triplets(n))))!=list(sorted(list(gettriplets(n)))):
        print(n)
        break
    else:
        print("OK")
