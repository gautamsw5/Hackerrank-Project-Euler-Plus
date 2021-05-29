# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for xyz in range(t):
    N=(int(input())-1)//2-1
    ans=24*N+18*N*(N+1)+(8*N*(N+1)*(2*N+1))//3+25
    print(ans%1000000007)
