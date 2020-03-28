apel=[]
nota=[]

for i in range (0,3):
	ap=input("Ingrese apellido: ")
	n=int(input("Ingrese nota: "))
	
	while n>10 or n<1:
		n=int(input("La nota debe estar entre 1 y 10. Inténtelo de nuevo: "))

	apel+=[ap]
	nota+=[n]
lista2=[]
lista3=[]
lista=[]
lista1=[]



for i in range (0,3):
	lista+=[[apel[i],nota[i]]]
for i in range (0,3):
	lista1+=[[nota[i],apel[i]]]

for i in range (0,3):
	c=min(lista)
	lista.remove(c)
	lista2+=[c]
	
for i in range (0,3):
	d=max(lista1)
	lista1.remove(d)
	lista3+=[d]

print (lista2)
print (lista3)