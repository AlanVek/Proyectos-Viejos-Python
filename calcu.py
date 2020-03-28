opcion=""
	
while opcion!="e":
	print ("Elija la operación a realizar:")
	print ("a) Suma")
	print ("b) Resta")
	print ("c) Multiplicación")
	print ("d) División")
	print ("e) Salir")
	opcion=input("Ingrese la opción elegida: ")

	if opcion=="a":
		n=int(input("Elija la cantidad de números a sumar: "))
		suma=0
		for i in range (0,n):
			p=int(input("Ingrese número: "))
			suma=suma+p
		print ("La suma es: ",suma)

	elif opcion=="b":
		n=int(input("Elija la cantidad de números a restar: "))
		t=int(input("Ingrese número: "))
		resta=t
		for i in range (0,n-1):
			p=int(input("Ingrese número: "))
			resta=resta-p
		print ("La resta es: ",resta)
	elif opcion=="c":
		n=int(input("Elija la cantidad de números a multiplicar: "))
		t=int(input("Ingrese número: "))
		multip=t
		for i in range (0,n-1):
			p=int(input("Ingrese número: "))
			multip=multip*p
		print ("La multiplicación es: ",multip)
	elif opcion=="d":
		n=int(input("Elija la cantidad de números a dividir: "))
		t=int(input("Ingrese número: "))
		divid=t
		for i in range (0,n-1):
			p=int(input("Ingrese número: "))
			divid=divid/p
		print ("La división es: ", divid)

	elif opcion!="e":
		print ("No ha ingresado una opción válida. Inténtelo de nuevo: ")
	elif opcion=="e":
		break

print ("Gracias por usar el programa. Adiós.")



			
