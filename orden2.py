lista=[3,5,7,6,8,9]

for i in range (0,len(lista)-1):
	for j in range (i+1,len(lista)):
		if lista[i]>lista[j]:
			aux=lista[i]
			lista[i]=lista[j]
			lista[j]=aux
print (lista)