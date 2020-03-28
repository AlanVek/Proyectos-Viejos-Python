a=[[1,4,5,-1],[2,6,-1,-1],[3,5,9,-1],[-1,-1,7,-1]]


def cantentre(a,b):
	suma=0
	for i in range (1,len(a[0])):
		if a[b-1][i]!=-1:
			suma+=1

	print ("El alumno",b,"entregó",suma,"ejercicios.")
cantentre(a,1)

def media(a,b):
	suma=0
	cant=0

	for i in range (1,len(a[0])):
		if a[b-1][i]!=-1:
			suma+=a[b-1][i]
			cant+=1

	if cant!=0:
		print ("La media del alumno",b,"es: ",suma/cant)
	else:
		print ("No entregó ejercicios.")

media(a,2)
def media2(a,b):
	suma=0
	cant=0

	for i in range (1,len(a[0])):
		if a[b-1][i]!=-1:
			suma+=a[b-1][i]
			cant+=1

	if cant==len(a[0])-1:
		return(suma/cant)
	
	else:
		return (0)
media2(a,1)
media2(a,2)

def medyentre(a):
	suma=0
	for i in range (0,len(a)):
		if media2(a,i,2)>3.5:
			suma+=1

	print ("La cantidad de estudiantes que presentaron todos los ejercicios y tienen media mayor a 3.5 es: ",suma)
medyentre(a)


def cantejerentre(a,b):
	suma=0
	for i in range (0,len(a)):
		if a[i][b]!=-1:
			suma+=1

	print ("La cantidad de estudiantes que entregaron el ejercicio",b,"es:",suma)
cantejerentre(a,3)


def mediaejerentre(a,b):
	cant=0
	suma=0
	for i in range (0,len(a)):
		if a[i][b]!=-1:
			suma+=a[i][b]
			cant+=1

	if cant!=0:
		print ("La nota media del ejercicio número",b,"es:",suma/cant)
	else:
		print ("Nadie entregó el ejercicio",b)

mediaejerentre(a,3)

def maxejer(a,b):
	maximo=a[0][b-1]

	for i in range (1,len(a)):
		if a[i][b]>maximo:
			maximo=a[i][b]

	print ("La nota más alta obtenida en el ejercicio",b,"fue",maximo)
maxejer(a,1)

def minejer(a,b):
	minimo=a[0][b]

	for i in range (1,len(a)):
		if a[i][b]<minimo and a[i][b]!=-1:
			minimo=a[i][b]

	print ("La nota más baja obtenida en el ejercicio",b,"fue",minimo)

minejer(a,3)

def abandonos(a):
	listaba=[]
	for j in range (1,len(a[0])):
		suma=0
		for i in range (0,len(a)):
			esta=False
			for p in range (0,len(listaba)):
				if listaba[p]==i:
					esta=True
			if a[i][j]==-1 and esta==False:
				aba=True
				for t in range (j,len(a[0])):
					if a[i][t]!=-1:
						aba=False
				if aba==True:
					suma+=1
					listaba+=[i]
		print ("En la semana",j-1,"abandonaron",suma,"personas.")

abandonos(a)



