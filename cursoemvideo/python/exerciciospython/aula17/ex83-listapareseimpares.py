l, par, imp = [], [], []
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    r = str(input('quer continuar? '))
    if r in 'Nn':
        break
print(f'A lista completa é: {l}.')
for c in l:
    if c % 2 == 0:
        par.append(c)
    else: imp.append(c)
imp = imp if len(imp) > 0 else 'Nem um'
par = par if len(par) > 0 else 'Nem um'
print(f'Os valores impares são: {imp}.')
print(f'Os valores impares são: {par}.')