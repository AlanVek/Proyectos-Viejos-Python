a=input("Ingrese lista de palabras, separadas por comas: ")

lista=a.split(",")

for i in range (0,len(lista)-1):
	for j in range (i+1,len(lista)):
		if lista[j]<lista[i]:
			aux=lista[i]
			lista[i]=lista[j]
			lista[j]=aux

print (lista[0],lista[len(lista)-1])

