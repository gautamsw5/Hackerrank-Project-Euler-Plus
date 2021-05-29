'''def pandigital(arr,n):
    return arr==[0]+[1]*n+(10-1-n)*[0]
m="0"
for n in range(1,10**5):
    arr=[0]*10
    s=""
    for k in range(1,10):
        x=n*k
        s=s+str(x)
        while x>0:
            arr[x%10]+=1
            x=x//10
        if pandigital(arr,9):
            print(n)
            if s>m:
                m=s
            break'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def pandigital(arr,n):
    return arr==[0]+[1]*n+(10-1-n)*[0]
N,K=map(int,input().split())
for n in range(2,N):
    arr=[0]*10
    for k in range(1,10):
        x=n*k
        while x>0:
            arr[x%10]+=1
            x=x//10
        if pandigital(arr,K):
            print(n)
            break
