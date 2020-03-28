from math import*
def cuadratica(a,b,c):
	if a!=0:
		if b**2-4*a*c>=0:

			raiz=sqrt(b**2-4*a*c)

			sol1=(-b+raiz)/(2*a)
			sol2=(-b-raiz)/(2*a)

			lista=[sol1,sol2]
			print (lista)
		else:
			print ([None,None])

	if a==0:
		if b==0:
			print ([None,None])
		else:
			if c==0:
				print ([0,0])
			else:
				print ([-c/b,-c/b])

cuadratica(1,0,1)
cuadratica(3,-5,2)
cuadratica(0,2,-4)
cuadratica(0,3,0)
cuadratica(0,0,2)