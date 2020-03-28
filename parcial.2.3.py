def leerpalabras(lista):
	listapal=[]
	p=""
	for i in range (0,len(lista)):
		for j in range (0,len(lista[i])):
			if lista[i][j]!="*":
				p+=lista[i][j]
			else:
				if p!="" and len(p)>=2:
					listapal+=[p]
				p=""
			if int(j)==len(lista[i])-1:
				if len(p)>=2:
					listapal+=[p]
				p=""

	for j in range (0,len(lista[i])):
		for i in range (0,len(lista)):
			if lista[i][j]!="*":
				p+=lista[i][j]
			else:
				if p!="" and len(p)>=2:
					listapal+=[p]
				p=""
			if int(i)==len(lista)-1:
				if len(p)>=2:
					listapal+=[p]
				p=""

	print (listapal)

leerpalabras([["*","H","O","L","A","*","R"],["C","*","T","E","*","L","A",],["A","T","R","I","L","*","P"],["E","*","O","*","U","P","A"],["S","O","S","*","Z","A","R"]])