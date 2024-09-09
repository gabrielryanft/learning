from math import sqrt, floor, ceil, trunc, pow, factorial

n = int(input('Digite um número: '))
raizq = sqrt(n)

print('A raiz quadrda de {} é {:.2f}'.format(n, raizq))
print('A raiz quadrada de {} aredondada para baixo é: {:.0f}.'.format(n, floor(raizq)))
print('A raiz quadrada de {} arredondada para cima é {:.0f}.'.format(n, ceil(raizq)))
print('A raiz quadrada de {} truncada é: {:.0f}.'.format(n, trunc(raizq)))
print('O número {} ao quadrado é: {}.'.format(n, pow(n, 2)))
print('O fatorial (n!) do número {} é: {}.'.format(n, factorial(n)))