print ("This is the game:")
print ("I give you a sequence and you have to tell me whether it's True or False.")
print ("If you guess, you win. If you don't, then I win.")
n=input("Are you ready? Type 'yes' or 'no': ")

while n!="yes" and n!="no":
	n=input("You didn't answer correctly, bastard. Are you ready or not? It's not that hard: ")

if n=="yes":
	print ("The sequence is:")
	print ("((3==4) or 3%2==1) and (pi<1 or ((7+9==(4^2)))")
	a=input("Type your answer, little bastard: ")

	if a=="True" or a=="true":
		print ("Good job, little bastard. You win the game. Goodbye.")
	if a=="False" or a=="false":
		print ("You had one job, bastard. And you blew it. You LOSE. See you next time.")

if n=="no":
	print ("Goodbye. Hope you die.")


