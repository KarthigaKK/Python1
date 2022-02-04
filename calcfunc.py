def add(x,y):
	return x+y 


#print(add(3,4))

def sub(x,y):
	return x-y 


def multiply(x,y):
	return x*y 

def divide(x,y):
	if y == 0:
		raise ValueError("Can't divide by Zero!")
	return x/y