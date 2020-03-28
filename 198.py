a=input("Ingrese primer cadena: ")
b=input("Ingrese segunda cadena: ")

pref=True
for i in range (0,len(b)):
	if a[i]!=b[i]:
		pref=False

if pref:
	print (b,"es prefijo de",a)
else:
	print (b,"no es prefijo de",a)