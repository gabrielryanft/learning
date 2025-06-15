import random
n = str(input('Digite um nome: '))
no = str(input('Digite um nome: '))
nom = str(input('Digite um nome: '))
nome = str(input('Digite um nome: '))

l = [n, no, nom, nome]

e = random.choice(l)

print('O gostosão é o : {}!!!'.format(e))
