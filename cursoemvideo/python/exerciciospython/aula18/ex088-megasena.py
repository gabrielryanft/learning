from random import randint
d, l = [], []
c, n = 0, int(input('Número de jogos: '))
while True:
    num = randint(1, 60)
    if num not in d:
        d.append(num)
        c += 1
    if len(d) == 6:
        l.append(d[:])
        d.clear()
    if len(l) == n:
        break
print('{:=^35}'.format(f' {n} jogos saindo! ')) #.center(30) centraliza a mensagem no meio de 30 espaços!
for p, b in enumerate(l):
    print(f'{p + 1}° jogo: {b}.')