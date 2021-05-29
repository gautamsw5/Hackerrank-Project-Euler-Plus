from collections import defaultdict
dct = defaultdict(set)
dct2 = defaultdict(set)
i = 1
while i*i < 10**13:
    s = ''.join(x for x in sorted(str(i*i)))
    dct[s].add(i*i)
    if len(dct[s]) > len(dct2[len(s)]) or (len(dct[s]) == len(dct2[len(s)]) and max(dct[s]) > max(dct2[len(s)])):
        dct2[len(s)] = dct[s]
    i += 1
dct3 = {}
for i in dct2:
    dct3[i] = max(dct2[i])
print(dct3)