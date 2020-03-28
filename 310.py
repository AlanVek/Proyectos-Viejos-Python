def intersec(a,b):
	lista=[]
	p=""
	for i in range (0,len(a)):
		for j in range (0,len(b)):
			if a[i]==b[j] and not p.find(str(b[j]))>=0:
				p+=str(b[j])
				lista+=[b[j]]
	print (lista)

intersec([3,4,5,2,2,1,3],[6,2,3,3,1])

intersec([5,6,3,2,6,6,6,6],[6])