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
N=int(input())
print(mysol(N))
