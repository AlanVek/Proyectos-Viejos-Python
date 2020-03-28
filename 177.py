cadena=input("Ingrese cadena con letras de la 'a' a la 'f': ")

i=0

while i<len(cadena):
	if cadena[i]>"f" or cadena[i]<"a":
		cadena=input("Ha ingresado valores no permitidos. Intente de nuevo: ")
		i=0
	else:
		i=i+1


print (int(cadena,16))