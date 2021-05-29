# Enter your code here. Read input from STDIN. Print output to STDOUT
def sumoff(n):
    if n==1 or n==0:
        return 0
    i=2
    s=1
    while i*i<n:
        if n%i==0:
            s=s+i+n//i
        i=i+1
    if i*i==n:
        s=s+i
    return s
arr=[]
i=1
while i<28123:
    if i<sumoff(i):
        arr.append(i)
    i=i+1
st=set(arr)
s=0
for n in range(1,28123):
    s=s+n
    for i in arr:
        if n-i in st:
            s=s-n
            break
print(s)
