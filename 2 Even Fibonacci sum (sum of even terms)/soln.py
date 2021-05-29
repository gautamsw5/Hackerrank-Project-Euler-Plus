#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=1
    b=2
    s=0
    while(a<n):
        if(a%2==0):
            s=s+a
        a,b=b,a+b
        #print(a)
    print(s)
