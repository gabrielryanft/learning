n = int(input('Digite um número: '))
nnp = 0
for np in range(1, n + 1):
    if n % np == 0:
        print('\033[0;32m', end='')
        nnp += 1
    else: print('\033[0;37m', end='')
    print('{}'.format(np), end='\033[0;37m, ')
print('\033[0;37mO número {} foi divisivel por: {} números.'.format(n, nnp))
if nnp == 2:
    print('É um número primo.')
else: print('Não é um número primo.')