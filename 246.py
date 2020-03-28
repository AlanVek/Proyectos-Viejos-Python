def filcol(a):
	
	for i in range (0,len(a)):
		sumafil=0
		for j in range (0,len(a[0])):
			sumafil+=a[i][j]
			
		for h in range (0,len(a[0])):
			sumacol=0
			for t in range (0,len(a)):
				sumacol+=a[t][j]
			if sumacol==sumafil:
				print ("Hay columnas y filas que suman lo mismo.")


filcol([[1,2,3],[75,0,0],[0,1,3]])






