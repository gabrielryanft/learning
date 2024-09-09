n1 = float(input('Digite a sua nota (0 - 10): '))
n2 = float(input('Digite outra nota (0 - 10): '))

if n1 or n2 > 10:
    print('Número invalido, Tente de novo.')
    if n1 > 10:
        print('O primeiro número({}) é maior que dez, digite um número menor ou igual a dez.'.format(n1))
    elif n2 > 10:
        print('O segundo número({}) é maior que dez, digite um número menor ou igual a dez.'.format(n2))
    else: print('Os dois números são maiores que dez, digite número menores ou iguais a dez.')
else:
    c = (n1 + n2) / 2
    cm = str(c).replace('.', ',')
    print('Sua nota é {}.'.format(cm))

    if (n1 + n2) / 2 == 10:
        print('Você passou com honras.')
    elif (n1 + n2) / 2 > 6:
        print('Você passou.')
    elif (n1 + n2) / 2 > 3:
        print('Você está de recuperação.')
    elif (n1 + n2) / 2 > 1:
        print('Você foi reprovado.')
    else: print('Você é burrão.')