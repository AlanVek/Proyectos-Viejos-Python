apel=[]
nota=[]

for i in range (0,3):
	ap=input("Ingrese apellido: ")
	n=int(input("Ingrese nota: "))
	
	while n>10 or n<1:
		n=int(input("La nota debe estar entre 1 y 10. Inténtelo de nuevo: "))

	apel+=[ap]
	nota+=[str(n)]
lista2=[]
lista3=[]
for i in range (0,3):
	apel[i]+="/"+nota[i]
for i in range (0,3):
	nota[i]+="/"+apel[i]

for i in range (0,3):
	a=max(apel)
	apel.remove(a)
	lista2+=[a]
for i in range (0,3):
	b=max(nota)
	nota.remove(b)
	lista3+=[b]

print (lista2)
print (lista3)