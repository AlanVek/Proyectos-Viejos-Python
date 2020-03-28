lista=[3,5,7,6,8,9]

lista2=[]
for i in range (0,len(lista)):
	a=min(lista)
	lista.remove(a)
	lista2+=[a]

print (lista2)