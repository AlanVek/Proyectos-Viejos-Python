def reversa(cadena):
	indice=-1
	cont=len(cadena)
	invertida=""
	while cont>=1:
		invertida=invertida+cadena[indice]
		indice=indice-1
		cont=cont-1
	return invertida

palabra=input ("Ingrese palabra: ")

if palabra.lower()==reversa(palabra.lower()):
	print ("Es palíndromo")

else:
	print ("No es palíndromo")