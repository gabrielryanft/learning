n = int(input('Digite um número: '))
r = int(input('razão: '))
c = 10
cont = 0
while c > 0:
    cont += c
    while c > 0:
        print(f' {n} -' if c > 1 else f' {n}  Acabou?\n', end='')
        n += r
        c -= 1
    c = int(input('Quer que eu calcule mais quantos números (Digite 0 (Zero) para sair)? '))
print(f'Foram imprimodos {cont} valores.')