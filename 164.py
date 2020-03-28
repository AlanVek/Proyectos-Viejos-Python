cadena=input("Ingrese cadena: ")

suma=0

for i in cadena:
	if "0"<=i and i<="9":
		suma+=1

print ("Hay",suma,"dígitos.")