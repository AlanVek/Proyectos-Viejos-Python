n= int(input("Ingrese el valor inicial: "))
m= int(input("Ingrese el valor final: "))
suma=0

if n%2==0 and m%2==0:
	for i in range (n,m+1,2):
		suma=suma+i

if n%2==0 and m%2!=0:
	for i in range (n,m,2):
		suma=suma+i2

if n%2!=0 and m%2==0:
	for i in range (n+1,m+1,2):
		suma=suma+i

if n%2!=0 and m%2!=0:
	for i in range (n+1,m,2):
		suma=suma+i

print (suma)
