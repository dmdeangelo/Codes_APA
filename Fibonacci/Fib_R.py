# Fibonacci Recursivo

#Importando biblioteca para medição de tempo
import time

#Base de recursão
def fib_r(position):	
	
	if(position == 0):
		return 0
	elif(position == 1):
		return 1
	else:
		return fib_r(position - 1) + fib_r(position - 2)


#Chamada

for x in range(0, 101):

	#Iniciando contagem de tempo
	start = time.time()
	
	#Pegando o resultado
	res = fib_r(x)
	
	#Parando a contagem de tempo
	end = time.time()

	#Dando a saída para o usuário
	print(x, " ", res, " ", end - start, " ", )
