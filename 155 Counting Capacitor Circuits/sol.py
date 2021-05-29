import math
n = 18 #int(input().strip())
def add(a, b):
    x = a[0]*b[1] + b[0]*a[1]
    y = a[1]*b[1]
    return (x//math.gcd(x,y), y//math.gcd(x,y))
D = [set(), set([(60,1)])]
arr = [1]
master = set(D[1])
for i in range(2, n+1):
    D.append(set())
    a = 1
    while a <= i - a:
        b = i - a
        for c1 in D[a]:
            for c2 in D[b]:
                D[i].add(add(c1, c2))
                sec = add((c1[1], c1[0]), (c2[1], c2[0]))
                D[i].add((sec[1], sec[0]))
        a += 1
    master = master.union(D[i]) 
    arr.append(len(master))
print(arr)