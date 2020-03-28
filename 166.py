n=input("Ingrese número: ")

entero=True
for i in n:
	if i<"0" or i>"9":
		entero=False

if entero:
	print ("Es entero.")
else:
	print ("No es entero.")