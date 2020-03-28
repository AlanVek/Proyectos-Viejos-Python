b=int(input("Ingrese número de día: "))
a=int(input("Ingrese número de mes: "))

if a==1:
	mes=0
if a==2:
	mes=31
if a==3:
	mes=59	
if a==4:
	mes=90
if a==5:
	mes=120
if a==6:
	mes=151
if a==7:
	mes=181
if a==8:
	mes=212
if a==9:
	mes=243	
if a==10:
	mes=273
if a==11:
	mes=304
if a==12:
	mes=334

print ("El número de día del año es: ", mes+b)
