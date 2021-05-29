import heapq
import math
n=int(input())
pq=[]
heapq.heapify(pq)
for i in range(n):
    a,b=map(int,input().split())
    heapq.heappush(pq,[b*math.log(a),a,b])
k=int(input())
ans=[0,0,0]
for i in range(k):
    ans=heapq.heappop(pq)
print(str(ans[1])+" "+str(ans[2]))
