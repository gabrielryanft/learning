l = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: {l}')
print(f'O valor nove apareceu {l.count(9)} vezes.')
if 3 in l:
    print(f'O valor tês apareceu na posição {l.index(3) + 1}.')
else: print('O três não foi digitado nem uma vez.')
print('Valores pares: ', end='')
for n in l:
    if n % 2 == 0:
        print(f'{n},', end='')