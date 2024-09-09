m = int(input('escreva um valor em metros(só números): '))

c = m * 100
mi = m * 1000
k = m / 1000

print('{}m em kilometros é {}km centimetros é {}cm, e em milimetros é {}mm.'.format(m, k, c, mi))