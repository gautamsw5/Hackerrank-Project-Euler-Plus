t=int(input())
for xyz in range(t):
	n=int(input())
	m=0
	o=0
	for x in dct:
		if x<=n and dct[x]>m:
			m=dct[x]
			o=x
	print(o,m)