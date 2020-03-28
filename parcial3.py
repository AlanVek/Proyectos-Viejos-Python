def mostrarcru(a):
	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			print (a[i][j],end=" ")
		print()

def leercru(a):
	p=""
	listapal=[]
	for i in range (0,len(a)):
		for j in range (0,len(a[0])):
			if a[i][j]=="*":
				if len(p)>=2:
					listapal+=[p]
					p=""
				else:
					p=""
			else:

				if j==(len(a[0])-1):
					if len(p)>=1:
						p+=a[i][j]
						listapal+=[p]
						p=""
					else:
						p=""
												
				else:
					p+=a[i][j]
	p=""
	for j in range (0,len(a[0])):
		for i in range (0,len(a)):
			if a[i][j]=="*":
				if len(p)>=2:
					listapal+=[p]
					p=""
				else:
					p=""
			else:
				if i==len(a)-1:
					if len(p)>=1:
						p+=a[i][j]
						listapal+=[p]
						p=""
					else:
						p=""
				else:
					p+=a[i][j]
	return (listapal)

cruci=[["*","H","O","L","A","*","R"],["C","*","T","E","*","L","A"],["A","T","R","I","L","*","P"],["E","*","O","*","U","P","A"],["S","O","S","*","Z","A","R"]]

print(leercru(cruci))