n= int(input("Ingrese valor principal: "))
m= int(input("Ingrese número a multiplicar: "))

if (m*n)>0:
	suma=0
	while suma<(m*n):
		suma=suma+n
		print (suma)

if (m*n)<0:
	if n>0:
		suma=2*n
		while suma>(m*n):
			suma=suma-n
			print (suma)
	if m>0:
		suma=0
		while suma>(m*n):
			suma=suma+n
			print (suma)

if (m*n)==0:
	print ("0")