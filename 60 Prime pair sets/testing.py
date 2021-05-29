import time
tx=time.time()
with open("test.txt","a") as f:
    for i in range(100):
        for j in range(100):
            for k in range(100):
                f.write(str(i)+" "+str(i+1)+"\n")
print(time.time()-tx)
x=input("Done")
