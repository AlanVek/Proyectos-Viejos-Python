b=int(input("Ingrese número del primer día: "))
a=int(input("Ingrese número del primer mes: "))
c=int(input("Ingrese número del segundo día: "))
d= int(input("Ingrese número del segundo mes: "))

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
if d==1:
	mes2=0
if d==2:
	mes2=31
if d==3:
	mes2=59	
if d==4:
	mes2=90
if d==5:
	mes2=120
if d==6:
	mes2=151
if d==7:
	mes2=181
if d==8:
	mes2=212
if d==9:
	mes2=243	
if d==10:
	mes2=273
if d==11:
	mes2=304
if d==12:
	mes2=334

print ("El número de día del año es: ", abs((mes+b)-(mes2+c)))
