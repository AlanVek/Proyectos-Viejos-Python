n=int(input("Ingrese la cantidad de notas del estudiante: "))

p=float(input("Ingrese nota: "))

d=0
if p>4:
	suma_a=p
	a=1
else:
	suma_a=0
	a=0
if p<4:
	suma_d=p
	d=1
else:
	suma_d=0
	d=0

suma_t=p

i=1

while i<n:
	h=float(input("Ingrese nota: "))
	if h>4:
		suma_a=suma_a+h
		a=a+1
	if h<4:
		suma_d=suma_d+p
		d=d+1
	suma_t+=h
	i=i+1	

print ("La cantidad de notas aprobadas es: ",a)
print ("La cantidad de notas desaprobadas es: ",d)
print ("El promedio de notas es: ",suma_t/n)
print ("El promedio de notas aprobadas es: ",suma_a/a)
print ("El promedio de notas desaprobadas es. ",suma_d/d)