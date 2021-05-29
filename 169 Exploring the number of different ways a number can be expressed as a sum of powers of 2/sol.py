# cache = {}
# arr = [pow(2,x) for x in range(91)]
# def solve(n, i, path):
#     if n==0:
#         print(i,path)
#         return 1
#     if n<0:
#         return 0
#     if (n,i) in cache:
#         return cache[(n,i)]
#     ans = 0
#     for j in range(i, 91):
#         if n >= 2*arr[j]:
#             # print(n,i,path,"-> calls ->",n-2*arr[j], j+1, path+[arr[j], arr[j]])
#             ans += solve(n-2*arr[j], j+1, path+[arr[j], arr[j]])
#         if n >= arr[j]:
#             # print(n,i,path,"-> calls ->",n-arr[j], i+1, path+[arr[j]])
#             ans += solve(n-arr[j], j+1, path+[arr[j]])
#         if n < arr[j]:
#             break
#     cache[(n,i)] = ans
#     return ans
# n = int(input())
# print(solve(n, 0, []))

##  DP memo: ###################
cache = {}
arr = [pow(2,x) for x in range(91)]
def solve(n, i):
    if n==0:
        return 1
    if n<0:
        return 0
    if (n, i) in cache:
        return cache[(n,i)]
    ans = 0
    for j in range(i, 91):
        if n >= 2*arr[j]:
            ans += solve(n-2*arr[j], j+1)
        if n >= arr[j]:
            ans += solve(n-arr[j], j+1)
        if n < arr[j]:
            break
    cache[(n,i)] = ans
    return ans
# for n in range(100):
#     print(n,solve(n, 0))
################################

## Stern's Diatomic series: ###########
cache = {}
def solve(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in cache:
        return cache[n]
    if n%2==0:
        cache[n] = solve(n//2)
        return cache[n]
    else:
        cache[n] = solve((n-1)//2) + solve((n+1)//2)
        return cache[n]
n = int(input())
print(n+1)

#######################################