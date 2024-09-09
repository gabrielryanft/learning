s = 0
sp = 0
np = 0
si = 0
ni = 0
for p in range(1, 7):
    n = int(input('Digite o {}° número: '.format(p)))
    s += n
    if n % 2 == 0:
        sp += n
        np += 1
    elif n % 2 != 0:
        si += n
        ni += 1
print('A soma de todos os números é: {}'.format(s))
print('A soma de todos os números pares(São {}) é: {}'.format(np, sp))
print('A soma de todos os números ímpares(São {}) é: {}'.format(ni, si))