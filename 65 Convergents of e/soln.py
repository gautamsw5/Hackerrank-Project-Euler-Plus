def sod(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
def get(new,num,den):
    return new*num+den,num
n=int(input())
if n==1:
    print(2)
elif n==2:
    print(3)
elif n%3==1:
    num=1
    den=1
    k=(n-1)//3   # 3k+1 th term is being found
    i=2*k
    while i>2:
        num,den=get(i,num,den)
        num,den=get(1,num,den)
        num,den=get(1,num,den)
        i=i-2
    num,den=get(2,num,den)
    num,den=get(1,num,den)
    num,den=get(2,num,den)
    #print(num,den)
    print(sod(num))
elif n%3==0:
    k=n//3
    den=1
    num=2*k
    i=num-2
    while i>=2:
        num,den=get(1,num,den)
        #print(num,den)
        num,den=get(1,num,den)
        #print(num,den)
        num,den=get(i,num,den)
        #print(num,den)
        i=i-2
    num,den=get(1,num,den)
    #print(num,den)
    num,den=get(2,num,den)
    #print(num,den)
    print(sod(num))
else:
    k=(n-2)//3
    den=1
    num=1
    i=2*k-2
    num,den=get(1,num,den)
    #print(num,den)
    num,den=get(i+2,num,den)
    #print(num,den)
    while i>=2:
        num,den=get(1,num,den)
        #print(num,den)
        num,den=get(1,num,den)
        #print(num,den)
        num,den=get(i,num,den)
        #print(num,den)
        i=i-2
    num,den=get(1,num,den)
    #print(num,den)
    num,den=get(2,num,den)
    #print(num,den)
    print(sod(num))
