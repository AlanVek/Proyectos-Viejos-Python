n= float(input("Ingrese base: "))
m= float(input("Ingrese exponente: "))

while n<0:
	n= float(input("Debe ingresar una base mayor a 0. Ingréselo de nuevo: "))

i=0

if m>0:
	exp=0
	while exp<n**m:
		exp= n**i
		print (exp)
		i=i+1

if m<0:
	exp=1000000000000000000000000000000000000000000000000000000
	while exp>n**m:
		exp=n**i
		print (exp)
		i=i-1
