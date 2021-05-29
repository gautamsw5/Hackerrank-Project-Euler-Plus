# Enter your code here. Read input from STDIN. Print output to STDOUT
# H C S D --> Types of cards
# 2 3 4 5 6 7 8 9 T J Q K A --> values
'''
\High Card: Highest value card.
\One Pair: Two cards of the same value.
\Two Pairs: Two different pairs.
\Three of a Kind: Three cards of the same value.
\Straight: All cards are consecutive values.
\Flush: All cards of the same suit.
\Full House: Three of a kind and a pair.
\Four of a Kind: Four cards of the same value.
\Straight Flush: All cards are consecutive values of same suit.
\Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''
values={"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":9,"Q":10,"K":11,"A":12}
values1={"A":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"J":10,"Q":11,"K":12}
v1=[0]*13
v2=[0]*13
def consec(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i-1]+1!=arr[i]:
            return False
    return True
def SF(p1,p2):
    # Straight Flush
    p1.sort()
    p2.sort()
    P1=0
    P2=0
    if consec([values[p1[i][:-1]] for i in range(len(p1))]) and p1[0][-1]==p1[1][-1] and p1[1][-1]==p1[2][-1] and p1[2][-1]==p1[3][-1] and p1[3][-1]==p1[4][-1]:
        P1=1
    if consec([values[p2[i][:-1]] for i in range(len(p2))]) and p2[0][-1]==p2[1][-1] and p2[1][-1]==p2[2][-1] and p2[2][-1]==p2[3][-1] and p2[3][-1]==p2[4][-1]:
        P2=1
    v1=[0]*13
    v2=[0]*13
    for i in p1:
        v1[values[i[:-1]]]+=1
    for i in p2:
        v2[values[i[:-1]]]+=1
    if p1[0][0]=="2" and p1[1][0]=="3" and p1[2][0]=="4" and p1[3][0]=="5" and p1[4][0]=="A" and p1[0][-1]==p1[1][-1] and p1[1][-1]==p1[2][-1] and p1[2][-1]==p1[3][-1] and p1[3][-1]==p1[4][-1]:
        P1=2
    if p2[0][0]=="2" and p2[1][0]=="3" and p2[2][0]=="4" and p2[3][0]=="5" and p2[4][0]=="A" and p1[0][-1]==p1[1][-1] and p1[1][-1]==p1[2][-1] and p1[2][-1]==p1[3][-1] and p1[3][-1]==p1[4][-1]:
        P2=2
    if P1==0 and P2==2:
        return "Player 2"
    if P1==2 and P2==0:
        return "Player 1"
    if P1==1 and P2==2:
        return "Player 2"
    if P1==2 and P2==1:
        return "Player 1"
    if P1==1 and P2==1:
        if v1[::-1]>v2[::-1]:
            return "Player 1"
        if v1[::-1]<v2[::-1]:
            return "Player 2"
        return FK(p1,p2)
    if P1==1 and P2==0:
        return "Player 1"
    if P1==0 and P2==1:
        return "Player 2"
    return FK(p1,p2)
def FK(p1,p2):
    # 4 of a kind
    P1=0
    P2=0
    v1=[0]*13
    v2=[0]*13
    pp1=-1
    pp2=-1
    for i in p1:
        v1[values[i[:-1]]]+=1
    for i in p2:
        v2[values[i[:-1]]]+=1
    for i in range(len(v1)):
        if v1[i]==4:
            P1=1
            pp1=i
            break
    for i in range(len(v2)):
        if v2[i]==4:
            P2=1
            pp2=i
            break
    if P1==0 and P2==0:
        return FH(p1,p2)
    if P1==1 and P2==0:
        return "Player 1"
    if P1==0 and P2==1:
        return "Player 2"
    if pp1>pp2:
        return "Player 1"
    if pp1<pp2:
        return "Player 2"
    return FH(p1,p2)
def FH(p1,p2):
    # Full House
    P1=0
    P2=0
    p13=-1
    p12=-1
    p23=-1
    p22=-1
    for i in range(len(v1)):
        if v1[i]==3:
            p13=i
            P1+=1
        elif v1[i]==2:
            p12=i
            P1+=1
    for i in range(len(v2)):
        if v2[i]==3:
            p23=i
            P2+=1
        elif v2[i]==2:
            p22=i
            P2+=1
    if P1==2 and P2<2:
        return "Player 1"
    if P1<2 and P2==2:
        return "Player 2"
    if P1<2 and P2<2:
        return F(p1,p2)
    if p13>p23:
        return "Player 1"
    if p23>p13:
        return "Player 2"
    if p12>p22:
        return "Player 1"
    if p22>p12:
        return "Player 2"
    return F(p1,p2)
def F(p1,p2):
    # Flush
    P1=0
    P2=0
    if p1[0][-1]==p1[1][-1] and p1[1][-1]==p1[2][-1] and p1[2][-1]==p1[3][-1] and p1[3][-1]==p1[4][-1]:
        P1=1
    if p2[0][-1]==p2[1][-1] and p2[1][-1]==p2[2][-1] and p2[2][-1]==p2[3][-1] and p2[3][-1]==p2[4][-1]:
        P2=1
    if P1==1 and P2==1:
        return S(p1,p2)
    if P1==1:
        return "Player 1"
    if P2==1:
        return "Player 2"
    return S(p1,p2)
def S(p1,p2):
    # Straight
    p1.sort()
    p2.sort()
    P1=0
    P2=0
    if consec([values[p1[i][:-1]] for i in range(len(p1))]):
        P1=1
    if consec([values[p2[i][:-1]] for i in range(len(p2))]):
        P2=1
    v1=[0]*13
    v2=[0]*13
    for i in p1:
        v1[values[i[:-1]]]+=1
    for i in p2:
        v2[values[i[:-1]]]+=1
    if p1[0][0]=="2" and p1[1][0]=="3" and p1[2][0]=="4" and p1[3][0]=="5" and p1[4][0]=="A":
        P1=2
    if p2[0][0]=="2" and p2[1][0]=="3" and p2[2][0]=="4" and p2[3][0]=="5" and p2[4][0]=="A":
        P2=2
    if P1==0 and P2==2:
        return "Player 2"
    if P1==2 and P2==0:
        return "Player 1"
    if P1==1 and P2==2:
        return "Player 1"
    if P1==2 and P2==1:
        return "Player 2"
    if P1==1 and P2==1:
        if v1[::-1]>v2[::-1]:
            return "Player 1"
        if v1[::-1]<v2[::-1]:
            return "Player 2"
        return TK(p1,p2)
    if P1==1 and P2==0:
        return "Player 1"
    if P1==0 and P2==1:
        return "Player 2"
    return TK(p1,p2)
def TK(p1,p2):
    # Three of a Kind
    P1=0
    P2=0
    pp1=-1
    pp2=-1
    for i in p1:
        v1[values[i[:-1]]]+=1
    for i in p2:
        v2[values[i[:-1]]]+=1
    for i in range(len(v1)):
        if v1[i]==3:
            P1=1
            pp1=i
            break
    for i in range(len(v2)):
        if v2[i]==3:
            P2=1
            pp2=i
            break
    if P1==0 and P2==0:
        return TP(p1,p2)
    if P1==1 and P2==0:
        return "Player 1"
    if P1==0 and P2==1:
        return "Player 2"
    if pp1>pp2:
        return "Player 1"
    if pp1<pp2:
        return "Player 2"
    return TP(p1,p2)
def TP(p1,p2):
    # Two pairs
    P1=0
    pp1=[]
    P2=0
    pp2=[]
    for i in range(len(v1)):
        if v1[i]==2:
            P1+=1
            pp1.append(i)
    for i in range(len(v2)):
        if v2[i]==2:
            P2+=1
            pp2.append(i)
    if P1<2 and P2<2:
        return OP(p1,p2)
    if P1==2 and P2==2:
        pp1.sort()
        pp2.sort()
        if pp1[1]>pp2[1]:
            return "Player 1"
        if pp2[1]>pp1[1]:
            return "Player 2"
        if pp1[0]>pp2[0]:
            return "Player 1"
        if pp2[0]>pp1[0]:
            return "Player 2"
        return OP(p1,p2)
    if P1==2:
        return "Player 1"
    if P2==2:
        return "Player 2"
    return OP(p1,p2)
def OP(p1,p2):
    # One Pair
    P1=0
    pp1=[]
    P2=0
    pp2=[]
    for i in range(len(v1)):
        if v1[i]==2:
            P1+=1
            pp1.append(i)
    for i in range(len(v2)):
        if v2[i]==2:
            P2+=1
            pp2.append(i)
    if P1==1 and P2==1:
        if pp1[0]==pp2[0]:
            return Hg(p1,p2)
        if pp1[0]<pp2[0]:
            return "Player 2"
        if pp2[0]<pp1[0]:
            return "Player 1"
    if P1==1:
        return "Player 1"
    if P2==1:
        return "Player 2"
    return Hg(p1,p2)
def Hg(p1,p2):
    # Highest
    if v1[::-1]>v2[::-1]:
        return "Player 1"
    return "Player 2"
count=0
t=int(input())
for xyz in range(t):
    p=list(map(str,input().split()))
    p1,p2=p[:5],p[5:]
    p1.sort()
    p2.sort()
    v1=[0]*13
    v2=[0]*13
    # Royal Flush
    if p1[0][0]=="A" and p1[1][0]=="J" and p1[2][0]=="K" and p1[3][0]=="Q" and p1[4][0]=="T" and p1[0][1]==p1[1][1] and p1[1][1]==p1[2][1] and p1[2][1]==p1[3][1] and p1[3][1]==p1[4][1]:
        print("Player 1")
        count+=1
        continue
    if p2[0][0]=="A" and p2[1][0]=="J" and p2[2][0]=="K" and p2[3][0]=="Q" and p2[4][0]=="T" and p2[0][1]==p2[1][1] and p2[1][1]==p2[2][1] and p2[2][1]==p2[3][1] and p2[3][1]==p2[4][1]:
        print("Player 2")
        continue
    # Straight Flush
    xxxx=SF(p1,p2)
    if xxxx=="Player 1":
        count+=1
    print(xxxx)
