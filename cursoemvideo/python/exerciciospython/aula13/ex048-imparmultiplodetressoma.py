ns = []
nn = 0
ni = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        ns.append(str(c)) #append cria um item na lista
        nn = nn + c
        ni = ni + 1
ns[-1] += ' ='
l = ' + '.join(ns) #join = unir todos os elementos da lista(com o sinal de adiçãoa(' + '))
print(l, nn, '(Nesse calculo foram somados {} valores.)'.format(ni)) #tiva que usar a virgula para concatenar o num com a str