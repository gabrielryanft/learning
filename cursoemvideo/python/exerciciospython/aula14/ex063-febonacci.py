try:
    n = int(input('Quer mostrar quantos números? '))
    if n <= 0:
        print('Valor invalido.')   
    elif n == 1:
        print('0')
    elif n == 2:
        print('0 - 1')
    else:
        c = 2
        f0 = 0
        f1 = 1
        print(f'{f0} - {f1} - ', end='')
        while c != n:
            f2 = f0 + f1
            print(f'{f2} - ' if c < n - 1 else f'{f2}', end='')
            f0, f1 = f1, f2
            c += 1
except TypeError:
    print('Valor invalido.')