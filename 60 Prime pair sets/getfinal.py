ans3=[]
t=[]
f="op3.txt"
x=open(f,"r")
for line in x:
    arr=list(map(int,line.split()))
    ans3.append(arr)
    '''if max(arr) in t:
        ans3[t.index(max(arr))][1].append(sum(arr))
    else:
        ans3.append([max(arr),[sum(arr)]])
        t.append(max(arr))
for i in range(len(ans3)):
    if len(ans3[i][1])==1:
        ans3[i][1]=ans3[i][1][0]'''
x.close()
print(str(ans3).replace(" ",""))
