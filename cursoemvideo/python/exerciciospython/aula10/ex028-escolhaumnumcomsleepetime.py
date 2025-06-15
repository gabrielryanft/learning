from random import randint
nc = randint(0, 5)

from time import sleep #vejasobreissodepois

np = int(input('Digite um N° de 0 a 5: '))
print('Estou escolhendo um número...')
sleep(1.5)
if np == nc:
    print(' -=- Você acertou!')
else: print(' -=- Você errou, pensei em {}.'.format(nc))