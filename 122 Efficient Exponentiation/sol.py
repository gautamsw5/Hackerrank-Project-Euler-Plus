with open('tmp.txt','w'): pass
file = open('tmp.txt','w')
arr = [None for i in range(276)]
vis = [False for i in range(276)]
n = 1
s = set([1])
que = [n]
q = [s]
# Similar to dijkstra without pq
while len(que)>0:
    cur = que.pop(0)
    st = q.pop(0)
    if arr[cur]==None or len(arr[cur]) > len(st):
        arr[cur] = st
    for i in list(st):
        if i+cur < 276 and not vis[i+cur]:
            que.append(i+cur)
            q.append(list(st)+[i+cur])
    vis[cur] = True
file.write(str(arr))