def es_primo(n):
	primo=True
	for i in range (2,n):
		if n%i==0:
			primo=False
			break
			
	if primo==True:
		
		return(True)
	else:
		
		return (False)

def muestra_primo(n):
	for i in range (2,n):
		if es_primo(i)==True:
			print (i)

t=int(input("Ingrese número: "))

muestra_primo(t)