# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N=int(input())
n=1
d=1
c=0
for i in range(0,N+1):
    if int(math.log(n,10))-int(math.log(d,10))>=1:
        print(i)
        c=c+1
    n,d=n+2*d,n+d
