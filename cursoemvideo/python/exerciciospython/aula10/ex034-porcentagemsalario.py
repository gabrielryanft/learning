s = float(input('Qual o seu salario? R$'))
if s > 1250.00:
    s = s / 100 * 10
else: s = s / 100 * 15
print('O seu aumento é R${:.2f}'.format(s))