a= int(input("Ingrese número: "))

primo=True 

for i in range(2,a):
	if a%i==0:
		primo=False
		break

if primo:
	print ("El número",a,"es primo.")
else:
	print ("El número",a,"no es primo.")