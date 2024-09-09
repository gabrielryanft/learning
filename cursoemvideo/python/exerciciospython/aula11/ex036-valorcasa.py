c = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
t = int(input('Tempo(Anos): '))

if c / (t * 12) <= s / 100 * 30:
    print('Foi aprovado. Você pagara: R${:.2f}p.m.'.format(c / (t * 12)))
else: print('Não foi aprovado. Você teria que pagar: R${:.2f}p.m.'.format(c / (t * 12)))