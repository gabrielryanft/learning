n1 = int(input('1 - Digite um número: '))
n2 = int(input('2 - Digite outro número: '))
n3 = int(input('3 - Digite outro outro número: '))

me = n1
n = 1
if n2 < n1 and n2 < n3:
    me = n2
    n = 2
if n3 < n1 and n3 < n2:
    me = n3
    n = 3

ma = n1
n0 = 1
if n2 > n1 and n2 > n3:
    ma = n2
    n0 = 2
if n3 > n1 and n3 > n2:
    ma = n3
    n0 = 3
print('-'*5 + '//' + '-'*5)
print('O menor é o {}. (O N° da {}° posição)'.format(me, n))
print('O maior é o {}. (O N° da {}° posição)'.format(ma, n0))
print('-'*5 + '//' + '-'*5)