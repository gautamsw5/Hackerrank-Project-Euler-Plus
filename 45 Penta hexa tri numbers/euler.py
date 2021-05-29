import math
def pent(k):
    x=math.sqrt(1+24*k)
    if math.floor(x)==math.ceil(x) and int(x)>4 and int(x+1)%6==0:
        return True
    return False
def hexa(k):
    x=math.sqrt(1+8*k)
    if math.floor(x)==math.ceil(x) and int(x)>2 and int(x+1)%4==0:
        return True
    return False
print("P T\n\n")
for i in range(10000000,20000000):
    n=(i*(i+1))//2
    if pent(n):
        print(n)
print("\n\nP H\n\n")
for i in range(10000000,20000000):
    n=i*(2*i-1)
    if pent(n):
        print(n)
