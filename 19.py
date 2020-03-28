n1=float(input("Ingrese nota: "))
while n1<1 or n1>10:
	n1=float(input("Las notas deben estar entre 1 y 10. Inténtelo de nuevo: "))
a1=float(input("Ingrese altura: "))
while a1>2 or a1<1.5:
	a1=float(input("Las alturas deben estar entre 1.5 y 2m. Inténtelo de nuevo: "))

suma=n1
if a1>1.6:
	suma6=1
else:
	suma6=0

i=0

while i<9:
	n=float(input("Ingrese nota: "))
	while n<1 or n>10:
		n=float(input("Las notas deben estar entre 1 y 10. Inténtelo de nuevo: "))
	a=float(input("Ingrese altura: "))
	while a>2 or a<1.5:
		a=float(input("Las alturas deben estar entre 1.5 y 2m. Inténtelo de nuevo: "))
	suma+=n
	if a>1.6:
		suma6=suma6+1
	if a>a1:
		a1=a

	i=i+1

print ("El promedio de las notas es: ",suma/10)
print ("La altura máxima es: ",a1)
print ("La cantidad de alumnos más altos que 1.6m es: ",suma6)
