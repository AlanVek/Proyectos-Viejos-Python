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

num_dia=mes+b

if (num_dia-1)%7==0:
	dia="lunes"
if (num_dia-2)%7==0:
	dia="martes"
if (num_dia-3)%7==0:
	dia="miércoles"
if (num_dia-4)%7==0:
	dia="jueves"
if (num_dia-5)%7==0:
	dia="viernes"
if (num_dia-6)%7==0:
	dia="sábado"
if (num_dia-7)%7==0:
	dia="domingo"

print ("El número de día es",num_dia,"y en 2018 cae",dia)
