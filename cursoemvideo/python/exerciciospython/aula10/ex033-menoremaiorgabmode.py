n1 = int(input('1 - Digite um número: '))
n2 = int(input('2 - Digite outro número: '))
n3 = int(input('3 - Digite outro outro número: '))

l = [n1, n2, n3]

mi = min(l)
ma = max(l)

print('  O maior é o {} (Pos.: {}°);\n  E o menor é o {} (Pos.: {}°).'.format(ma, l.index(ma) + 1, mi, l.index(mi) + 1))