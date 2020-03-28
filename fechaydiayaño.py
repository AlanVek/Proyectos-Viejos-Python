opcion=""

while opcion!="b":
	print ("Seleccione una de las siguientes opciones:")
	print ("a) Introducir fecha para obtener día.")
	print ("b) Cerrar el programa.")
	opcion=input("Introduzca la opción elegida: ")



	if opcion=="a":
		try:
			b=int(input("Ingrese número de día: "))
			a=int(input("Ingrese número de mes: "))
			c=int(input("Ingrese año: "))

			while (c%4)!=0 and b==29 and a==2:
				c=int(input("Este año no tiene 29 de febrero. Ingrese otro año: "))

			while 12<a or a<=0:
				a=int(input("El mes debe ser un número entre 1 y 12. Ingrese otro mes: "))
			while 31<b or b<=0:
				b=int(input("El día debe ser un número entre 1 y 31. Ingrese otro día: "))
			while c<2018:
				c= int(input("El año debe ser mayor o igual a 2018. Ingrese otro año: "))
			while (a==2 or a==4 or a==6 or a==9 or a==9 or a==11) and b>=31:
				b=int(input("El mes ingresado tiene 30 días. Ingrese de nuevo el día: "))
			while a==2 and b>=30:
				b=int(input("Febrero no tiene más de 28 ó 29 días, dependiendo del año. Ingrese de nuevo el día: ")) 

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

			num_dia=(mes+b)+(c-2018)

			i=2018
			if a>2:
				while i<=c:
					if i%4==0:
						num_dia=num_dia+1
					i=i+1
			else:
				while i<c:
					if i%4==0:
						num_dia=num_dia+1

					i=i+1
	
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


			print ("El",b,"del",a,"del",c,"es, fue o será",dia,"- Gracias por usar el programa.")

		except:
			print ("Ha ingresado un dato incorrecto.  El programa se cerrará. Inténtelo de nuevo.")

		if opcion!="a":
			opcion=input("No ha ingresado una opción correcta. Inténtelo de nuevo: ")
			
print ("Gracias por usar el programa.")