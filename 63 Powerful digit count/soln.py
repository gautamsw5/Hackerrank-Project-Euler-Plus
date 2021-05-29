# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(1,10):
    x=i**n
    if x>=10**(n-1) and x<10**n:
        print(x)
