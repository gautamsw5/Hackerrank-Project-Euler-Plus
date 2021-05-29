# Enter your code here. Read input from STDIN. Print output to STDOUT
ans=[12, 60, 120, 240, 420, 720, 840, 1680, 2520, 4620, 5040, 9240, 18480,
27720, 55440, 110880, 120120, 166320, 180180, 240240, 360360,  720720, 1081080,
1441440, 2042040, 2162160, 2882880, 3603600, 4084080]
brr=[1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 16, 20, 25, 31, 40, 46, 50, 51, 53, 64, 80, 104, 105, 124, 130, 135, 142, 158, 168]
t=int(input())
for xyz in range(t):
    n=int(input())
    if n<60:
        print(12)
    elif n>=4084080:
        print(4084080)
    else:
        l=0
        r=len(ans)-1
        while l<=r:
            m=l+(r-l)//2
            if ans[m]==n or (ans[m]<n and ans[m+1]>n):
                print(ans[m])
                break
            elif ans[m]>n:
                r=m-1
            else:
                l=m+1
