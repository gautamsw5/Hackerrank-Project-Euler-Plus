primes = [True]*1000001
primes[0]=False
primes[1]=False
p=set()
arr=[2]
for i in range(2,1000001):
    if primes[i]:
        arr.append(i)
        for k in range(2*i,1000001,i):
            primes[k]=False
print(primes[17])
s=0
#543 is longest chain length for this question
k=int(input("Enter: "))
for i in range(k):
    s=s+arr[i]
if s in p:
    print(s)
i=k
while i<len(arr):
    s=s+arr[i]-arr[i-k]
    if s in p:
        print(s)
    i+=1
