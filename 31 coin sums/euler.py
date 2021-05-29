ct=0
for h in range(2):
    for g in range(3):
        for f in range(5):
            for e in range(11):
                for d in range(21):
                    for c in range(41):
                        for b in range(101):
                            #x=2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h
                            #print(x)
                            if (2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h) <= 200:
                                ct=ct+1
print(ct)
