# Enter your code here. Read input from STDIN. Print output to STDOUT
arr=[0]*23928
arr[1]=1
arr[2]=1
brr=[0]*5001
x=1
for i in range(3,23928):
    arr[i]=arr[i-1]+arr[i-2]
    if brr[x]==0 and arr[i]//(10**x)>0:
        brr[x]=i
        x=x+1
t=int(input())
for i in range(t):
    n=int(input())
    print(brr[n-1])
