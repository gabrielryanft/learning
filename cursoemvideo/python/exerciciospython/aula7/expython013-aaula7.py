s = int(input('Qual o seu salario atual? '))

s100 = s / 100
s15 = s100 * 15
sa = s + s15

print('O seu sálario de {} com 15% de aumento seria: {}.'.format(s, sa))