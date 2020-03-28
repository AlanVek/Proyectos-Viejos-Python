from random import*

i=0
suma=0
suma_prom=0
while i<10:
	n=randint(1,10000)

	if n%5==0 and n%3==0:
		suma+=1
	suma_prom+=n
	print(n)
	i=i+1

print ("El promedio de todos los números es:",suma_prom/10)
print (suma,"es/son múltiplo(s) de 3 y 5 a la vez.")
