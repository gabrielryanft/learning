t, l = [], []
while True:
    t.append(str(input('Nome: ')))
    t.append(float(input('Peso: ')))
    l.append(t[:])
    if len(l) == 1:
        pe = le = t[1]
        pp, pl = [], [] 
    else:
        if t[1] > pe:
            pe = t[1]
        if t[1] < le:
            le = t[1]
    t.clear()
    r = str(input('Quer continuar( S / N )? '))
    if r in 'Nn':
        break
for i in l:
    if i[1] == pe:
        pp.append(i[0])
    if i[1] == le:
        pl.append(i[0])
print(f'há {len(l)} pessoas na lista.')
print(f'O maior peso foi de {pe}. Pertencentes a: {pp}.')
print(f'O menor peso foi de {le}. pertencentes a: {pl}.')