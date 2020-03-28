def ayb(a,b):
	p=""
	lista=[]
	
	for j in range (0,len(b)):
		if p.find(str(b[j]))==-1:
			p+=str(b[j])
			
	for i in range (0,len(a)):
		if p.find(str(a[i]))==-1:
			p+=str(a[i])
			lista+=[a[i]]
	
	for i in range (0,len(lista)-1):
		for j in range (i+1,len(lista)):
			if lista[i]<lista[j]:
				aux=lista[i]
				lista[i]=lista[j]
				lista[j]=aux
	print (lista)


ayb([3,4,5,2,2,1,3],[6,2,3,3,1])

ayb([5,6,3,2,6,6,6,6],[6])