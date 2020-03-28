def superposicion(x,y):
	for i in x:
		for p in y:
			if i==p:
				print ("Comparten el miembro: ",i) 



l=int(input("Ingrese cantidad de miembros de la lista 1: "))

lista1=[""]
t=0
while t<l:
	lista1.append(input("Ingrese miembro a agregar: "))
	t=t+1

f=int(input("Ingrese cantidad de miembros de la lista 2: "))

lista2=[""]
h=0
while h<f:
	lista2.append(input("Ingrese miembro a agregar: "))
	h=h+1

superposicion(lista1,lista2)



