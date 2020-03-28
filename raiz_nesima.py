a=float(input("Ingrese número: "))
i=2

while a<0:
	a=float(input("El número ingresado no puede ser menor a 0. Inténtelo de nuevo: "))
	
while i<=100:
	p=a**(1/i)
	print (p)
	i=i+1