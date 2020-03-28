letra= input("Ingrese letra: ")

if letra>='a' and letra<='z' or letra=='ñ':
	print ("La letra es una minúscula.")

else:
	if letra>='A' and letra<='Z' or letra=='Ñ':
		print ("La letra es una mayúscula")
	else:
		print ("No es letra")
