# Enter your code here. Read input from STDIN. Print output to STDOUT
z=0
for n in range(1,25):
    c=0
    for i in range(1,10):
        x=i**n
        if x>=10**(n-1) and x<10**n:
            c=c+1
    print(n,c)
    z=z+c
print(z)
