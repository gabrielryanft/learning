l = []
while True:
    n = int(input('Digite um número: '))
    if n in l:
        print('Valor já está na lista. Tente de novo.')
    else:
        l.append(n)
        r = str(input('quer continuar( S / N )? '))
        if r not in 'Ss':
            break
l.sort()
print(f'você digitou os valores {l}.')
#ou
l1 = l[:] # fazendo copia da lista
print(f'Você digitou os valores {sorted(l1)}')