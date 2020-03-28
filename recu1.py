def divicom(a,b):
	n=min(a,b)
	lista=[]
	for i in range (1,n+1):
		if n%i==0 and b%i==0:
			lista+=[i]

	return (lista)

def maxcomdiv(a,b):
	lista1=divicom(a,b)

	n=lista1[0]
	maximo=n
	if len(lista)>=1:
		for i in range (1,len(lista1)):
			if lista1[i]>n:
				maximo=lista1[i]
	return (maximo)

def may1(a):
	while a<=1:
		a=int(input("El número debe ser mayor que 1. Inténtelo de nuevo: "))



n=int(input("Ingrese el primer número: "))
may1(n)
m=int(input("Ingrese el segundo número: "))
may1(m)

print ("Los divisores comunes a ambos son:", divicom(n,m))
print ("El máximo común divisor entre ambos es: ", maxcomdiv(n,m))