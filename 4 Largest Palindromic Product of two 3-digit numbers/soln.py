import sys


t = int(input().strip())
for a0 in range(t):
    n = eval(input().strip())
    x=n//1000
    if n%1000<=int(str(x)[::-1]):
        x=x-1
    f=1
    while f==1:
        k=x*1000+int(str(x)[::-1])
        for i in range(100,1000):
            if k%i==0 and k//i>99 and k//i<1000:
                f=0
                print(i,"*",k//i," = ",k)
                break
        x=x-1
