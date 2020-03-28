a= (input("Ingrese primera palabra: "))
b= (input("Ingrese segunda palabra: "))
c= (input("Ingrese tercera palabra: "))
d= (input("Ingrese cuarta palabra: "))
e= (input("Ingrese quinta palabra: "))

candidato=a

if b.lower()<candidato.lower():
	candidato=b

if candidato.lower()>c.lower():
	candidato=c

if candidato.lower()>d.lower():
	candidato=d
		
if candidato.lower()>e.lower():
	candidato=e


print ("La primera en orden alfabético es: ",candidato)
