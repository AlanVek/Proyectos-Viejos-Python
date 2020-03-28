from math import pi

opcion=""

while opcion!="d":
	print ("Elija una de las siguientes opciones:")
	print ("- a: Calcular el diámetro de la circunferencia.")
	print ("- b: Calcular el perímetro de la circunferencia.")
	print ("- c: Calcular el área de la circunferencia. ")
	print ("- d: Finalizar.")
	

	opcion= input("Ingrese la opción elegida: ")

	if opcion=="a":
		radio= float(input("Ingrese el radio de la circunferencia: "))
		
		print ("El diámetro de la circunferencia es: ", 2*radio)

	elif opcion=="b":
		radio= float(input("Ingrese el radio de la circunferencia: "))
		
		print ("El perímetro de la circunferencia es: ", 2*pi*radio)

	elif opcion=="c":
		radio= float(input("Ingrese el radio de la circunferencia: "))
		
		print ("El área de la circunferencia es: ", pi*(radio**2))

	elif opcion!="d":
		
		print ("Debe ingresar una de las siguientes opciones: a, b, c o d")

print ("Gracias por usar el programa")