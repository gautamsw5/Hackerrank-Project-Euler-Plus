# # from collections import defaultdict
# # n,m = map(int, input().split())
# # arr = list(map(int, input().split()))
# # count = defaultdict(int)

# # ans = 0
# # for i in count:
# #     if count==1:
# #         ans += i
# # print(ans)
# from collections import defaultdict
# import itertools
# ##n,M = map(int, input().split())
# ##arr = list(map(int, input().split()))
# n, m = 6, 3
# arr = [1, 3, 6, 8, 10, 11]
# freq = {}
# freq[0] = {}
# freq[0][0] = 1
# subsets = defaultdict()
# subsets[1] = list()
# for i in sorted(arr, reverse = True):
#     for m in sorted(subsets, reverse = True):
#         for x in sorted(subsets[m], key = lambda x : sum(x)):
#             if not m+1 in subsets:
#                 subsets[m+1] = list()
#             subsets[m+1].append(x+[i])
#     subsets[1].append([i])
#     for m in sorted(freq, reverse = True):
#         for x in sorted(freq[m], reverse = True):
#             # print(i,m,x)
#             if not m+1 in freq:
#                 freq[m+1] = {}
#             if not x+i in freq[m+1]:
#                 freq[m+1][x+i] = freq[m][x]
#             else:
#                 freq[m+1][x+i] += freq[m][x]
# for m in range(1,n+1):
#     freqq = {}
#     for i in itertools.combinations(arr, m):
#         if not sum(i) in freqq:
#             freqq[sum(i)] = 1
#         else:
#             freqq[sum(i)] += 1
#     print(m,freqq)
#     print(m,freq[m])
#     print(freqq==freq[m])
# # ans = 0
# # for i in freq[m]:
# #     if freq[m][i]==1:
# #         ans += i
# # print(freq[m])
# # print(ans)
from collections import defaultdict
n,M = map(int, input().split())
arr = list(map(int, input().split()))
freq = defaultdict(dict)
freq[0][0] = 1
for i in sorted(arr, reverse = True):
    for m in sorted(freq, reverse = True):
        for x in sorted(freq[m], reverse = True):
            if not m+1 in freq:
                freq[m+1] = {}
            if not x+i in freq[m+1]:
                freq[m+1][x+i] = freq[m][x]
            else:
                freq[m+1][x+i] += freq[m][x]
ans = 0
for i in freq[M]:
    if freq[M][i]==1:
        ans += i
print(ans)