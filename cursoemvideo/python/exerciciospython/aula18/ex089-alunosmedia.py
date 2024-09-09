na = 1
l, t = [], []
while True:
    print('{:=^30}'.format(f' Aluno N° {na}: '))
    n = str(input('Nome do aluno: ')).title()
    n1 = float(input('1° nota do aluno: '))
    n2 = float(input('2° nota do aluno: '))
    m = (n1 + n2) / 2
    t.append(n)
    t.append(n1)
    t.append(n2)
    t.append(m)
    l.append(t[:])
    t.clear()
    r = str(input('Continuar( S / N )? '))
    if r in 'Nn':
        break
    na += 1
print(f'{"N°":<6}{"Nome":<20}{"Média":>7}')
for c, a in enumerate(l):
    if c % 2 == 0:
        print(f'\033[40m{c + 1:<6}{str(a[0])[:16] + "..." if len(a[0]) >= 16 else a[0]:<20}{a[3]:>7}  \033[m')
    else:
        print(f'\033[7;40m{c + 1:<6}{str(a[0])[:16] + "...":<20}{a[3]:>7}  \033[m')
while True:
    a = int(input('Quer ver a nota de qual aluno (Digite o N° dele.)( 999 p/ sair )? '))
    if a == 999:
        break
    print(f'\033[32m{l[a - 1][0]}\033[m' + f' tirou a média {l[a - 1][3]}, com as notas {l[a - 1][1]} e {l[a - 1][2]}.')
print('Tchau!')