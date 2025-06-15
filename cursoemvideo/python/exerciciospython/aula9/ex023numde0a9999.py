n = int(input('Digite um número(De 0 até 9999): '))
ns = str(n)
print('Milhar: {}'.format(ns[0]))
print('Centena: {}'.format(ns[1]))
print('Dezena: {}'.format(ns[2]))
print('Unidade: {}'.format(ns[3]))

#ou: do jeito matematico ==

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))