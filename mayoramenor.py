n=int(input("Ingrese cantidad de números: "))
while n<=0:
	n=int(input("No ha ingresado un valor correcto. Inténtelo de nuevo: "))

lista=[int(input("Ingrese número: "))]

for i in range (0,n-1):
	lista2=[int(input("Ingrese número: "))]
	lista+=lista2
	

for i in range (0,n):
	b=max(lista)
	print(b)
	lista.remove(b)



