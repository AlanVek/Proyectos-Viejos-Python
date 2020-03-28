n=input("Ingrese valores separados con coma: ")

lista=n.split(",")

for i in range (0,len(lista)):
	lista[i]=int(lista[i])
	if lista[i]%2==0:
		lista[i]=""
for i in lista:
	if i=="":
		lista.remove(i)


print (lista)