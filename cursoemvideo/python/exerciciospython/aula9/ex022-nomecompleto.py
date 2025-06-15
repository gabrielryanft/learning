n = str(input('Qual é o seu nome(completo)? ')).strip() #strip() tira os espaços antes e depois de uma string.
print('Maiusculas: {}'.format(n.upper()))
print('Minusculas: {}'.format(n.lower()))
print('Número de letras: {}'.format(len(n) - n.count(' '))) #len(n)(= espaços.) -(= menos.) n.count(' ')(= conta os espaços(' ') que tem em n.)
print('Primeiro nome, N° de letras: {}'.format(n.find(' ')))#encontra o primeiro espaço da string e diz o indice do bgl(que por conhecidencia é o n de letras antes do primeiro espaço. ou seje o número de letras do primiro nome.)
s = n.split()
print('Primeiro nome, N° de letras(De um jeito diferente(Olha no codigo.).): {}'.format(len(s[0])))