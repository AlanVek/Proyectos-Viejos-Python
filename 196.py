n=input("Ingrese cadena: ")

p=0
for i in range (0,len(n)):
	if n[i]==" ":
		subcadena=n[p:i]
		p=i+1
		if len(subcadena)==3:
			print (subcadena)
	if i==(len(n)-1):
		subsubcadena=n[p:i+1]
		if len(subsubcadena)==3:
			print (subsubcadena)
