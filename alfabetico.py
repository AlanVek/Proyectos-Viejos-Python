n=int(input("Ingrese cantidad de letras: "))
while n<=0:
	n=int(input("No ha ingresado un valor correcto. Inténtelo de nuevo: "))

lista=[input("Ingrese letra: ")]
for i in range (0,n-1):
	lista.append(input("Ingrese letra: "))

	

for i in range (0,n):
	b=min(lista)
	print(b)
	lista.remove(b)



