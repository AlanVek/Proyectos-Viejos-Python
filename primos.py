a=int(input("Ingrese número: "))

primo=True

for i in range(2,a+1):

	primo=True
	for divisor in range (2,i-1):
		if i%divisor==0:
			primo=False
			break

	if primo==True:
		print (i)


