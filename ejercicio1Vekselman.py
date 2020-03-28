def listaoperacion(lista):
	a=int(input("Ingrese operación. 1.Venta, 2.Alquiler: "))
	while a!=1 and a!=2:
		a=int(input("La operación ingresada no es correcta. Inténtelo de nuevo: "))

	lista+=[a]
	return(lista)
def listatipo(lista):
	a=int(input("Ingrese el tipo. 1.Vivienda, 2.Local Comercial, 3.Terreno: "))
	while a!=1 and a!=2 and a!=3:
		a=int(input("El tipo ingresado no es correcto. Inténtelo de nuevo: "))
	lista+=[a]
	
def noenlista(a,lista):
	enlista=False
	for i in range (0,len(lista)):
		if lista[i]==a:
			enlista=True
			break
	if not enlista:
		lista+=[a]

def listabarrio(lista,listarepe):
	a=input("Ingrese nombre del barrio: ")
	noenlista(a,lista)
	listarepe+=[a]
	
def listasup(lista):
	a=int(input("Ingrese superficie: "))
	while a<30:
		a=int(input("La superficie debe tener al menos 30 metros cuadrados. Inténtelo de nuevo: "))
	lista+=[a]
	
def listaprecio(lista):
	a=int(input("Ingrese precio: "))
	while a<1000:
		a=int(input("El precio debe ser al menos 1000. Inténtelo de nuevo: "))
	lista+=[a]
	

def listaidentif(oper,tipo,barrio,lista):
	for i in range (0,len(oper)):
		if barrio[i].find(" ")==-1:
			identif=str(oper[i])+str(tipo[i])+barrio[i][0:(len(barrio[i]))//2]
		else:
			a=barrio[i].find(" ")
			identif=str(oper[i])+str(tipo[i])+barrio[i][0]+barrio[i][a+1]
		lista+=[identif]
def listapreciosmetrocuad(precios,sup,lista):
	for i in range (0,len(precios)):
		lista+=[precios[i]/sup[i]]
def promediopreciosmetrocuad(preciosmetrocuad):
	suma=0
	for i in range (0,len(preciosmetrocuad)):
		suma+=preciosmetrocuad[i]
	return (suma/len(preciosmetrocuad))
def propmaysup(superficies,identificadores):
	mayor=superficies[0]
	indice=0
	for i in range (1,len(superficies)):
		if superficies[i]>mayor:
			mayor=superficies[i]
			indice=i
	return ([mayor,identificadores[indice]])
operaciones=[]
tipos=[]
precios=[]
barrios=[]
superficies=[]
identificadores=[]
preciosmetrocuad=[]
barriorepe=[]

opcion=""
while opcion!="n":
	listaoperacion(operaciones)
	listatipo(tipos)
	listasup(superficies)
	listaprecio(precios)
	listabarrio(barrios,barriorepe)

	opcion=input("Si desea terminar, presione 'n'. Si desea seguir, presione cualquier otra tecla: ")

listaidentif(operaciones,tipos,barriorepe,identificadores)
listapreciosmetrocuad(precios,superficies,preciosmetrocuad)

a=propmaysup(superficies,identificadores)
print ("Lista de barrios: ")
print(barrios)
print("Lista de identificadores de propiedades: ")
print(identificadores)
print("Lista de precios por metro cuadrado para propiedades en venta: ")
print(preciosmetrocuad)
print("Promedios de precios por metro cuadrado para propiedades en venta: ", promediopreciosmetrocuad(preciosmetrocuad))
print("Propiedad de mayor superficie: ",a[1],a[0],"metros cuadrados")

