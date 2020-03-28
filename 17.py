
i=0
n=0
opcion="si"
suma=0
while opcion=="si":
	n1=float(input("Ingrese nota: "))
	n2=float(input("Ingrese nota: "))
	n3=float(input("Ingrese nota: "))
	suma1=n1+n2+n3
	suma=suma+suma1
	print ("El promedio del alumno es: ",suma1/3)
	n=n+1
	opcion=input("¿Desea cargar las notas de otro alumno? Ponga 'si' o 'no': ")
	

print ("El promedio del curso es: ", suma/(3*n))

