def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)

try:
	x=(int(input("Ingrese número para decir su factorial: ")))
	while x<0 or x//1!=x:
		x=int(input("El número debe ser entero y mayor a 0. Inténtelo de nuevo: "))

	print (factorial(x))

except:
	print("Ha habido un error. La aplicación se cerrará.")