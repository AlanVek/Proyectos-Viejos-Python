suma_e=0
suma_a=0
n1=input("Ingrese nombre del jugador: ")
e1=int(input("Ingrese edad del jugador: "))
a1=int(input("Ingrese altura del jugador: "))
lista_n=[n1]
lista_e=[e1]
lista_a=[a1]
for i in range (0,9):
	n=input("Ingrese nombre del jugador: ")
	e=int(input("Ingrese edad del jugador: "))
	a=int(input("Ingrese altura del jugador: "))
	lista_nn=[n]
	lista_n=lista_n+lista_nn
	lista_ee=[e]
	lista_e=lista_e+lista_ee
	lista_aa=[a]
	lista_a=lista_a+lista_aa


t= lista_e.index(max(lista_e))
nmaxe=lista_n[t]

print ("El de mayor edad se llama: ",nmaxe)

p=lista_a.index(min(lista_a))
nmina=lista_n[p]
print ("El de menor altura se llama: ",nmina)

suma=0
i=0
while i<10:
	y=lista_e[i]
	suma=suma+y
	i=i+1
print ("El promedio de edades es: ",suma/10)

suma2=0
g=0
while g<10:
	h=lista_a[g]
	suma2=suma2+h
	g=g+1
print ("El promedio de alturas es: ",suma2/10)