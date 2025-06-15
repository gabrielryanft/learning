li = ('cachorro', 'gato', 'menta', 'dedo', 'mesa', 'roteador', 'dentro', 'fora', 'dentro', 'não', 'sim', 'para')
for p in li:
    c = 0
    v = []
    for l in p:
        if l.lower() in 'aeiou':
            v.append(l)
            c += 1
    print(f'Há {c} vogais em "{p.title()}". Elas são: {v}')

  