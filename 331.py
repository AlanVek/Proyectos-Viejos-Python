def inverso(a):
	lista=[]
	for i in range (len(a)-1,-1,-1):
		lista+=[a[i]]

	print (lista)


a=[9,8,7,6,5,4,3,2,1]
inverso(a)
print (a)

