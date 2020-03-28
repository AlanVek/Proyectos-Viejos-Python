def nomlet(a,b):
	lista=[]
	for i in range (0,len(a)):
		if a[i][0]==b:
			lista+=[a[i]]

	print (lista)


nomlet(["Alan","Marcos","Pablo","Aníbal"],"A")