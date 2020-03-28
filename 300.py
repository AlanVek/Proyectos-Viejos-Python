def orden_alfabetico(a):
	for i in range (0,len(a)-1):
		for j in range (i+1,len(a)):
			if a[i]<a[j]:
				aux=a[i]
				a[i]=a[j]
				a[j]=aux

	print ("La primera es: ",a[len(a)-1])
	print ("La última es: ",a[0])

a=input("Ingrese palabras, separadas por comas: ")

lista=a.split(",")

orden_alfabetico(lista)