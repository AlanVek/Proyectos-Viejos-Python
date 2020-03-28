def sumamat(a,b):
	matriz=[]
	for i in range (0,len(a)):
		lista=[]
		for j in range (0,len(a[0])):
			lista+=[a[i][j]+b[j][i]]
		matriz+=[lista]
	return (matriz)
def mostrarmatriz(a):
	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			print (a[i][j],end=" ")
		print()

A=[[1,0,0],[0,1,0],[0,0,1]]
B=[[1,2,3],[4,5,6],[7,8,9]]

mostrarmatriz(A)
print()
mostrarmatriz(B)
print()
mostrarmatriz(sumamat(A,B))