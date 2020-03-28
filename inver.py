from random import*
def ordenlista(a):

	n=randint(0,1)

	if n==0:

		for i in range (0,len(a)-1):
			for j in range (i+1,len(a)):
				if a[j]>a[i]:
					aux=a[i]
					a[i]=a[j]
					a[j]=aux

	if n==1:
		for i in range (0,len(a)-1):
			for j in range (i+1,len(a)):
				if a[j]<a[i]:
					aux=a[i]
					a[i]=a[j]
					a[j]=aux
	return (a)



print (ordenlista([4,7,2,5,3,1,6]))


