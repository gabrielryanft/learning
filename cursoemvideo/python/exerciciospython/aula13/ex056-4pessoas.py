si = 0
m20 = 0
ihmv = 0
nhmv = ''
for n in range(1, 5):
    print('{}° pessoa:'.format(n))
    no = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    g = str(input('Gênero [ H / M ]: ')).strip()
    si += i
    if n == 1 and g in 'Hh': #g in 'Mm' verifica se o coiso ta no outro coiso.
        ihmv = i
        nhmv = no
    else:
        if g in 'Hh' and i > ihmv:
            ihmv = i
            nhmv = no
    if g in 'Mm' and i < 20:
        m20 += 1
        if m20 == 1:
            apenas = 'apenas 1'
            plural = ''
            nao = ''
        elif m20 == 0:
            nao = 'não '
            apenas = 'nem uma'
            plural = ''
        else:
            plural = 'es'
            apenas = m20
            nao = ''
print('A média de idade é {};'.format(str(si / 4).replace('.', ',')))
print('O homem mais velho tem {} anos e se chama {};'.format(ihmv, nhmv))
print('Na lista {}há {} mulher{} menor{} de 20 anos.'.format(nao, apenas, plural, plural))