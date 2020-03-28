a= float(input("Ingrese el primer lado del triángulo: "))
b= float(input("Ingrese el segundo lado del triángulo: "))
c= float(input("Ingrese el tercer lado del triángulo: "))

if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
	if (a==b or a==c or b==c) and (a!=b or b!=c or a!=c):
		print ("El triángulo es isósceles.")

	else:
		if a!=b and b!=c and a!=c:
			print ("El triángulo es escaleno.")
		else:
			print ("El triángulo es equilátero.")
else:
	print ("No es triángulo.")