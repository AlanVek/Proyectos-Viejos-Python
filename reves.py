def fraseReves ():
	entrada = (str(input("Dame la frase: ")))
	lista = []
	for n in entrada:
		lista += [n]
		lista.reverse()
	for f in lista:
		print(f,end="")
	return()


fraseReves()