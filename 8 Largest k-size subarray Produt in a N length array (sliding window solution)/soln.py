import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    num=list(str(num))
    if k==1:
        print(ord(max(num))-ord('0'))
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
        print(mx)
