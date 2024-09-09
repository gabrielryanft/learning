f = str(input('Digite uma frase ou uma palavra: ')).strip().upper()
p = f.split() # tira todos os espaços.
pj = ''.join(p)
pjc = ''
for pos in range(len(pj) - 1, -1, -1): #segundo -1 significa o caracter ates do primeiro. e o terceiro significa que é para volfta de 1 em 1.
    pjc += pj[pos]
print('Você escreveu : {}, ao contrario é: {}.'.format(pj, pjc))
if pjc == pj:
    print('Você tem um palindromo.')
else: print('Você não tem um palindromo.')
