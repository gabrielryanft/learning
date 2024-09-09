l = []
pmai = []
pmen = []
for c in range(0, 5):
    l.append(int(input(f'Digite o {c + 1}° número: ')))
    if c == 0:
        mai = men = l[c]
    else:
        if l[c] >= mai:
            mai = l[c]
        if l[c] <= men:
            men = l[c]
for n, v in enumerate(l):
    if v == mai:
        pmai.append(n + 1)
        pplumai = 'ões' if len(pmai) > 1 else 'ão'
        nplumai = 's' if len(pmai) > 1 else ''
    if v == men:
        pmen.append(n + 1)
        pplumen = 'ões' if len(pmai) > 1 else 'ão'
        nplumen = 's' if len(pmai) > 1 else ''
print(f'Você digitou os valores: {l}')
print(f'O maior valor é {mai} na{nplumai} posiç{pplumai}: {pmai}')
print(f'O menor valor é {men} na{nplumen} posiç{pplumai}: {pmen}')