def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def sod(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
def get(new,num,den):
    return new*num+den,num
num=1
den=1
k=33   # 3k+1 th term is being found
i=2*k
while i>2:
    num,den=get(i,num,den)
    print(num,den)
    num,den=get(1,num,den)
    print(num,den)
    num,den=get(1,num,den)
    print(num,den)
    i=i-2
num,den=get(2,num,den)
print(num,den)
num,den=get(1,num,den)
print(num,den)
num,den=get(2,num,den)
print(num,den)
