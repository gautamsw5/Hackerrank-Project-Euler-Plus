# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def match(x,y):
    for i in range(0,len(x)):
        if x[i]!=y[2*i]:
            return False
    return True
n=int(input())
x=list(map(str,input().split()))
low=""
high=""
for i in x:
    low=low+i+"0"
    high=high+i+"9"
low=low[:-1]
high=high[:-1]
low = int(math.sqrt(int(low))-1)
high = int(math.sqrt(int(high))+2)
if x[-1]=="0":
    low=low-low%10
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            break
elif x[-1]=="5":
    low=low-low%10+5
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            break
elif x[-1]=="1":
    low=low-low%10+1
    f=True
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            f=False
            break
    if f:
        low=low-low%10+9
        for i in range(low,high,10):
            if match(x,str(i*i)):
                print(i)
                break
elif x[-1]=="4":
    low=low-low%10+2
    f=True
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            f=False
            break
    if f:
        low=low-low%10+8
        for i in range(low,high,10):
            if match(x,str(i*i)):
                print(i)
                break
elif x[-1]=="9":
    low=low-low%10+3
    f=True
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            f=False
            break
    if f:
        low=low-low%10+7
        for i in range(low,high,10):
            if match(x,str(i*i)):
                print(i)
                break
elif x[-1]=="6":
    #print("here")
    low=low-low%10+4
    f=True
    for i in range(low,high,10):
        if match(x,str(i*i)):
            print(i)
            f=False
            break
    if f:
        low=low-low%10+6
        for i in range(low,high,10):
            if match(x,str(i*i)):
                print(i)
                break
