dct2={}
for i in dct:
	if not dct[i] in dct2:
		dct2[dct[i]]=i
	elif dct2[dct[i]]<i:
		dct2[dct[i]]=i
print(len(dct2))
x=input()
f=open("gen2.txt","a")
f.write(str(dct2))
f.close()