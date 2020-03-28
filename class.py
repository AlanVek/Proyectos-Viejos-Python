from math import*
import numbers

try:
	n=float(input("Ingrese número: "))
	if isinstance(n,numbers.Number)==True:
		print ("Es número.")
except: 
	print ("No es número.")