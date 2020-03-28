def multmat(a,b):
	for i in range (0,len(a)):
		for j in range (0,len(a[i])):
			a[i][j]=b*a[i][j]

	print (a)

multmat([[1,2,3],[4,5,6]],3)