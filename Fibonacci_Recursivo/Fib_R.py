# Fibonacci Recursivo

#Base de recursão
def fib_r(position):
	if(position == 0):
		return 0
	elif(position == 1):
		return 1
	else:
		return fib_r(position - 1) + fib_r(position - 2)


#Chamada
print(fib_r(20))
