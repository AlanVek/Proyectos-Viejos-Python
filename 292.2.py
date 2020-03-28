def divisores(n):
	suma=0
	for i in range (1,n):
		if n%i==0:
			suma+=i

	return (suma)

n=int(input("Ingrese número: "))

for i in range (0,n-1):
	for j in range (i+1,n):
			if divisores(i)==j and divisores(j)==i:
					print (i,"y",j,"son amigos.")

