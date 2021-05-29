# Enter your code here. Read input from STDIN. Print output to STDOUT
brr=[0]*33600
i=1
y=1900
x=1900
z=0
months=[31,28,31,30,31,30,31,31,30,31,30,31]
for xyz in range(0,2800):
    for j in range(0,12):
        if i==0:
            brr[z]=brr[z-1]+1
        else:
            brr[z]=brr[z-1]
        i=(i+months[j])%7
        if ((y%4==0 and y%100!=0) or y%400==0) and j==1:
            i=(i+1)%7
        z=z+1
    y+=1
t=int(input())
for xyz in range(t):
    y1,m1,d1=map(int,input().split())
    y2,m2,d2=map(int,input().split())
    if d1>1:
        if m1==12:
            m1=1
            y1=y1+1
        else:
            m1=m1+1
    if d2>1:
        if m2==12:
            m2=1
            y2=y2+1
        else:
            m2=m2+1
    if 1==2:#y1-1900<2800 and y2-1900<2800:
        ans = abs(brr[(y1-1900)*12+(m1-1)]-brr[(y2-1900)*12+(m2-1)])
        print(ans)
    else:
        x=((y1-1900)*12+(m1-1))//2800
        y=((y1-1900)*12+(m1-1))%2800
        ans = brr[len(brr)-1]*x+brr[y]
        #print(ans)
        x=((y2-1900)*12+(m2-1))//2800
        y=((y2-1900)*12+(m2-1))%2800
        #ans = abs(ans -brr[len(brr)-1]*x+brr[y])
        ans2 = brr[len(brr)-1]*x+brr[y]
        print(abs(ans-ans2))
