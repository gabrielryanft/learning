n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro outro número: '))

l = [n1, n2, n3]
l.sort()
print('Valores em ordem:\n 1 - {};\n 2 - {};\n 3 - {}.'.format(l[0], l[1], l[2]))
print('---//---12')
print('  O maior é o {} (Pos.: 1°);\n  E o menor é o {} (Pos.: 3°).'.format(l[0], l[2]))