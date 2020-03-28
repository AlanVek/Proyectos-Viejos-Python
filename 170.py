n=input("Ingrese número binario: ")


i=0

while i<len(n):
	if n[i]!="1" and n[i]!="0":
		n=input("No ha ingresado un binario correcto. Inténtelo de nuevo: ")
		i=-1
	i=i+1