def palin(n):
    return str(n)==str(n)[::-1]
c=0
m=0
for i in range(10**4):
    x=i
    f=0
    for xyz in range(51):
        x=x+int(str(x)[::-1])
        if palin(x):
            f=1
            break
    if f==0:
        c=c+1
print(c)
