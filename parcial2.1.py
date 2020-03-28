from random import*
n=int(input("Ingrese cantidad de columnas: "))
while n>100 or n<1:
	n=int(input("La cantidad de columnas debe estar entre 1 y 100. Intente de nuevo: "))
m=int(input("Ingrese cantidad de filas: "))
while m>100 or m<1:
	m=int(input("La cantidad de filas debe estar entre 1 y 100. Intente de nuevo: "))


lista=[]
listamax=[]
for i in range (0,m):
	listafil=[]
	for j in range (0,n):
		listafil+=[randint(0,1000)]
	lista+=[listafil]

	maxfila=listafil[0]
	for h in range (1,len(listafil)):
		if listafil[h]>maxfila:
			maxfila=listafil[h]
	listamax+=[maxfila]
for i in range (0,m):
	for j in range (0,n):
		print (lista[i][j],end=" ")
	print()
suma=0
listaimp=[]
for i in range (0,len(listamax)):
	if i%2==1:
		listaimp+=[listamax[i]]
		if listamax[i]%2==1:
			suma+=listamax[i]

print ("Los máximos de las filas impares son: ",listaimp)

print ("La suma de los máximos impares de las filas impares es: ",suma)
