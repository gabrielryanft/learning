c = 1
pm = t = 0
while True:
    n = str(input('Nome do produto: ')).strip().title()
    p = float(input('Preço: R$'))
    if p < 0:
        p = float(input('Somente números positivos. Preço: R$'))
    if c == 1:
        pb = p
        nb = n
    else:
        if p < pb:
            pb = p
            nb = n
    if p > 999:
        pm += 1
    t += p
    co = str(input('Quer continuar( S / N )? '))
    if co in 'Nn':
        break
    c +=1
print(f'Praço total: {t}.')
print(f'Produto mais barato: {nb}.')
print(f'Produtos de R$1,000 ou mais: {pm}.')