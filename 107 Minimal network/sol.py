# Simple Greedy to add min weight edges that connect current graph to newer nodes
import heapq
n,m = map(int, input().split())
adj = [[] for i in range(n)]
vis = [False for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    adj[a-1].append([c, b-1])
    adj[b-1].append([c, a-1])
vis[0] = True
c = 1
pq = []
heapq.heapify(pq)
for i in adj[0]:
    heapq.heappush(pq, i)
edge_sum = 0
while c < n:
    ed = heapq.heappop(pq)
    if not vis[ed[1]]:
        edge_sum += ed[0]
        for i in adj[ed[1]]:
            heapq.heappush(pq, i)
        vis[ed[1]] = True
        c += 1
print(edge_sum)