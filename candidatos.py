a= float(input("Ingrese primer número: "))
b= float(input("Ingrese segundo número: "))
c= float(input("Ingrese tercer número: "))
d= float(input("Ingrese cuarto número: "))
e= float(input("Ingrese quinto número: "))

candidato=a

if b>candidato:
	candidato=b

if candidato<c:
	candidato=c
	
if candidato<d:
	candidato=d
		
if candidato<e:
	candidato=e


print ("El máximo es ", candidato)