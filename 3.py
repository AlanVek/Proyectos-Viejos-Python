opcion=""
suma_seda=0
suma_total=0

while opcion!="Fin":
	n=input("Ingrese nombre del producto: ")
	c=int(input("Ingrese categoría del producto: 1.Lana, 2.Hilo de algodón, 3.Seda: "))
	while c!=1 and c!=2 and c!=3:
		c=int(input("La categoría ingresada no fue correcta. Inténtelo de nuevo. 1.Lana, 2.Hilo de algodón, 3.Seda: "))

	pk=float(input("Ingrese el precio por kilogramo: "))
	while pk>200 or pk<1:
		pk=float(input("El precio por kilogramo debe estar entre $1 y $200. Inténtelo de nuevo: "))

	p=float(input("Ingrese peso en kilogramos: "))
	while p>10 or p<0.1:
		p=float(input("El peso debe estar entre 100 gramos (0.1kg) y 10kg. Inténtelo de nuevo: "))

	if c==3:
		suma_seda+=p

	suma_total+=p*pk

	opcion=input("¿Desea seguir ingresando datos? Presione cualquier tecla para continuar o escriba 'Fin' para terminar: ")
print ("----------------------------------------------------------------------------------------------------------")
print ("El precio total de lo vendido fue:",suma_total)
print ("Los kilogramos de seda vendidos fueron:",suma_seda)

