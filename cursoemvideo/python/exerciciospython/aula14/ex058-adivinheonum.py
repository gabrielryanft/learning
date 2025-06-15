from random import randint
nc = randint(1, 10)
np = int(input('Eu escolhi um número entre 1 e 10.\n Tente adivinha-lo. Digite um número: '))
while np != nc:
    if np < nc:
        np = int(input('A resposta é um número MAIOR. Tente de novo: '))
    else: np = int(input('A resposta é um número MENOR. Tente de novo: '))
print('Acertou! A resposta é {}!'.format(nc))