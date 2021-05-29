import itertools
ans=0
arr=[]
for i in itertools.permutations([0,1,2,3,4,5,6]):
    if (i[2]*100+i[3]*10+i[4])%3==0 and i[3]%2==0 and i[5]%5==0 and (i[4]*100+i[5]*10+i[6])%7==0:
        arr.append(i)
for a in arr:
    s=0
    for i in a:
        s=s*10+i
    ans+=s
print(s)
