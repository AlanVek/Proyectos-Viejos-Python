from random import*

n=int(input("Ingrese número de columnas: "))
m=int(input("Ingrese número de filas: "))


lista=[]

for i in range (0,m):
	lista1=[]
	for j in range (0,n):
		lista1+=[randint(0,1000)]
	lista+=[lista1]

listamax=[]

for i in range (0,m):
	if i%2==1:
		a=lista[i][0]
		for j in range (1,n):
			if lista[i][j]>a:
				a=lista[i][j]
		listamax+=[a]

sumamax=0
for i in range (0,len(listamax)):
	if listamax[i]%2==1:
		sumamax+=listamax[i]
print ("La matriz resultante es: ")

for i in range (0,m):
	for j in range (0,n):
		print (lista[i][j],end=" ")
	print()

print ("Los máximos de las filas impares son: ", listamax)
print ("La suma de los máximos impares de las filas impares es: ",sumamax)