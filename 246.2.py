def filcol(a):
	listafil=[]
	for i in range (0,len(a)):
		sumafil=0
		for j in range (0,len(a[i])):
			sumafil+=a[i][j]

		listafil+=[sumafil]
	listacol=[]
	for j in range (0,len(a[0])):
		sumacol=0
		for t in range (0,len(a)):
			sumacol+=a[t][j]

		listacol+=[sumacol]

	igual=False
	for i in range (0,len(listafil)):
		for j in range (0,len(listacol)):
			if listafil[i]==listacol[j]:
				print ("La fila",i+1,"suma lo mismo que la columna",j+1)
				igual=True

	if igual==False:
		print ("Ninguna columna suma lo mismo que ninguna fila.")


filcol([[1,2,3],[5,0,0],[0,1,3]])
filcol([[70,0,0],[1,1,0],[0,45,3]])






