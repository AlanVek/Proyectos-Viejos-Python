try: 
	f=int(input("Ingrese la cantidad de veces que desee utilizar el programa: "))
	while f<0 or f%1!=0:
		print ("Debe ingresar un valor entero y mayor a 0. Inténtelo de nuevo: ")
	t=0
	while t<f:
		try:
			a=int(input("Ingrese el primer número: "))
			b=int(input("Ingrese el segundo número: "))
			c=int(input("Ingrese el tercer número: "))

			d=min(a,b,c)

			for i in range(1,d+1):
				if a%i==0 and b%i==0 and c%i==0:
					l=i


			print ("El máximo común divisor entre los tres número es: ",l)

		except:
			print ("No ha ingresado un número correcto.")

		t=t+1
except:
	print("La cantidad de repeticiones no ha sido un valor válido. El programa se cerrará.")

print ("Gracias por usar el programa.")
