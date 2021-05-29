# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def pent(k):
    x=math.sqrt(1+24*k)
    if math.floor(x)==math.ceil(x) and int(x)>4 and int(x+1)%6==0:
        return True
    return False
def Pent(n):
    return (n*(3*n-1))//2
N,k=map(int,input().split())
for n in range(k+1,N):
    if pent(Pent(n)+Pent(n-k)) or pent(Pent(n)-Pent(n-k)):
        print(Pent(n))
