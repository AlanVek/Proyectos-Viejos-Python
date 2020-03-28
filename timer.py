import threading
import time
def f():
	print ("Hola")
t=threading.Timer(5,f)
t.start()

if t==4.5:
	t.cancel()