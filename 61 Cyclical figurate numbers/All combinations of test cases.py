import itertools
beginmas=[set() for i in range(100)]
endmas=[set() for i in range(100)]
masterset=[set() for i in range(6)]
def get(n):
    ret=set()
    if n in masterset[0]:
        ret.add(0)
    if n in masterset[1]:
        ret.add(1)
    if n in masterset[2]:
        ret.add(2)
    if n in masterset[3]:
        ret.add(3)
    if n in masterset[4]:
        ret.add(4)
    if n in masterset[5]:
        ret.add(5)
    return ret
def triangle(n):
    return (n*(n+1))//2
def square(n):
    return n*n
def pentagon(n):
    return (n*(3*n-1))//2
def hexagon(n):
    return n*(2*n-1)
def heptagon(n):
    return (n*(5*n-3))//2
def octagon(n):
    return n*(3*n-2)
def check6(arr,comp):
    for a in arr[0]:
        for b in arr[1]:
            for c in arr[2]:
                for d in arr[3]:
                    for e in arr[4]:
                        for f in arr[5]:
                            s=set()
                            s.add(a)
                            s.add(b)
                            s.add(c)
                            s.add(d)
                            s.add(e)
                            s.add(f)
                            if s.intersection(comp)==comp:
                                return True
    return False
def check5(arr,comp):
    for a in arr[0]:
        for b in arr[1]:
            for c in arr[2]:
                for d in arr[3]:
                    for e in arr[4]:
                        s=set()
                        s.add(a)
                        s.add(b)
                        s.add(c)
                        s.add(d)
                        s.add(e)
                        if s.intersection(comp)==comp:
                            return True
    return False
def check4(arr,comp):
    for a in arr[0]:
        for b in arr[1]:
            for c in arr[2]:
                for d in arr[3]:
                    s=set()
                    s.add(a)
                    s.add(b)
                    s.add(c)
                    s.add(d)
                    if s.intersection(comp)==comp:
                        return True
    return False
def check3(arr,comp):
    for a in arr[0]:
        for b in arr[1]:
            for c in arr[2]:
                s=set()
                s.add(a)
                s.add(b)
                s.add(c)
                if s.intersection(comp)==comp:
                    return True
    return False
def check2(arr,comp):
    for a in arr[0]:
        for b in arr[1]:
            s=set()
            s.add(a)
            s.add(b)
            if s.intersection(comp)==comp:
                return True
    return False
def check1(arr,comp):
    for a in arr[0]:
        s=set()
        s.add(a)
        if s.intersection(comp)==comp:
            return True
    return False
def f5(comp,xvc):
    ansset=set()
    for start in masterset[xvc]:
        for sec in beginmas[start%100]:
            if start!=sec:
                for thir in beginmas[sec%100]:
                    if thir!=start and thir!=sec:
                        for forth in beginmas[thir%100]:
                            if forth!=thir and forth!=start and forth!=sec:
                                for fifth in beginmas[forth%100].intersection(endmas[start//100]):
                                    if fifth!=thir and fifth!=start and fifth!=sec and fifth!=forth:
                                        if check5([get(start),get(sec),get(thir),get(forth),get(fifth)],comp):
                                            ansset.add(tuple(sorted([start,sec,thir,forth,fifth])))
    return ansset
def f4(comp,xvc):
    ansset=set()
    for start in masterset[xvc]:
        for sec in beginmas[start%100]:
            if start!=sec:
                for thir in beginmas[sec%100]:
                    if thir!=start and thir!=sec:
                        for forth in beginmas[thir%100].intersection(endmas[start//100]):
                            if forth!=thir and forth!=start and forth!=sec:
                                if check4([get(start),get(sec),get(thir),get(forth)],comp):
                                            ansset.add(tuple(sorted([start,sec,thir,forth])))
    return ansset
def f3(comp,xvc):
    ansset=set()
    for start in masterset[xvc]:
        for sec in beginmas[start%100]:
            if start!=sec:
                for thir in beginmas[sec%100].intersection(endmas[start//100]):
                    if thir!=start and thir!=sec:
                        if check3([get(start),get(sec),get(thir)],comp):
                                            ansset.add(tuple(sorted([start,sec,thir])))
    return ansset
def f2(comp,xvc):
    ansset=set()
    for start in masterset[xvc]:
        for sec in beginmas[start%100].intersection(endmas[start//100]):
            if start!=sec:
                if check2([get(start),get(sec)],comp):
                    ansset.add(tuple(sorted([start,sec])))
    return ansset
def f1(comp,xvc):
    ansset=set()
    for start in masterset[xvc]:
        if check1([get(start)],comp) and start//100==start%100:
                    ansset.add(tuple(sorted([start])))
    return ansset
i=1
t=triangle(0)
s=square(0)
p=pentagon(0)
h=hexagon(0)
H=heptagon(0)
o=octagon(0)
while min([t,s,p,h,H,o])<10**4:
    t=triangle(i)
    s=square(i)
    p=pentagon(i)
    h=hexagon(i)
    H=heptagon(i)
    o=octagon(i)
    c=0
    for x in [t,s,p,h,H,o]:
        if x>999 and x<10**4:
            beginmas[x//100].add(x)
            endmas[x%100].add(x)
            masterset[c].add(x)
        c=c+1
    i=i+1
def solve(l):
    comp=set()
    for i in l:
        comp.add(i-3)
    if len(comp)==6:
        print(28684)
    else:
        anset=[]
        if len(comp)==1:
            anset=f1(comp,max(comp))
        elif len(comp)==2:
            anset=f2(comp,max(comp))
        elif len(comp)==3:
            anset=f3(comp,max(comp))
        elif len(comp)==4:
            anset=f4(comp,max(comp))
        elif len(comp)==5:
            anset=f5(comp,max(comp))
        ans=[]
        for i in anset:
            ans.append(sum(i))
        ans.sort()
        for i in ans:
            print(i)
c=0
lst=[3,4,5,6,7,8]
for k in range(1,7):
    for comb in itertools.combinations(lst,k):
        print(comb)
        solve(list(comb))
        c=c+1
print(c)
