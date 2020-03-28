print ("Welcome to the game.")

print("Select a number and I'll tell you whether it's odd or even.")

def f(x):
	if x%2==0:
		print ("The number is even.")
	else:
		if x%2==1:
			print ("The number is odd.")
		else:
			print ("You didn´t type an integer, you bastard.")


i=0
while i<1:
	e=input("If you want to leave, press any key. If you want to stay, just press 'enter': ")
	if e=="":
		try:
			n=float(input("Enter your number: "))
			f(n)
		except:
			print ("You had to enter a number, bastard. Try again.")
	else:
		break


print ("Thank you, goodbye and come back any time.")