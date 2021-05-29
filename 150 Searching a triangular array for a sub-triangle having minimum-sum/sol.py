import heapq
pq = []
heapq.heapify(pq)
n,k = map(int, input().split())
arr = []
dp = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    tmp = [0]
    for j in range(len(arr[i])):
        tmp.append(tmp[-1]+arr[i][j])
    dp.append(tmp)
for i in range(n):
    for j in range(0, len(arr[i])):
        s = 0
        for h in range(1,n-i+1):
            s += dp[i+h-1][j+h]-dp[i+h-1][j]
            heapq.heappush(pq,s)
for i in range(k):
    print(heapq.heappop(pq))
