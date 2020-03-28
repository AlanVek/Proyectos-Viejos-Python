opcion=""

i=0
suma=0

while opcion!="N":
	n=int(input("Ingrese número: "))
	suma+=n
	i+=1
	opcion=input("¿Desea continuar?: ")

print ("El promedio es: ",suma/i)