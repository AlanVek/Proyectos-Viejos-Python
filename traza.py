def traza(a):
	if range (0,len(a))==range (0,len(a[0])):
		suma=0

		for i in range (0,len(a)):
			for j in range (0,len(a[i])):
				if i==j:
					suma+=a[i][j]

		return (suma)

	else:
		return (None)


print(traza ([[1,2,3],[3,4,5],[7,8,9]]))
print(traza ([[1,2],[3,4],[5,6]]))