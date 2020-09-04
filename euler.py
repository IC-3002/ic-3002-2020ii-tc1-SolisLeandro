def e_cuadratica(n):
	# Implemente esta función
	if n < 0:
		return -1
	elif n == 0:
		return 1
	elif n == 1:
		return 2
	else:
		acum=2
		for i in range(2,n+1):
			acum+=(1/factorial(i))
	return acum
	
def e_lineal(n):
	# Implemente esta función

	if n < 0:
		return -1
	elif n == 0:
		return 1
	elif n == 1:
		return 2
	else:
		acum=2
		fact=2
		for i in range(2,n+1):
			acum+=(1/fact)
			fact*=i+1
	return acum
	return 0
    
def factorial(n):
	fact = 1
	if n > 0:
   		for i in range(1,n + 1):
   			fact = fact*i
	return fact
