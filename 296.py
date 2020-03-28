nombres=["Alan","Franco","Lautaro"]
tiempo=[[1,0.9,1,0.58,1.02],[6,0,0,1,2],[1,3,5,3,2]]


def ganador(a,b):
	suma=0
	for j in range (0,5):
		suma+=b[0][j]
	minimo=suma
	minindice=0
	for i in range (1,len(b)):
		suma=0
		for j in range (0,5):
			suma+=b[i][j]

		if suma<minimo:
			minimo=suma
			minindice=i

	print ("El ganador es",a[minindice])

ganador(nombres,tiempo)

def ganador_etapa(a,b,c):

	minimo=b[0][c-1]
	minindice=0
	

	for i in range (1,len(a)):
		h=b[i][c-1]

		if h<minimo:
			minimo=h
			minindice=i

	print ("El ganador de la etapa",c,"es",a[minindice])
ganador_etapa(nombres,tiempo,3)

def ganador_cada_etapa(a,b):
	for j in range (0,5):
		minimo=b[0][j]
		minindice=0
		for i in range (1,len(b)):
			h=b[i][j]

			if h<minimo:
				minimo=h
				minindice=i

		print ("El ganador de la etapa",j+1,"es",a[minindice])

ganador_cada_etapa(nombres,tiempo)




