with open('tmp.txt','w'): pass
file = open('tmp.txt','w')
# x = 7
# dp = [None]*(10**x)
# arr = [0]
# for d in range(x):
#     c = 0
#     for i in range(10**d,10**(d+1)):
#         t = i
#         while i!=0:
#             if dp[i]!=None:
#                 c += dp[i]
#                 break
#             if i==89:
#                 dp[i] = 0
#                 break
#             if i==1:
#                 c += 1
#                 dp[i] = 1
#                 break
#             s = 0
#             while i>0:
#                 s += (i%10)**2
#                 i = i//10
#             i = s
#     arr.append(arr[-1]+c)
# print(arr)
arr = [0, 7, 80, 857, 8558, 85623, 856929, 8581146, 85744333, 854325192]