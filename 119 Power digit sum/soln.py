with open('tmp.txt','w'): pass
file = open('tmp.txt','w')
# b=int(input())
def sum_toB(n, b):
    ans = 0
    while n>0:
        ans += n%b
        n = n//b
    return ans
def solve(b):
    MAX = 10**100
    ans=[]
    for s in range(2, 30000):
        n = s
        while n<MAX:
            if s==sum_toB(n, b) and n>=b:
                ans.append(n)
            n = n*s
    ans.sort()
    # s=""
    # for i in ans:
    #     s+=str(i)+" "
    # print(s.strip())
    return ans
# file.write('[')
# for b in range(2, 1001):
#     # file.write('['+str(solve(b)).replace(" ","")+'],')
#     solve(b)
#     print(b)
# file.write(str(solve(2)))
file.write(str(solve(3)))
file.close()