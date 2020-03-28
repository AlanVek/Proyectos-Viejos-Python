n=int(input("Ingrese número: "))

while n%1!=0:
	n=int(input("El número debe ser entero. Inténtelo de nuevo: "))

a=str(n)

for i in range (len(a)-1,-1,-1):
	print (a[i])
	