mf=open("op3.txt","r")
with open("test.txt","a") as f:
    for line in mf:
        f.write("<p>"+line+"</p>")
