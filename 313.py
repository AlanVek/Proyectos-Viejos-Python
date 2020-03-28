def impares(a):
	lista=[]
	for i in range (0,len(a)):
		if a[i]%2==1:
			lista+=[a[i]]

	print ([lista])


impares([5,4,6,8,7,13,12])