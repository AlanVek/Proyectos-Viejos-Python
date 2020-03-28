def divisores(n):
	suma=0
	for i in range (0,n):
		if n%i==0:
			suma+=n

	return (suma)

n=int(input("Ingrese número: "))

for i in range (0,n-1):
	for j in range (i+1,n):
			if divisores(i)==divisores(j):
					print (i,"y",j,"son amigos.")

