import random

n = str(input('O nome de um aluno: '))
no = str(input('O nome de outro aluno: '))
nom = str(input('O nome de outro aluno: '))
nome = str(input('O nome de outro aluno: '))

lista = [n, no, nom, nome]
random.shuffle(lista)

print('A ordem será: {}.'.format(','.join(lista)))