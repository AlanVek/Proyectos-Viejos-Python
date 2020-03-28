cadena=input("Ingrese cadena: ")
n=int(input("Ingrese cantidad de unidades a mover: "))

c=""

alfa="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
beta="abcdefghijklmnñopqrstuvwxyz"
num="0123456789"


for i in cadena:
	for t in alfa:
		if i==t:
			f=alfa.index(i)+n
			while f>len(alfa)-1:
				f=f-len(alfa)
			c+=alfa[f]
			
	for s in beta:
		if i==s:
			k=beta.index(s)+n
			while k>len(beta)-1:
				k=k-len(beta)			
			c+=beta[k]

	for h in num:
		if i==h:
			z=num.index(h)+n
			while z>len(num)-1:
				z=z-len(num)
			c+=num[z]
		

print (c)