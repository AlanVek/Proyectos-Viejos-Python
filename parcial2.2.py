from random import*

m=int(input("Ingrese cantidad de filas de la primera: "))
n=int(input("Ingrese cantidad de columnas de la primera: "))
p=int(input("Ingrese cantidad de columnas de la segunda: "))
mat1=[]
mat2=[]

def hacermatriz(m,n):
	mat=[]
	for i in range (0,m):
		lista1=[]
		for j in range (0,n):
			lista1+=[randint(0,10)]
		mat+=[lista1]
	return(mat)
mat1=hacermatriz(m,n)
mat2=hacermatriz(n,p)

mat3=[]
def printmatriz(a):
	for i in range (0,len(a)):
		for j in range (0,len(a[i])):
			print (a[i][j],end=" ")
		print()


print ("La primera matriz es: ")
printmatriz(mat1)

print ("La segunda matriz es: ")
printmatriz(mat2)

def multmatriz(a,b):
	mat=[]
	for i in range(0,len(a)):
		lista1=[]
		for t in range (0,len(b[i])):
			suma=0
			for j in range (0,len(b)):
				suma+=a[i][j]*b[j][t]
			lista1+=[suma]
		mat+=[lista1]
	return(mat)

print ("La matriz resultante es: ")
mat3=multmatriz(mat1,mat2)
printmatriz(mat3)


