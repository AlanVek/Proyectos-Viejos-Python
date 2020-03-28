def trisup(a):
	tri=True
	for i in range (0,len(a)):
		for j in range (0,i):
			if a[i][j]!=0:
				tri=False
				break
			
	if tri:
		print ("La matriz es diagonal superior.")
	else:
		print ("La matriz no es diagonal superior.")


trisup([[1,2,3],[4,5,6],[7,8,9]])
trisup([[1,2,3],[0,2,3],[0,0,5]])
trisup ([[0,0,0],[0,0,0],[0,0,0]])
trisup ([[1,1,1],[1,1,0],[1,0,0]])