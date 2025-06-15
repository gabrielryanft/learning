r = 's'
s = c = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        ma = me = n
    else:
        if ma < n:
            ma = n
        if me > n:
            me = n
    r = str(input('quer continuar( S / N )? '))
m = s / c
print(f'Você digitou {c} números;\nA média deles é {m};\nO maior é {ma} e o menor é {me}.')