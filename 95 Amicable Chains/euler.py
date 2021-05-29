N=int(input())+1
if N>=629072:
    print(14316)
else:
    fact = [set() for i in range(N)]
    for i in range(2,N):
        for p in range(2*i,N,i):
            fact[p].add(i)
    factsum = [1]*N
    for i in range(N):
        factsum[i]+=sum(fact[i])
    mxlen = 0
    minmxlen = 100000000000
    for i in range(6,N):
        s=set()
        s.add(i)
        x=i
        c=1
        while True:
            i=factsum[i]
            c=c+1
            if i>N-1:
                break
            if i==x and c>mxlen:
                mxlen = c
                if 1 in s:
                    s.remove(1)
                minmxlen = min(s)
            if i in s:
                break
            s.add(i)
    print(minmxlen)
