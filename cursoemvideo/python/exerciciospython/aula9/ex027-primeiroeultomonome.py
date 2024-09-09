n = str(input('Digite o seu nome: '))
nl = n.split() #transforma o nome em uma lista.

print('Olá, {}!'.format(n.title()))
print('Primeiro nome: {}.'.format(nl[0].title()))
print('Último nome: {}.'.format(nl[len(nl) - 1].title()))