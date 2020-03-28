def minim10(a):
	while a<10:
		a=int(input("El precio debe ser mínimo $10. Inténtelo de nuevo: "))
def dist123(a):
	while a!=1 and a!=2 and a!=3:
		a=int(input("El número debe ser 1, 2 ó 3. Inténtelo de nuevo: "))

def noenlista(a,b):
	esta=False
	for i in range (0,len(b)):
		if b[i]==a:
			esta=True
			break
	if esta==False:
		b+=[a]

def mitad(a):
	b=a[0:(len(a)//2)]
	return (b)
def tipopub(a):
	if a==1:
		cual="Diario"
	elif a==2:
		cual="Semanal"
	elif a==3:
		cual="Mensual"
	return (cual)
def listanom(nombres):
	a=input("Ingrese nombre del cliente: ")
	noenlista(a,nombres)
	return (nombres)
def listaejem(ejem):
	b=input("Ingrese nombre del ejemplar: ")	
	ejem+=[b]
	return (ejem)
def listaprecios(precios):
	c=int(input("Ingrese precio del ejemplar: "))
	minim10(c)
	precios+=[c]
	return (precios)

def listatipo(tipos):
	d=int(input("Ingrese el tipo de publicación. 1: Diario, 2: Semanal, 3: Mensual: "))
	tipos+=[d]
	return (tipos)

def identif(ejem,tipos,ident):
	ident=[]
	for i in range (0,len(tipos)):
		ident+=[mitad(ejem[i])+tipopub(tipos[i])]

	return (ident)

def mascaro(a):
	maximo=a[0]
	n=0
	for i in range (1,len(a)):
		if a[i]>maximo:
			maximo=a[i]
			n=i
	return ([maximo,n])

def recaud(a,b):
	suma=0
	for i in range (0,len(a)):
		if b[i]==1:
			suma+=31*a[i]
		elif b[i]==2:
			suma+=4*a[i]
		elif b[i]==3:
			suma+=a[i]
	return (suma)

nombres=[]
ejem=[]
precios=[]
tipos=[]
ident=[]
opcion=""

while opcion!="n":
	listanom(nombres)
	listaejem(ejem)
	listaprecios(precios)
	listatipo(tipos)

	opcion=input("Si desea seguir, presione cualquier tecla. Si no, pulse 'n': "  )

listaid=identif(ejem,tipos,ident) 

mascaroejem=mascaro(precios)

print ("La lista de clientes es: ", nombres )
print ("La lista de identificadores es: ", listaid)
print ("El ejemplar más caro es: ",ejem[mascaroejem[1]], "y cuesta: ", mascaroejem[0] )
print ("La recaudación prevista para el mes de octubre es: ", recaud(precios,tipos) )