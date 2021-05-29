# N = 10**6+1
# fact = [[] for i in range(N)]
# for i in range(2, N):
#     for j in range(2*i,N,i):
#         fact[j].append(i)
# s = 0
# arr = []
# for t in range(N):
#     c = 0
#     if t&1 == 0:
#         for i in range(len(fact[t])//2):
#             if fact[t][i]&1 == fact[t][len(fact[t])-i-1]&1:
#                 c += 1
#                 if c>10:
#                     break
#         if c < 11 and c>0:
#             s += 1
#     arr.append(s)
# print("done")
# for xyz in range(int(input())):
#     print(arr[int(input())])


## Python 2 worked #############
N = 10**6+1
arr = [0]*N
tot = [0]*N
for i in range(2,1000,2):
    j = 2
    p = i*(i+j)
    while p<N:
        tot[p] += 1
        j += 2
        p = i*(i+j)
for i in range(1,N):
    if 0<tot[i]<11:
        arr[i] = arr[i-1] + 1
    else:
        arr[i] = arr[i-1]
t = int(input())
for xyz in range(t):
    print(arr[int(input())])
################################

# print(arr2[100])
# print(arr2==arr)