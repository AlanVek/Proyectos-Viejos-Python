n=input("Ingrese palabra: ")

cadena=""
for i in range (len(n)-1,-1,-1):
	cadena=cadena+n[i]

if cadena==n:
	print ("Es palíndromo.")
else:
	print ("No es palíndromo.")
