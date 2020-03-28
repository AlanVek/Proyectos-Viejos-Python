lista1=[""]

h=int(input("Ingrese la cantidad de miembros de la lista: "))
i=0
while i<h:
	lista1.append(int(input("Ingresa número entero para la lista: ")))
	i=i+1

for q in range(1,h+1):
	print("*"*int(lista1[q]))
	
	