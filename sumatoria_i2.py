n= int(input("Ingrese el valor inicial: "))
m= int(input("Ingrese el valor final: "))
suma=0

for i in range (n,m+1):
	suma=suma+i**2

print (suma)