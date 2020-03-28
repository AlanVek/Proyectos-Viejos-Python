from math import pi
opcion=""

while opcion!="3":
	print ("Las opciones son: ")
	print ("1) Calcular perímetro.")
	print ("2) Calcular área.")
	print ("3) Salir.")
	
	opcion=input("Ingrese la opción deseada: ")

	if opcion=="1":
		print ("Las opciones son: ")
		print ("1) Triángulo.")
		print ("2) Cuadrado. ")
		print ("3) Círculo")
		print ("4) Regresar. ")

		opcion1=input("Ingrese la opción deseada: ")

		if opcion1=="1":
			a=int(input("Ingrese lado del triángulo: "))
			b=int(input("Ingrese lado del triángulo: "))
			c=int(input("Ingrese lado del triángulo: "))
			print ("El perímetro es: ",a+b+c)
			
		if opcion1=="2":
			a=int(input("Ingrese lado del cuadrado: "))
			print ("El perímetro es: ",4*a)
			
		if opcion1=="3":
			a=float(input("Ingrese radio del círculo: "))
			print ("El perímetro es: ",2*pi*a)
			
	if opcion=="2":
		print ("Las opciones son: ")
		print ("1) Triángulo.")
		print ("2) Cuadrado. ")
		print ("3) Círculo")
		print ("4) Regresar. ")

		opcion1=input("Ingrese la opción deseada: ")

		if opcion1=="1":
			a=int(input("Ingrese altura del triángulo: "))
			b=int(input("Ingrese base del triángulo: "))
			print ("El área es: ",a*b/2)
			
		if opcion1=="2":
			a=int(input("Ingrese lado del cuadrado: "))
			print ("El área es: ",a**2)
			
		if opcion1=="3":
			a=float(input("Ingrese radio del círculo: "))
			print ("El área es: ",pi*(a**2))
			
print ("Gracias por usar el programa.")

