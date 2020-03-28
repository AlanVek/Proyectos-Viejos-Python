tamaño=""
suma=0
suma2=0
c60=0
while tamaño!=0:
	tamaño=int(input("Ingrese el tamaño: "))
	while tamaño!=60 and tamaño !=120 and tamaño!=0:
		tamaño=int(input("El tamaño debe ser 60 ó 120 gramos. En caso de no comprar, ingrese 0: "))
	if tamaño!=0:
		cantidad=int(input("Ingrese la cantidad deseadas de huevos de Pascuas: "))
		while cantidad<=0:
			cantidad=int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))
		suma=suma+cantidad
		suma2=suma2+tamaño*cantidad
		if tamaño==60:
			c60=c60+cantidad

print ("La cantidad necesaria de chocolate son",suma2,"gramos.")
print ("La cantidad de huevos a producir es",suma)
print ("La cantidad de huevos de 60 gramos es",c60)