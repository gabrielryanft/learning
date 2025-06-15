from math import factorial
from time import sleep
n = int(input('Digite um número: '))
f = factorial(n)
print('o número {}! (Fatorial) é {}.'.format(n, f))

print('Ou...')
sleep(1)

n1 = int(input('digite um número de novo: '))
c = n1
f1 = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c != 1 else ' = ', end='')
    f1 *= c
    c -= 1
print('{}'.format(f1))