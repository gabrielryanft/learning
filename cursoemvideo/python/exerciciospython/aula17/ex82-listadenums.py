l = list()
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    r = str(input('Quer continuar? '))
    if r in 'Nn':
        break
print(f'O total de números digitados foi {len(l)}.')
print(f'A lista em ordem decrescente é {sorted(l, reverse=True)}.') #sorted(l, reverse=True)  deixa a lista sorted e ao contrario, ou seja em ordem decrescente. também seria possival fazer l.sort(reverse=True) da no mesmo.
print('Na lista tem 5.' if 5 in l else 'Na lista não tem 5.')