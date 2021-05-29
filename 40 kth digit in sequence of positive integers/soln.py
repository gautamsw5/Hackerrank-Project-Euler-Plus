import random
num_of_i_dig_nums=[0]
for i in range(21):
    num_of_i_dig_nums.append(9*(10**i))
num_of_dig_in_i_dig_nums=[0]
for i in range(1,21):
    num_of_dig_in_i_dig_nums.append(i*num_of_i_dig_nums[i])
cumularr=[0]
for i in range(1,21):
    cumularr.append(cumularr[-1]+num_of_dig_in_i_dig_nums[i])
def binn(N):
    l=0
    r=len(cumularr)-1
    while l<=r:
        m = (r-l)//2 + l
        if cumularr[m]<=N and cumularr[m+1]>N:
            N=N-cumularr[m]
            if N==0:
                return m,N
            return m+1,N
        elif cumularr[m]<N:
            l=m+1
        else:
            r=m-1
def lin(N):
    i=0
    while N-num_of_dig_in_i_dig_nums[i]>0:
        N=N-num_of_dig_in_i_dig_nums[i]
        i=i+1
    return i,N
def stresstest():
    while True:
        n=random.randint(1,10**3+1)
        if lin(n)!=binn(n):
            print(n,lin(n),binn(n))
            break
        else:
            print(n,"OK")
def nthdigit(N):
    N=N-1
    if N==0:
        return 1
    if N<9:
        return N+1
    i=0
    '''while N-num_of_dig_in_i_dig_nums[i]>0:
        N=N-num_of_dig_in_i_dig_nums[i]
        i=i+1'''
    i,N=binn(N)
    k=10**(i-1)+N//i
    return int(str(k)[N%i])
t=int(input())
for xyz in range(t):
    d=list(map(int,input().split()))
    p=1
    for i in d:
        p*=nthdigit(i)
    print(p)
    
