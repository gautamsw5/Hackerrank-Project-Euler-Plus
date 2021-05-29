def sodk(n,k):
    s=0
    while n>0:
        s=s+(n%10)**k
        n=n//10
    return s
ans3=0
ans4=0
ans5=0
ans6=0
for i in range(10,10**6):
    if i==sodk(i,3):
        ans3+=i
    if i==sodk(i,4):
        ans4+=i
    if i==sodk(i,5):
        ans5+=i
    if i==sodk(i,6):
        ans6+=i
print(ans3,ans4,ans5,ans6)
'''
ans=[1301,19316,443839,548834]
n=int(input())
print(ans[n-3])
'''
