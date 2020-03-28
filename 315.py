def primo(a):
	primo=True
	for i in range (2,a):
		if a%i==0:
			primo=False
			break

	if primo:
		return (True)
	else:
		return (False)


def primlista(a):
	lista=[]

	for i in range (0,len(a)):
		if primo(a[i])==True:
			lista+=[a[i]]

	print (lista)

primlista([3,5,6,8,12,23,13,15,7])
