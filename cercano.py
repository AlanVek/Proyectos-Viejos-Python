from math import*

a= float(input("Ingrese el primer número: "))
b= float(input("Ingrese el segundo número: "))
c= float(input("Ingrese el tercer número: "))
d= float(input("Ingrese el cuarto número: "))
e= float(input("Ingrese el quinto número: "))

uno= abs(a-b)
dos= abs(a-c)
tres= abs(a-d)
cuatro= abs(a-e)

if dos<uno and dos<tres and dos<cuatro:
	print ("El número más cercano a ", a, "es: ", c)

else:
	if tres<uno and tres<dos and tres<cuatro:
		print ("El número más cercano a ", a, "es: ", d)
	else:
		if cuatro<uno and cuatro<dos and cuatro<tres:
			print ("El número más cercano a ", a, "es: ", e)
		else: 
			if uno<dos and uno<tres and uno<cuatro:
				print ("El número más cercano a ", a, "es: ", b)

if uno==dos and uno<tres and uno<cuatro:
	print ("Los números más cercanos a ", a, "son: ", b, "y", c)

if uno==tres and uno<dos and uno<cuatro:
	print ("Los números más cercanos a ", a, "son: ", b, "y", d)
if uno==cuatro and uno<dos and uno<tres:
	 print ("Los números más cercanos a ", a, "son: ", b , "y",e)
if dos==tres and dos<uno and dos<cuatro:
	print ("Los números más cercanos a ", a, "son: ", c, "y",d)
if dos==cuatro and dos<uno and dos<tres:
	print ("Los números más cercanos a ", a, "son: ", c, "y",e)
if tres==cuatro and tres<uno and tres<dos:
	print ("Los números más cercanos a ", a, "son: ", d, "y",e)
if uno==dos and uno==tres and uno<cuatro:
	print ("Los números más cercanos a ", a, "son: ", b,",",c, "y", d)
if uno==dos and uno==cuatro and uno<tres:
	print ("Los números más cercanos a ", a, "son: ", b, ",", c, "y", e)
if uno==tres and uno==cuatro and uno<dos:
	print ("Los números más cercanos a ", a, "son: ", b,",", d, "y", e)
if dos==tres and dos==cuatro and dos<uno:
	print ("Los números más cercanos a ", a, "son: ", c,",",d,"y",e)
if uno==dos and uno==tres and uno==cuatro:
	print ("Los números más cercanos a ", a, "son: ",b, ",", c, ",", d, "y", e)




