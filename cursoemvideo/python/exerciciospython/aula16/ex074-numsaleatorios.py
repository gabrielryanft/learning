from random import randint
l = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados são: {l}.')
print(f'O maior número é {max(l)}')
print(f'O menor número é {min(l)}')