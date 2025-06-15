r = s = c = 0
r = int(input('Digite um número: '))
while r != 999:
    s += r
    c += 1
    r = int(input('Digite um número: '))
print(f'Você digitou {c}. E a soma deles é {s}.')