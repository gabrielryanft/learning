n = int(input('Digite algum número: '))
print('  Escolha:\n   1 - binario;\n   2 - hexadecimal;\n   3 - octal.')
r = int(input('Escolha uma das opções acima: '))

if r == 1:
    print('  {} em binario é: {}.'.format(n, bin(n)[2:]))
elif r == 2:
    print('  {} em hexadecimal é: {}.'.format(n, hex(n)[2:]))
elif r == 3:
    print('  {} em octal é: {}.'.format(n, oct(n)[2:]))
else: 
    print('Vai se foder! te dei três opções, escolha uma delas(Sua mula!).')