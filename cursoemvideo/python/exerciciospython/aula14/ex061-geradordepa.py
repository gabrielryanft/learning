n = int(input('Digite um número: '))
r = int(input('razão: '))
c = 10
while c >= 0:
    print(f' {n} -' if c > 0 else f' {n}  Acabou!', end='')
    n += r
    c -= 1