from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjaente: '))

hi = (co ** 2 + ca ** 2) ** 0.5
hii = hypot(co, ca)
print('A hipotenusa é = {:.2f}'.format(hi))
print('O mesmo resulatado comm diferente caminho: {:.2f}'.format(hii))