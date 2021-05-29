# Enter your code here. Read input from STDIN. Print output to STDOUT
arr=[0]*1001
arr[0]=1
brr=[0]*1001
brr[0]=1
for i in range(1,1001):
    arr[i]=arr[i-1]*i
    x=arr[i]
    while x>0:
        brr[i]+=x%10
        x=x//10
t=int(input())
for xyz in range(t):
    n=int(input())
    if n<len(brr):
        print(brr[n])
