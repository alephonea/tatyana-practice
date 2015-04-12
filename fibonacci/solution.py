
# solution module is a library module , the function is for fibonacci numbers.

def fibonacci(number):
	x=1
	y=2
	i=2
	z=0
	if number ==1:
		print 1
		return 1
	elif number==2:
		print 2
		return 2
	else:
		while i!=number:
			z=x+y
			x=y
			y=z
			i+=1
	return z
