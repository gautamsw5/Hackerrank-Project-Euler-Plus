# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=0
for i in range(1,n+1):
    s+=pow(i,i,10**10)
print(s%(10**10))
