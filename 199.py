a=input("Ingrese primer cadena: ")
b=input("Ingrese segunda cadena: ")

c=""
for i in range (0,len(a)):
	if a[i]==b[0]:
		c+=a[i:i+len(b)]
			


if c==b:
	print (b,"es subcadena de",a)
else:
	print (b,"no es subcadena de",a)