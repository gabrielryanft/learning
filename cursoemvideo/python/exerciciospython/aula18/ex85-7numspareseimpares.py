l = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        l[0].append(n)
    else: l[1].append(n)

print(f'Todos os valores são: {l}')
print(f'Os números impares: {sorted(l[1])}')
print(f'Os números pares: {sorted(l[0])}')