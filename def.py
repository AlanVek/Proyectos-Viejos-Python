def f(x,y,z):
	
	print ("El resultado es: ",(x**y)+z)

def funcion():
	try:
		a=int(input("Ingrese base: "))
		b=int(input("Ingrese exponente: "))
		c=int(input("Ingrese suma: "))
		if a%a==0 and b%b==0 and c%c==0:
	 		return f(a,b,c)
	except:
		print("No ha ingresado los datos correctos. Esta repetición se cancelará".)


l= int(input("Elija cantidad de repeticiones: "))
i=0
while i<l:
	funcion()
	i=i+1

print("Hasta luego.")