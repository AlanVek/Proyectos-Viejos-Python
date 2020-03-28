a= (input("Ingrese primera palabra: "))
b= (input("Ingrese segunda palabra: "))
c= (input("Ingrese tercera palabra: "))
d= (input("Ingrese cuarta palabra: "))
e= (input("Ingrese quinta palabra: "))

candidato=a

if b<candidato:
	candidato=b

if candidato>c:
	candidato=c

if candidato>d:
	candidato=d
		
if candidato>e:
	candidato=e


print ("La primera en orden alfabético es ", candidato)