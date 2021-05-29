c=0
fact=[1,1]
for i in range(2,101):
    fact.append(i*fact[-1])
for n in range(1,101):
    for r in range(n):
        if fact[n]/(fact[r]*fact[n-r])>10**6:
            c=c+1
print(c)
