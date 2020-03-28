from math import*

largo= float(input("Ingrese largo de cabeza: "))
ancho= float(input("Ingrese ancho de cabeza: "))
sup= float(input("Ingrese largo de parte superior a pupilas: "))
nac_cabello= float(input("Ingrese largo de nacimiento de cabello a pupilas: "))
nariz= float(input("Ingrese largo de nariz a mentón: "))
labios= float(input("Ingrese largo de labios a mentón: "))
pupla= float(input("Ingrese largo de pupila a labios: "))
pupna= float(input("Ingrese largo de pupilas a nariz: "))
lab= float(input("Ingrese largo de labios: "))
nar= float(input("Ingrese ancho de nariz: "))
pelo= input("Ingrese color de pelo: ")
ojos= input("Ingrese color de ojos: ")
sexo= input("Ingrese sexo (F o M): ")

if largo<=0 or ancho<=0 or sup<=0 or nac_cabello<=0 or nariz<=0 or labios<=0 or pupla<=0 or pupna<=0 or lab<=0 or nar<=0:
	print ("Los valores ingresados deben ser mayores a cero.")

if (sexo=="F" or sexo=="f" or sexo=="M" or sexo=="m") and (pelo=="rubio" or pelo=="Rubio" or pelo=="negro" or pelo=="Negro" or pelo=="Castaño" or pelo=="castaño" or pelo=="Rojo" or pelo=="rojo") and (ojos=="Marrones" or ojos=="marrones" or ojos=="Marrón" or ojos=="marrón" or ojos=="marron" or ojos=="Marron" or ojos=="Verdes" or ojos=="Verde" or ojos=="verde" or ojos=="verdes" or ojos=="Azul" or ojos=="azul" or ojos=="azules" or ojos=="Azules"):
	if sexo=="F" or sexo=="f":
		if pelo=="rubio" or pelo=="Rubio":
			pelo=0.39
		else:
			if pelo=="negro" or pelo=="Negro" or pelo=="Castaño" or pelo=="castaño":
				pelo=0.26
			if pelo=="rojo" or pelo=="Rojo":
				pelo=0.09
	else:
			if pelo=="rubio" or pelo=="Rubio":
				pelo=0.275
			if pelo=="negro" or pelo=="Negro":
				pelo=0.35
			if pelo=="Castaño" or pelo=="castaño":
				pelo=0.3
			if pelo=="Rojo" or pelo=="rojo":
				pelo=0.075
		
	if ojos=="Azul" or ojos=="azul" or ojos=="azules" or ojos=="Azules":
		ojos=0.34
	if ojos=="Marrones" or ojos=="marrones" or ojos=="Marrón" or ojos=="marrón" or ojos=="marron" or ojos=="Marron":
		ojos=0.19
	if ojos=="Verdes" or ojos=="Verde" or ojos=="verde" or ojos=="verdes":
		ojos=0.14
		
	indice=(((largo/ancho)+(sup/nac_cabello)+(nariz/labios)+(nac_cabello/pupna)+(pupla/pupna)+(lab/nar))/6)*pelo*ojos
	print ("Su índice de belleza es: ", indice)		
	
else:
	if (pelo!="rubio" and pelo!="Rubio" and pelo!="negro" and pelo!="Negro" and pelo!="Castaño" and pelo!="castaño" and pelo!="Rojo" and pelo!="rojo"):
		print ("No ingresó un color de pelo válido.")

	if sexo!="F" and sexo!="f" and sexo!="M" and sexo!="m":
		print ("No ingresó un sexo válido.") 

	if ojos!="Marrones" and ojos!="marrones" and ojos!="Marrón" and ojos!="marrón" and ojos!="marron" and ojos!="Marron" and ojos!="Verdes" and ojos!="Verde" and ojos!="verde" and ojos!="verdes" and ojos!="Azul" and ojos!="azul" and ojos!="azules" and ojos!="Azules":
		print ("No ingresó un color de ojos válido.")


	
