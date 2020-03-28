from random import*
def crearmatriz(n):
	matriz=[]
	for i in range (0,n):
		lista=[]
		for j in range (0,n):
			a=randint(0,10)
			while a%2!=0:
				a=randint(0,10)
			lista+=[a]
		matriz+=[lista]

	return (matriz)

def mostrarmatriz(a):
	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			print (a[i][j],end=" ")
		print()

def numtriangsup(a):
	lista=[]
	for i in range (0,n-1):
		for j in range (i+1,n):
			lista+=[a[i][j]]
	return(lista)
def diagon(a):
	diagonal=True

	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			if j!=i and a[i][j]!=0:
				diagonal=False
				break
	if diagonal:
		return (True)
	else:
		return (False)
n=int(input("Ingrese dimensión de la matriz: "))
while n<2 or n>10:
	n=int(input("El número debe estar entre 2 y 10. Inténtelo de nuevo: "))


matriz=crearmatriz(n)

print ("La matriz resultante es: ")
mostrarmatriz(matriz)

print ("La lista de números en la triangular superior es: ", numtriangsup(matriz))

diag=diagon(matriz)

if diag:
	print ("La matriz es diagonal.")
else:
	print ("La matriz no es diagonal.")