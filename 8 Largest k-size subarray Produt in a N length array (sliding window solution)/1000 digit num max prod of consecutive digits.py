import sys
import random

'''t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()'''
def sliding(num,k):
    num=list(str(num))
    if k==1:
        return ord(max(num))-ord('0')
    else:
        arr = [ord(i)-ord('0') for i in num]
        i=0
        mx=0
        prod=1
        curr=0
        start=0
        #print(arr)
        while curr<len(arr):
            while curr<min(start+k,len(arr)) and arr[curr]!=0:
                prod=prod*arr[curr]
                curr=curr+1
            if curr==start+k and prod>mx:
                mx=prod
            if curr<len(arr) and arr[curr]!=0:
                if curr==start+k:
                    while curr<len(arr) and arr[curr]!=0:
                        if prod>mx:
                            mx=prod
                        prod=prod*arr[curr]//arr[start]
                        curr=curr+1
                        start+=1
                    if prod>mx:
                        mx=prod
                else:
                    break
            while curr<len(arr) and arr[curr]==0:
                start=curr+1
                prod=1
                curr=start
        return mx
'''t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()'''
def bforce(num,k):
    num=list(str(num))
    if k==1:
        return ord(max(num))-ord('0')
    else:
        mx=0
        arr = [ord(i)-ord('0') for i in num]
        for i in range(0,len(arr)-k+1):
            if arr[i]!=0:
                prod=arr[i]
                for j in range(i+1,i+k):
                    prod*=arr[j]
                    if prod==0:
                        break
                if prod>mx:
                    mx=prod
        return mx
for xyz in range(0,1000):
    k=random.randint(1,8)
    n=random.randint(10**k,10**1000)
    if bforce(n,k)==sliding(n,k):
        print("OK")
    else:
        print("n = ",n)
        print("k = ",k)
        print("ans = ",bforce(n,k))
        print("your ans = ",sliding(n,k))
        break
