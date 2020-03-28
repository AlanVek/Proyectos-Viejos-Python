max=[]
min=[]
mes=[]
for i in range (0,12):
		mesx=input("Ingrese mes: ")
		ma=int(input("Ingrese temperatura máxima: "))
		mi=int(input("Ingrese temperatura mínima: "))

		mes+=[mesx]
		max+=[ma]
		min+=[mi]

sumax=0
sumin=0
for i in range (0,12):
		sumax+=max[i]
		sumin+=min[i]

promax=sumax/12
promin=sumin/12

print ("El promedio de temperaturas máximas es: ",promax)
print ("El promedio de temperaturas mínimas es: ",promin)

dif=[]

for i in range (0,12):
		d=(abs(max[i]-min[i]))
		dif+=[[d,mes[i]]

print ("La lista de diferencias de temperatura por mes es: ",dif)

diforden=[]
for i in range (0,12):
		a=max(dif)
		dif.remove(a)
		diforden+=[a]

print ("Las diferencias de temperatura ordenadas de mayor a menor es: ",diforden)







