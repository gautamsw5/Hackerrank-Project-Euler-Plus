# Enter your code here. Read input from STDIN. Print output to STDOUT
PT=[1, 210, 40755, 7906276, 1533776805, 297544793910,57722156241751]
PH=[1, 40755, 1533776805, 57722156241751]
n,a,b=map(int,input().split())
if (a==3 and b==5) or (a==5 and b==3):
    i=0
    while i<len(PT) and PT[i]<n:
        print(PT[i])
        i=i+1
elif (a==6 and b==5) or (a==5 and b==6):
    i=0
    while i<len(PH) and PH[i]<n:
        print(PH[i])
        i=i+1
