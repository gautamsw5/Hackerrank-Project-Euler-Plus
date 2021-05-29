def pandigital(a,b,c,n):
    x=[0]*10
    y=[0]+[1]*n+(10-1-n)*[0]
    while a>0:
        x[a%10]+=1
        a=a//10
    while b>0:
        x[b%10]+=1
        b=b//10
    while c>0:
        x[c%10]+=1
        c=c//10
    return x==y
for i in range(4,10):
    print(i,([0]+[1]*i+(10-1-i)*[0]))
    s=set()
    for a in range(1,1964):
        for b in range(1,149):
            if(pandigital(a,b,a*b,i)):
                s.add(a*b)
                print(a,"X",b,"=",a*b)
    print(i,"-->",sum(list(s)))
