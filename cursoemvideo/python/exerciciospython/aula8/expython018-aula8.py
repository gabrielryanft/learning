from math import radians, sin, cos, tan

a = float(input('Digite um ângulo: '))

seno = sin(radians(a)) #radians converte os graus em radianos(pq é isso que ele asseita) ou algo do genero
coss = cos(radians(a))
tang = cos(radians(a))

print(' O seno é: {:.2f}; \n O cosseno é: {:.2f}; \n A tangente é: {:.2f}.'.format(seno, coss, tang))