from random import randint
l = ('Papel', 'Pedra', 'Tesoura')
print('Escolhas:\n[ 1 ] Papel;\n[ 2 ] Pedra\n[ 3 ] Tesoura.')
e = int(input('Sua escolha: '))
c = randint(0, 2)
if e == 0 or e > 3:
    print('Tente um valor válido.')
else:
    print('-H-' * 3)
    print('Você jogou: {}'.format(l[e - 1]))
    print('computador jogou: {}'.format(l[c]))
    print('-H-' * 3)
    if c == 0: #papel
        if e == 1: #papel
            print('Empatou.')
        elif e == 2:#pedra
            print('Você perdeu.')
        elif e == 3:#tesoura
            print('Você ganhou.')
    elif c == 1: #pedra
        if e == 1: #papel
             print('Você ganhou.')
        elif e == 2:#pedra
            print('Empatou.')
        elif e == 3:#tesoura
            print('Você perdeu.')
    elif c == 2: #tesoura
        if e == 1: #papel
            print('Você perdeu.')
        elif e == 2:#pedra
             print('Você ganhou.')
        elif e == 3:#tesoura
            print('Empatou.')