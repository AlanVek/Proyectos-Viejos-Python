n=int(input("Ingrese número: "))


if 0<n<10:
	suma=n

if 10<=n:
	i=10
	suma=0
	while n//i!=0:
		suma+=n%i
		n=n//i

	suma=suma+n
		

print (suma)



	

		