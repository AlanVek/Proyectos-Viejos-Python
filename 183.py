n=input("Ingrese cadena: ")

cadena=""
a=""
for i in n:
	if not i<"0":
		a+=i

for i in range (len(a)-1,-1,-1):
	cadena=cadena+a[i]

if cadena==a:
	print ("Es palíndromo.")
else:
	print ("No es palíndromo.")
