from random import randint
v = p = 0
while True:
    n = int(input('Digite um número (Sair: N° negativo (Ex: -1)): '))
    if n < 0:
        break
    pi = str(input('Par ou impar( P / I )(Sair: Qualquer coisa menos P ou I)? '))
    if pi not in 'PpIi':
        break
    nc = randint(0, 10)
    nt = nc + n
    if n % 2 == 0 and pi in 'Pp' or n % 2 != 0 and pi in 'Ii':
        print(f'Você jogou {n} e o computador {nc}. O total é {nt}, você ganhou!')
        v += 1
    else:
        print(f'Você jogou {n} e o computador {nc}. O total é {nt}, você perdeu.')
        p += 1
pluralv = '' if v <= 1 else 'es'
pluralp = '' if p <= 1 else 'es'
naov = 'não ' if v == 0 else ''
naop = 'não ' if p == 0 else ''
v = v if v > 0 else 'nem uma'
p = p if p > 0 else 'nem uma'
print('Você saiu.')
print(f'Você {naov}ganhou {v} vez{pluralv} e {naop}perdeu {p} vez{pluralp}.')