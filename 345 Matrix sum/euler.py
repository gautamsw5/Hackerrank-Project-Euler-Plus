n=int(input())
matrix = []
for i in range(n):
    l=list(map(int,input().split()))
    matrix.append(l)
'''def solve(s,summ,i):
    if len(s)==1:
        for j in s:
            summ.add((i,j))
            print(summ)
            summ.remove((i,j))
        return
    for j in s:
        s.remove(j)
        summ.add((i,j))
        solve(s,summ,i+1)
        summ.remove((i,j))
        s.add(j)'''
m=0
def solve(s,summ,i):
    global m
    if len(s)==1:
        for j in s:
            summ+=matrix[i][j]
            if summ>m:
                print(summ)
                m=summ
            summ-=matrix[i][j]
        return
    for j in s:
        s.remove(j)
        summ+=matrix[i][j]
        solve(s,summ,i+1)
        summ-=matrix[i][j]
        s.add(j)
solve({i for i in range(n)},0,0)
print("max sum is ",m)
x=input()
