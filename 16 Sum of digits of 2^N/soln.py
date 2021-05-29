# Enter your code here. Read input from STDIN. Print output to STDOUT
def sod(n):
    s=0
    while(n>0):
        s=s+n%10
        n=n//10
    return s
t=int(input())
for i in range(t):
    print(sod(2**int(input())))
