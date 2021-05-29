#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s=n*n*(n-1) - n*(n-1)*(2*n-1)//3 + n*n - n*(n-1)//2
    print((n*n*(n+1)*(n+1))//4-s)
