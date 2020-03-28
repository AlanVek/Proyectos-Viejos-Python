cadena=input("Ingrese cadena: ")

suma=0

for i in range (1,len(cadena)):
	
	if (cadena[i]>"9" or cadena[i]<"0") and (cadena[i-1]<="9" and cadena[i-1]>="0"):
		suma+=1

	if i==(len(cadena)-1):
		if "0"<=cadena[i]<="9":
			suma+=1

print (suma)


