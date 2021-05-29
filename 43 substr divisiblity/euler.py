ans=0
for last in range(102,1000,17):
    d=[-1]*10
    d[9]=last%10
    d[8]=(last%100)//10
    d[7]=(last%1000)//100
    if d[9]!=d[8] and d[9]!=d[7] and d[7]!=d[8]:
        for x in range(0,10):
            if not x in d[7:] and (x*100+d[7]*10+d[8])%13==0:
                d[6]=x
                for y in range(0,10):
                    if not y in d[6:] and (y*100+d[6]*10+d[7])%11==0:
                        d[5]=y
                        for z in range(0,10):
                            if not z in d[5:] and (z*100+d[5]*10+d[6])%7==0:
                                d[4]=z
                                for a in range(0,10):
                                    if not a in d[4:] and (a*100+d[4]*10+d[5])%5==0:
                                        d[3]=a
                                        for b in range(0,10):
                                            if not b in d[3:] and (b*100+d[3]*10+d[4])%3==0:
                                                d[2]=b
                                                for c in range(0,10):
                                                    if not c in d[2:] and (c*100+d[2]*10+d[3])%2==0:
                                                        d[1]=c
                                                        d[0]=45-sum(d[1:])
                                                        s=""
                                                        for i in d:
                                                            s=s+str(i)
                                                        ans+=int(s)
                                                        print(s)
print(ans)
