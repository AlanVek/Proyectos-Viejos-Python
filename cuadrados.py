numero1=float(input("Ingrese primer número:"))
numero2=float(input("Ingrese segundo número:"))

if numero1**2>numero2:
	print ("El segundo es menor que el cuadrado del primero")

else:
	if numero1**2<numero2:
		print ("El segundo es mayor que el cuadrado del primero")
	else:
		print ("El segundo es el cuadrado del primero")