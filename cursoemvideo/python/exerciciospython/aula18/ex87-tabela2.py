l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for b in range(0, 3):
    for i in range(0, 3):
        l[b][i] = int(input('Digite um número: '))
for b in range(0, 3):
    for i in range(0,3):
        print(f'[{l[b][i]:^5}]', end='')
    print()
tp = t3 = 0
for b in l:
    for i in b:
        if i % 2 == 0:
            tp += i
for c in range(0, 3):
    t3 += l[c][2]
print(f'A soma de todos os valores pares é: {tp}.')
print(f'A soma de todos os valores da 3° coluna é: {t3}.')
print(f'O maior valor da seginda linha é: {max(l[1])}.')