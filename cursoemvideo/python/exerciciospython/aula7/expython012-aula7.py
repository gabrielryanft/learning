p = int(input('Digite o preço do produto: '))

p100 = p / 100
p5 = p100 * 5
pc = p - p5

print('{} com 5% de desconto é: {}'.format(p, pc))