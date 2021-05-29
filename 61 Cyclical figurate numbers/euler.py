begin=[[set() for i in range(100)] for j in range(6)]
end=[[set() for i in range(100)] for j in range(6)]
beginmas=[set() for i in range(100)]
endmas=[set() for i in range(100)]
master={}
masterset=[set() for i in range(6)]
# Intersections (0,3) (1,2) (0,1,3) (1,4) (2,4)
setrep={(0,3),(1,2),(0,1,3),(1,4),(2,4)}
y={(0, 3): {9730, 1540, 1035, 2701, 6670, 4753, 5778, 4371, 1431, 3486, 5151, 2850, 4005, 6441, 1326, 3003, 5565, 8128, 8385, 7875, 8646, 3655, 6216, 7626, 8911, 4560, 7381, 4950, 3160, 4186, 9180, 2016, 2145, 1891, 7140, 2278, 1128, 1770, 5995, 5356, 9453, 2415, 3828, 1653, 6903, 3321, 2556}, (0,): {6786, 5253, 3081, 9870, 1176, 6555, 3741, 2080, 1953, 2211, 1830, 5671, 3240, 2346, 1711, 4656, 2485, 4278, 6328, 1081, 5050, 1596, 8256, 8001, 8515, 2628, 7750, 8778, 3403, 3916, 1485, 7503, 5460, 9045, 2775, 6105, 7260, 1378, 9316, 7021, 2926, 4465, 3570, 4851, 9591, 1275, 5886, 4095}, (0, 1, 3): {1225}, (1,): {1024, 2304, 3969, 4096, 1156, 3844, 4225, 4356, 6400, 3721, 4489, 8836, 9604, 1296, 1681, 1936, 2704, 3600, 4624, 5776, 7056, 7569, 3481, 4761, 2209, 6561, 9216, 1444, 3364, 4900, 8100, 2601, 3249, 5041, 2809, 1849, 7225, 1600, 1089, 3136, 5184, 2116, 2500, 6084, 6724, 7744, 8649, 9025, 3025, 5329, 1369, 8281, 8464, 2401, 6241, 1764, 2916, 5476, 7396, 2025, 6889, 9409, 1521, 7921, 5625}, (1, 4): {5929}, (1, 2): {9801}, (2,): {1926, 1162, 3725, 1426, 7315, 7957, 8855, 5017, 1820, 4510, 6305, 5922, 3876, 6700, 5551, 8626, 1717, 1335, 1080, 7740, 4030, 2752, 2625, 2882, 7107, 4676, 2501, 3015, 5192, 2380, 3151, 8400, 1617, 2262, 9560, 3290, 4187, 1247, 6112, 2147, 6501, 7526, 5735, 3432, 1001, 9322, 4845, 1520, 8177, 2035, 6902, 3577, 5370, 9087}, (2, 4): {4347}, (4,): {4995, 8323, 1288, 2059, 2839, 1177, 6682, 6426, 2205, 6943, 3744, 6175, 4774, 3367, 8614, 7209, 4141, 9517, 1071, 2356, 5688, 7480, 3010, 5452, 7756, 4558, 8910, 2512, 3553, 3940, 5221, 8037, 9828, 2673, 3186, 1651, 1525, 1782, 9211, 1404, 1918}, (5,): {1408, 1281, 3201, 8321, 1541, 2821, 4485, 1160, 6533, 8965, 1680, 1045, 3605, 7701, 4256, 2465, 6816, 1825, 9633, 2296, 1976, 3008, 4033, 7105, 8640, 3400, 8008, 2640, 9296, 2133, 5461, 5208, 5720, 4961, 5985, 3816, 7400, 4720, 6256, 9976}}

def find(n):
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
def get(x):
    return[x in masterset[i] for i in range(6)]
def check(arr):
    retarr=[False for i in range(6)]
    ret=True
    for i in range(6):
        for j in range(6):
            retarr[i]=retarr[i] or arr[j][i]
    for i in range(6):
        ret=ret and retarr[i]
    return ret
i=1
cmp=set()
cmp.add(0)
cmp.add(1)
cmp.add(2)
cmp.add(3)
cmp.add(4)
cmp.add(5)
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
            begin[c][x//100].add(x)
            end[c][x%100].add(x)
            beginmas[x//100].add(x)
            endmas[x%100].add(x)
            masterset[c].add(x)
            if x in master:
                tmp=list(master[x])
                tmp[c]=1
                master[x]=tuple(tmp)
            else:
                tmp=[0,0,0,0,0,0]
                tmp[c]=1
                master[x]=tuple(tmp)
        c=c+1
    i=i+1
ansset=set()
for start in masterset[0]:
    for sec in beginmas[start%100]:
        if start!=sec:
            for thir in beginmas[sec%100]:
                if thir!=start and thir!=sec:
                    for forth in beginmas[thir%100]:
                        if forth!=thir and forth!=start and forth!=sec:
                            for fifth in beginmas[forth%100]:
                                if fifth!=thir and fifth!=start and fifth!=sec and fifth!=forth:
                                    for sixth in beginmas[fifth%100].intersection(endmas[start//100]):
                                        if sixth!=thir and sixth!=start and sixth!=sec and sixth!=forth and sixth!=forth and sixth!=fifth:
                                            if check([get(start),get(sec),get(thir),get(forth),get(fifth),get(sixth)]) and start//100==sixth%100:
                                                print(start,sec,thir,forth,fifth,sixth)
                                                ansset.add(start+sec+thir+forth+fifth+sixth)
