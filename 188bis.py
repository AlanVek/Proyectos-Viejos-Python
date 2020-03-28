cadena=input("Ingrese cadena: ")
n=int(input("Ingrese cantidad de unidades a mover: "))

c=""

alfa="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
beta="abcdefghijklmnñopqrstuvwxyz"
num="0123456789"


for i in range (0,len(cadena)):
	
	for t in range (0,len(alfa)):
		if cadena[i]==alfa[t]:
			f=t+n
			while f>len(alfa)-1:
				f=f-len(alfa)
			c+=alfa[f]
			
	for s in range (0,len(beta)):
		if cadena[i]==beta[s]:
			k=s+n
			while k>len(beta)-1:
				k=k-len(beta)			
			c+=beta[k]

	for h in range (0,len(num)):
		if cadena[i]==num[h]:
			z=h+n
			while z>len(num)-1:
				z=z-len(num)
			c+=num[z]
		

print (c)