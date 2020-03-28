def fact(x):
	t=1
	while x>0:
		t=t*x
		x=x-1

	if x==0:
		t=t*1

	return (t)
p=1
while p>0:

	n=int(input("Ingrese entero: "))

	print ("Su factorial es: ",fact(n))