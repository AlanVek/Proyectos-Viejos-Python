n=input("Ingrese nombre de usuario: ")

while len(n)<6:
	n=input("El nombre de usuario debe tener al menos 6 caracteres. Inténtelo de nuevo: ")
while len(n)>12:
	n=input("El nombre de usuario debe tener máximo 12 caracteres. Inténtelo de nuevo: ")

if 6<=len(n)<=12:
	for i in n:
		while i<"0" or i>"z":
			valido=False
			n=input("El nombre de usuario sólo puede tener letras o números. Inténtelo de nuevo: ")
			break
		if i>"0" or i<"z":
			valido=True

	if valido:
		print ("El nombre de usuario es válido.")