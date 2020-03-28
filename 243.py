def traspuesta(a):
	lista=[]
	for j in range (0,len(a[0])):
		tra=[]
		for i in range (0,len(a)):
			tra+=[a[i][j]]
		lista+=[tra]


	print (lista)

traspuesta ([[1,2,3],[4,5,6],[7,8,9]])