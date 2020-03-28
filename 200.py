a=input("Ingrese primera cadena: ")
b=input("Ingrese segunda cadena: ")

pref=True
cadena=""
d=min(len(b),len(a))
i=0
while pref==True and i<d:
	if a[i]==b[i]:
		cadena+=a[i]
	else:
		pref=False
	i=i+1



print ("El prefijo común más largo entre ambas cadenas es: '",cadena,"'")