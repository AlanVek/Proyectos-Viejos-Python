i=0
n1=input("Ingrese nombre: ")
e1=int(input("Ingrese edad: "))
a1=int(input("Ingrese altura: "))
suma_a=a1
suma_e=e1
nemax=n1
namin=n1
while i<9:
	n=input("Ingrese nombre: ")
	e=int(input("Ingrese edad: "))
	a=int(input("Ingrese altura: "))
	suma_a=suma_a+a
	suma_e=suma_e+e
	if a<a1:
		a1=a
		namin=n
	if e>e1:
		e1=e
		nemax=n
	i=i+1

print ("El promedio de edades es: ", suma_e/10)
print ("El promedio de alturas es: ", suma_a/10)
print ("El de mayor edad es: ",nemax)
print ("El de menor altura es: ",namin)