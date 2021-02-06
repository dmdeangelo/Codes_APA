#Fibonacci Recursivo e Iterativo

#Importando biblioteca para medição de tempo
import time

#Fibonacci Recursivo
def fib_r(position):	
	
	if(position == 0):
		return 0
	elif(position == 1):
		return 1
	else:
		return fib_r(position - 1) + fib_r(position - 2)


#Fibonacci Iterativo
def fib_i(position):
	if(position == 0):
		return 0
	elif(position == 1):
		return 1
	else:
		first = 0
		second = 1
		value = 0

		for x in range(2, position + 1):
			value = first + second
			first = second
			second = value

		return value


#Chamada
for x in range(0, 101):

#Processo para dados com Recursão
	#Iniciando contagem de tempo
	start = time.time()
	
	#Pegando o resultado recursivo
	res1 = fib_r(x)
	
	#Parando a contagem de tempo
	end = time.time()

	#Pegando o tempo recursivo
	t1 = end - start


#Processo para dados com Iteração
	#Iniciando contagem de tempo
	start = time.time()
	
	#Pegando o resultado recursivo
	res2 = fib_i(x)
	
	#Parando a contagem de tempo
	end = time.time()

	#Pegando o tempo recursivo
	t2 = end - start

	#Dando a saída completa para o usuário
	#print(x, " ", res1, " ", res2 , " ", t1, " ", t2)

	#Dando a saída resumida para o usuário
	print(x, " ", res1, " ", t1, " ", t2)