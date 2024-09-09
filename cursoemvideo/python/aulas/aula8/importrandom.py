import math
import random 

n = int(input('Digite um número. '))
raizq = math.sqrt(n)
aleat01 = random.random()
aleat110 = random.randint(1, 10)

print('A raiz quadrada de {} é {:.2f}.Toma um número aleatório de 0 a 1 com 2 casas decimais aí: {:.2f}, e um número aleatorio de 1 a 10: {}.'.format(n, raizq, aleat01, aleat110))