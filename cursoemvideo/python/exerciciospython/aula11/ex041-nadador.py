from datetime import date
a = int(input('Digite o ano que o atleta nasceu: '))
i = date.today().year - a

if i <= 9:
    c = 'Mrim'
elif i <= 14:
    c = 'Infantil'
elif i <= 19:
    c = 'Junior'
elif i <= 25:
    c = 'Sênior'
else: print('Master')

print('O atleta tem {} anos;\nSua classificação é: {}'.format(i, c))