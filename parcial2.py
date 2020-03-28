from random import*

n=int(input("Ingrese cantidad de columnas de la primera: "))
m=int(input("Ingrese cantidad de filas de la primera: "))
p=int(input("Ingrese cantidad de columnas de la segunda: "))

def crearmat (a,b):
	lista=[]
	for i in range (0,a):
		lista1=[]
		for j in range (0,b):
			lista1+=[randint(0,1000)]
		lista+=[lista1]

	return (lista)

mata=crearmat(m,n)
matb=crearmat(n,p)

def mostrarmat (a):
	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			print (a[i][j],end=" ")
		print()

print ("La primera matriz es: ", mostrarmat(mata))
print ("La segunda matriz es: ", mostrarmat(matb))

matc=[]
lista1=[]
for i in range (0,m):
	lista1=[]
	for t in range (0,p):
		suma=0
		for j in range (0,n):
			suma+=mata[i][j]*matb[j][t]
		lista1+=[suma]
	matc+=[lista1]

print ("La multiplicación es: ")
print (mostrarmat(matc))

