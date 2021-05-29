import math
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m=-1
    while(n%2==0):
        n=n//2
        m=2
    i=3
    while(i<int(math.sqrt(n))+1):
        while(n%i==0):
            n=n//i
            m=i
        i=i+2
    if(n>2):
        m=n
    print(m)
