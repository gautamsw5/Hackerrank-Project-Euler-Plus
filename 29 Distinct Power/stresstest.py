import math
def bforce(n): # Stupid approach
    ans=set()
    for a in range(2,n+1):
        ans.add(a**a)
        for b in range(a+1,n+1):
            ans.add(a**b)
            ans.add(b**a)
    return len(ans)
def log(N,k):  # math.log is fucked up!!
    c=k
    ret=0
    while c<=N:
        c=c*k
        ret+=1
    return ret
def mysol(N):
#N=int(input())
    arr=[0]
    s=set()
    i=1
    while i<=math.log(N,2)+1:
        for n in range(2,N+1):
            s.add(i*n)
        arr.append(len(s))   # arr[i] is count of distinct multiples of 2,3,4,...,i (upto N for each i)
                             # Ex. N=5, i=4
                             # 2,  3,  4,  5  ,i=1                              --> 4
                             # 4,  6,  8, 10  ,i=2  (include i=1 also)          --> 7
                             # 6,  9, 12, 15  ,i=3  (include i=1,i=2 also)      --> 10
                             # 8, 12, 16, 20  ,i=4  (include i=1,i=2,i=3 also)  --> 12
        #print(N,i,s)
        i=i+1
    #print(arr)
    s2=set()   # Store powers of numbers >=2 and <=N upto N power ex. --> 4,8,16,32,... ,9,27,81,... ,16,... like that
    s3=set()   # Tried to store 1powers <= _|(N) but included some non 1 powers unintentionally
    for i in range(2,N+1):
        j=2
        ad=i*i
        while ad<=N:
            s2.add(ad)
            ad*=i
            j=j+1
        if i*i<=N:
            s3.add(i)
    ans=0
    for a in range(2,N+1):
        if not(a in s2 or a in s3): # 1powers > _|(N)
            #print(a)
            ans+=N-1
        elif (a in s3 and not a in s2): # 1powers <= _|(N)
            #print(a,int(math.log(N,a)))
            ans+=arr[log(N,a)]          # arr[Highest power of a <= N] gives number of distinct powers in required range
#print(ans)
    return ans
def lcm(k, i):
    if i % k == 0:
        return i
    else:
        i_ = i
        k_ = k
        r = i % k;
        while (r != 0):
            i = k
            k = r
            r = i % k
        return i_ * k_ / k

def realsol(maxExponent):
    MaxBasePower = 16
    minExponent=[0]*((maxExponent+1)*MaxBasePower)
    for i in range(1,MaxBasePower+1):
        for j in range(1,maxExponent+1):
            if (minExponent[i*j] == 0):
                minExponent[i*j] = i
    base=[0]*(maxExponent + 1)
    repeated=0
    for x in range(2,maxExponent+1):
        parent = base[x]
        if (parent == 0):
            power = x * x
            while (power <= maxExponent):
                base[power] = x
                power *= x
            continue
        exponent = 0
        reduce = x
        while (reduce > 1):
            reduce //= parent
            exponent+=1
        for y in range(2,maxExponent+1):
            if (minExponent[y * exponent] < exponent):
                repeated+=1
    alll = maxExponent - 1
    result = alll*alll - repeated
    return result
def stresstest():
    for i in range(1,10**5+1):
        r=realsol(i)
        my=mysol(i)
        if r==my:
            print(i,"OK")
        else:
            print("Wrong")
            print(i,r)
            break
'''a=[]
for i in range(2,10**5+1):
    a.append(mysol(i))'''
'''t=int(input())
m=0
kk=0
for n in range(893,t+1):
    
    #print((n-1)*(n-1),(n-1)*(n-1)-ans,ans)
    my=mysol(n)
    ans=bforce(n)
    #print(n,ans,my,(ans-my))
    if ans!=my:
        if abs(ans-my)>m:
            m=abs(ans-my)
            kk=n
        print("n =",n," ans =",ans," your ans =",my)'''
