def comunlistas (a=[None],b=[None]):
	lista=[]
	for i in range (0,len(a)):
		for j in range (0,len(b)):
			if a[i]==b[j]:
				pert=False
				for t in range (0,len(lista)):
					if a[i]==lista[t]:
						pert=True
				if pert==False:
					lista+=[a[i]]

	print(lista)


comunlistas()