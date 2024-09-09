v = int(input('Qual o valor que você quer retirar: '))
c = 50
t = 0
while True:
    if v >= c:
        v -= c
        t += 1
    else: 
        if t > 0:
            if c == 1:
                print(f'{t} moedas de R${c}.')
            else: print(f'{t} notas de R${c}.')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t = 0
        if v == 0: break