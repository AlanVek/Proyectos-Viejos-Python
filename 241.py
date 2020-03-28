def difmat(a,b):
	mat=[]
	
	for i in range (0,len(a)):
		lista=[]
		for j in range (0,len(a[i])):
			lista+=[a[i][j]-b[i][j]]
		
		mat+=[lista]

	print (mat)


difmat([[1,2,3],[4,5,6]],[[0,0,3],[0,0,6]])