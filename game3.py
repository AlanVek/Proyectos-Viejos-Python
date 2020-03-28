import time

print ("El juego es el siguiente: ")
print ("Me das una secuencia de la cantidad de números enteros que elijas y yo te devuelvo otra secuencia con los mismos números pero de menor a mayor.")
print ("Aunque...")
print ("...quizás la lista tenga un valor cambiado.")
print ("Sólo tenés 10 segundos para decidir si hay un valor diferente o no.")
print ("Si creés que la lista que te doy es la misma que me diste, poné 'True'. Si no, poné 'False'.")
print ("Si adivinaste y tardaste menos de 10 segundos, ganás. Si no adivinaste y/o si tardaste más de 10 segundos, perdés.")
n= input("¿Estás list@? Poné 'si' o 'no': ")

while n!="si" and n!="no":
	n=input("¿Estás list@ o no? No ingresaste un valor válido. Intentá de nuevo: ")

while n=="si":
	try:
		p=int(input("¿Con cuántos números querés jugar?: "))
	except:
		try:
			p=int(input("Tenés que ingresar un número entero. Intentalo de nuevo: "))
		except:
			print("Ha habido demasiados errores. El programa se cerrará. Adiós.")
			break

	if p<=0:
		print ("¿Estás chistos@? Intentá de nuevo. ")
	else: 
		try:
			x=int(input("Ingresá un número: "))
			
			lista=[x]

			for i in range (0,p-1):
				z=int(input("Ingresá un número: "))
				
				lista2=[z]
				lista+=lista2
		except:
			try:
				print ("Tenés que ingresar números enteros. Intentalo de nuevo: ")
				x=int(input("Ingresá un número: "))
				
				lista=[x]

				for i in range (0,p-1):
					z=int(input("Ingresá un número: "))
					lista2=[z]
					lista+=lista2
			except:
				print("Ha habido demasiados ingresos con error. El programa se cerrará. Adiós.")
				break

		igual=True
		if ((max(lista)//2) in lista)==True and (max(lista)//2)!=(len(lista)//2):
			g=max(lista)//2
			t=len(lista)//2
			lista8=[t]
			lista+=lista8
			lista.remove(g)
			igual=False
		else:
			if (max(lista)-min(lista)) in lista==True and (max(lista)-min(lista))!=len(lista):
				g=max(lista)
				c=min(lista)
				d=g-c
				t=len(lista)
				lita9=[t]
				lista+=lista9
				lista.remove(d)
				igual=False
			else:
				if (max(lista)//min(lista)) in lista==True and (max(lista)//min(lista))!=len(lista):
					g=max(lista)
					c=min(lista)
					d=g//c
					t=len(lista)
					lista9=[t]
					lista+=lista9
					lista.remove(d)
					igual=False	
				else:
					suma=0
					for i in range (0,len(lista)):
						a=lista[i]
						suma=suma+a
					if 100<=suma:
						q=len(lista)**2
						lista99=[q]
						lista+=lista99
						lista.remove(lista[1])
						igual=False

		lista.sort()
		print (lista)

		start_time=time.time()
		r=input("Ingresá tu respuesta: ")
		end_time=time.time()
		elapsed_time=end_time-start_time

		if ((r=="True" or r=="true") and igual) and elapsed_time<=10:
			print ("¡Excelente! Ganaste el juego. La respuesta era 'True' y tardaste: ",elapsed_time,"segundos.")
		if ((r=="False" or r=="false") and not igual) and elapsed_time<=10:
			print ("¡Excelente! Ganaste el juego. La respuesta era 'False' y tardaste: ",elapsed_time,"segundos.")
		if (((r=="True" or r=="true") and not igual) or ((r=="False" or r=="false") and igual)) and elapsed_time<=10:
			print ("¡Qué mal! Perdiste el juego. Tardaste",elapsed_time,"segundos pero tu respuesta fue incorrecta.")
		if ((r=="True" or r=="true") and igual) and elapsed_time>10:
			print ("¡Qué mal! Perdiste el juego. Tu respuesta fue correcta pero tardaste: ",elapsed_time,"segundos.")
		if ((r=="False" or r=="false") and not igual) and elapsed_time>10:
			print ("¡Qué mal! Perdiste el juego. Tu respuesta fue correcta pero tardaste: ",elapsed_time,"segundos.")
		if (((r=="True" or r=="true") and not igual) or ((r=="False" or r=="false") and igual)) and elapsed_time>10:
			print ("¡Qué mal! Perdiste el juego. Tu respuesta fue incorrecta y además tardaste: ",elapsed_time,"segundos.")

		n=input("¿Querés intentarlo de nuevo? Poné 'si' para continuar y 'no' para salir: ")

if n=="no":
	print ("Adiós.")