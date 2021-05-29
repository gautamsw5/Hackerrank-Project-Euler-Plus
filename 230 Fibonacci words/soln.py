# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
for xyz in range(q):
    A,B,n=map(str,input().split())
    n=int(n)
    if n<len(A):
        print(A[n-1])
    elif n<len(B):
        print(B[n-len(A)-1])
    else:
        a=len(A)
        b=len(B)
        sa='A'
        sb='B'
        while a<n:
            a,b=b,a+b
            sa,sb=sb,sa+sb
            print(sa)
        x=''
        for i in sa:
            if i=='A' and n-len(A)>0:
                n=n-len(A)
            elif i=='B' and n-len(B)>0:
                n=n-len(B)
            else:
                x=i
                break
        print((A+B)[n])
