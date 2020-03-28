a=input("Ingrese primer cadena: ")
b=input("Ingrese segunda cadena: ")
c=input("Ingrese tercera cadena: ")

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

pref2=True
cadena2=""
g=min(len(cadena),len(c))
h=0
while pref2==True and h<g:
	if cadena[h]==c[h]:
		cadena2+=c[h]
	else:
		pref=False
	h=h+1


print ("El prefijo común más largo entre las tres cadenas es: '",cadena2,"'")