a= float(input("Ingrese número: "))
i=1

while a%1!=0:
	a=float(input("El número ingresado debe ser entero. Inténtelo de nuevo: "))

while i<=10:
	print (a,"x",i,"= ",a*i)
	i=i+1