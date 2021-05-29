# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=0
for i in range(n):
    s=s+int(input())
print(str(s)[:10])
