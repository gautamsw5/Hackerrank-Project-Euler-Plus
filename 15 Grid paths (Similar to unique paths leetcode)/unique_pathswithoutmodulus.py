mp=[[0 for i in range(502)]for j in range(502)]
def getu(m,n,mp):
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    c=0
    if(n>1):
        t=0
        if(mp[m-1][n-2]!=0):
            t=mp[m-1][n-2]
        else:
            t=getu(m,n-1,mp)
            mp[m-1][n-2]=t
        c+=t
    if(m>1):
        t=0
        if(mp[m-2][n-1]!=0):
            t=mp[m-2][n-1]
        else:
            t=getu(m-1,n,mp)
            mp[m-2][n-1]=t
        c+=t
    return c
getu(50,50,mp)
getu(100,100,mp)
getu(150,150,mp)
getu(250,250,mp)
getu(400,400,mp)
getu(502,502,mp)
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(mp[m][n])
