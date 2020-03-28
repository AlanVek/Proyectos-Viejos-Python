n=input("Ingrese cadena: ")
k=int(input("Ingrese entero: "))

p=0
subcadena=""
subsubcadena=""
for i in range (0,len(n)):
	if n[i]==" ":
		subcadena=n[p:i]
		p=i+1
		if len(subcadena)==k:
			print (subcadena)
	if i==(len(n)-1):
		subsubcadena=n[p:i+1]
		if len(subsubcadena)==k:
			print (subsubcadena)

