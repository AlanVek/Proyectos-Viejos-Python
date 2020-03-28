n=input("Ingrese palabra: ")


for i in range (0,len(n)-1):
	if n[i]<n[i+1]:
		alf=True
	else:
		alf=False
		break

if alf:
	print ("La palabra es alfabética.")
else:
	print ("La palabra no es alfabética.")