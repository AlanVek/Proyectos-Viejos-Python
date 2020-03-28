def diagon(a):
	cua=True
	for t in range (0,len(a)):
		if len(a)!=len(a[t]):
			cua=False
			break

	if cua==False:
		print (None)

	else:
		suma=0
		for i in range (0,len(a)):
			suma+=a[i][i]


		print (suma)


diagon ([[1,2,3],[4,5,6],[7,8,9]])
