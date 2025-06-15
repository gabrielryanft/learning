from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
o = 'Gabriel totoso'
while o != 0:
    print('''Ecolha uma opção:
        [ 1 ] Somar;
        [ 2 ] Multiplicar;
        [ 3 ] Maior;
        [ 4 ] Novos números;
        [ 0 ] Sair.''')
    o = int(input('Sua opção: '))
    if o == 1:
        rec = 'Calculando'
        print('\r' + rec, end='')
        sleep(0.6)
        rec = 'Calculando.'
        print('\r' + rec, end='')
        sleep(0.7)
        rec = 'Calculando..'
        print('\r' + rec, end='')
        sleep(0.8)
        rec = 'Calculando...'
        print('\r' + rec)
        sleep(0.9)
        print('{} + {} = {}'.format(n1, n2 , n1 + n2))
    elif o == 2:
        rec = 'Calculando'
        print('\r' + rec, end='')
        sleep(0.6)
        rec = 'Calculando.'
        print('\r' + rec, end='')
        sleep(0.7)
        rec = 'Calculando..'
        print('\r' + rec, end='')
        sleep(0.8)
        rec = 'Calculando...'
        print('\r' + rec)
        sleep(0.9)
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif o == 3:
        rec = 'Calculando'
        print('\r' + rec, end='')
        sleep(0.6)
        rec = 'Calculando.'
        print('\r' + rec, end='')
        sleep(0.7)
        rec = 'Calculando..'
        print('\r' + rec, end='')
        sleep(0.8)
        rec = 'Calculando...'
        print('\r' + rec)
        sleep(0.9)
        if n1 > n2:
            print('O primeiro número ({}) é maior.'.format(n1))
        else: print('O segundo número ({}) é maior.'.format(n2))
    elif o == 4:
        rec = 'Recomeçando'
        print('\r' + rec, end='')
        sleep(0.6)
        rec = 'Recomeçando.'
        print('\r' + rec, end='')
        sleep(0.7)
        rec = 'Recomeçando..'
        print('\r' + rec, end='')
        sleep(0.8)
        rec = 'Recomeçando...'
        print('\r' + rec)
        sleep(0.9)
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
rec = 'Saindo'
print('\r' + rec, end='')
sleep(0.6)
rec = 'Saindo.'
print('\r' + rec, end='')
sleep(0.7)
rec = 'Saindo..'
print('\r' + rec, end='')
sleep(0.8)
rec = 'Saindo...'
print('\r' + rec)
sleep(0.9)