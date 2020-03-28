zona=""
supmay=0
n=0
supzonamax=0
while zona!="Z":
	zona=input("Ingrese zona: ")
	while zona!="A" and zona!="B" and zona!="C" and zona!="Z":
		zona=input("Las zonas válidas son 'A', 'B' y 'C'. Inténtelo de nuevo: ")
	if zona!="Z":
		sup=float(input("Ingrese superficie: "))
		while sup<40:
			sup=float(input("La superficie debe ser mayor o igual a 40 metros cuadrados. Inténtelo de nuevo: "))
		if sup>100:
			supmay=supmay+1
		if sup>supzonamax:
			supzonamax=sup
			zonamax=zona
		n=n+1


try:
	print("La zona donde se registró la mayor superficie fue: ",zonamax)
except:
	print ("La zona donde se registró la mayor superficie no se puede proveer porque no se han ingresado datos.")
print ("La cantidad de datos ingresados fue: ",n)
try:
	print ("El porcentaje de superficies mayores que 100 metros cuadrados en relación al total es: ", (supmay/n)*100,"%")
except:
	print ("El porcentaje de superficies mayores a 100 metros cuadrados no se puede proveer debido a la falta de datos.")



