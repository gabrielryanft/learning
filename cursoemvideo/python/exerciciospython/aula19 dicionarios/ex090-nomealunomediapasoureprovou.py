d = dict()
d['nome'] = str(input('Nome: '))
d['nota'] = float(input(f'Média de {d["nome"]}: '))
if d['nota'] > 6:
    d['situacao'] = 'passado'
elif d['nota'] > 4:
    d['situacao'] = 'recuperação'
else: d['situacao'] = 'reprovou'
for t, i in d.items():
    print(f'{t.title() if t != "situacao" else "situação"} é {i}.')