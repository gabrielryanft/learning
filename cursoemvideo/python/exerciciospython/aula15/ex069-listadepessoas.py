print('{:-^20}'.format('Cadastre'))
i18 = h = m20 = 0
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo ( H / M ): '))
    while s not in 'HhMm':
        s = str(input('Valor invalido. Sexo( H / M ): '))
    if i > 18:
        i18 += 1
    if s in 'Hh':
        h += 1
    if s in 'Mm' and i < 20:
        m20 += 1 
    c = str(input('Quer continuar ( S / N )? '))
    while c not in 'SsNn':
        c = str(input('Valor invalido. Quer continuar ( S / N )? '))
    if c in 'Nn':
        break
plui18 = '' if i18 < 2 else 's'
naoi18 = '' if i18 > 0 else 'não '
i18 = i18 if i18 > 0 else 'nem uma'
pluh = 'm' if h < 2 else 'ns'
naoh = '' if h > 0 else 'não '
h = h if h > 0 else 'nem um'
plum20 = '' if m20 < 2 else 'es'
naom20 = '' if m20 > 0 else 'não '
m20 = m20 if m20 > 0 else 'nem uma'
print(f'Na lista {naoi18}há {i18} pessoa{plui18} com mais de 18 anos.')
print(f'Na lista {naoh}há {h} home{pluh}.')
print(f'Na lista {naom20}há {m20} mulher{plum20} menor{plum20} de 20 anos.')