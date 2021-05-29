n=int(input())
arr=list(map(int,input().split()))
i=0
# aloowed Chars
alw=['0','1','2','3','4','5','6','7','8','9',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',";",":",",",".","'","?","-","!","(",")"]
'''
Sample Input:
82
32 66 50 20 11 0 42 66 33 19 13 20 47 66 37 14 58 67 43 23 14 17 49 67 46 20 6 51 66 55 9 39 67 45 3 25 56 66 39 14 37 34 65 51 22 8 1 40 65 32 17 14 21 45 65 36 12 57 66 41 20 15 19 50 66 44 23 7 49 65 54 11 36 66 47 0 24 58 65 38 12 38
Sample output:
abc
'''
for a in range(ord("a"),ord("z")+1):
    s=["" for i in range(len(arr))]
    f=0
    for i in range(0,len(arr),3):
        if not str(chr(arr[i]^a)) in alw:
            f=1
            break
        s[i]=str(chr(arr[i]^a))
    if f==1:
        continue
    for b in range(ord("a"),ord("z")+1):
        f=0
        for i in range(1,len(arr),3):
            if not str(chr(arr[i]^b)) in alw:
                f=1
                break
            s[i]=str(chr(arr[i]^b))
        if f==1:
            continue
        for c in range(ord("a"),ord("z")+1):
            f=0
            for i in range(2,len(arr),3):
                if not str(chr(arr[i]^c)) in alw:
                    f=1
                    break
                s[i]=str(chr(arr[i]^c))
            if f==0:
                print(chr(a)+chr(b)+chr(c))
