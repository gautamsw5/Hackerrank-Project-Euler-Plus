import heapq
n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))
dist = [[None for i in range(n)]for j in range(n)]
visited = [[False for i in range(n)]for j in range(n)]
dist[0][0]=grid[0][0]
pq=[]
heapq.heapify(pq)
heapq.heappush(pq,[grid[0][0],0,0])
#heapq.heappop(pq)
c=0
while c<n*n:
    q = heapq.heappop(pq)
    i=q[1]
    j=q[2]
    if not visited[i][j]:
        c=c+1
        #print(dist[n-1][n-1],c)
    visited[i][j]=True
    if i>0 and not visited[i-1][j]:
        if dist[i-1][j]==None or dist[i-1][j]>dist[i][j]+grid[i-1][j]:
            dist[i-1][j] = dist[i][j]+grid[i-1][j]
            heapq.heappush(pq,[dist[i-1][j],i-1,j])
    if j>0 and not visited[i][j-1]:
        if dist[i][j-1]==None or dist[i][j-1]>dist[i][j]+grid[i][j-1]:
            dist[i][j-1] = dist[i][j]+grid[i][j-1]
            heapq.heappush(pq,[dist[i][j-1],i,j-1])
    if i<n-1 and not visited[i+1][j]:
        if dist[i+1][j]==None or dist[i+1][j]>dist[i][j]+grid[i+1][j]:
            dist[i+1][j] = dist[i][j]+grid[i+1][j]
            heapq.heappush(pq,[dist[i+1][j],i+1,j])
    if j<n-1 and not visited[i][j+1]:
        if dist[i][j+1]==None or dist[i][j+1]>dist[i][j]+grid[i][j+1]:
            dist[i][j+1] = dist[i][j]+grid[i][j+1]
            heapq.heappush(pq,[dist[i][j+1],i,j+1])
print(dist[n-1][n-1])
