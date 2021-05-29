import itertools
while True:
    n=int(input())
    print(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9,10,11,12]))[n-1])
