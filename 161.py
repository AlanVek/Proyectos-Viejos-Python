cadena=input("Ingrese cadena de palabras: ")
n=int(input("Ingrese número entero: "))

suma=1
p=0
for i in range (0,len(cadena)):
	if cadena[i]==" ":
		subcadena=cadena[p:i]
		p=i+1
		if len(subcadena)>=n:
			suma+=1
	if i==(len(cadena)-1):
		subsubcadena=cadena[p:i+1]
		if len (subsubcadena)>=n:
			suma+=1	
if suma>1:
	print ("Hay palabras largas")
else:
	print ("No hay palabras largas.")