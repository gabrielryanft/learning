n = t = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    t += n
    c += 1
print(f'A soma dos {c} números é {t}.')