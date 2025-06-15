from random import randint 
from time import sleep
from operator import itemgetter
dictionary = {'1º player': randint(1, 6),
              '2º player': randint(1, 6),
              '3º player': randint(1, 6),
              '4º player': randint(1, 6)}
for t, v in dictionary.items():
    print(f'{f"{t} rolled {v} on the dice.":^44}')
ranking = list()
ranking = sorted(dictionary.items(), key = itemgetter(1), reverse = True)#key = itemgetter(1) = o termo chave é o item 1(eu acho)
print(f'{"°-.-" * 11}')
print(f'{"Ranking":^44}')
for p, d in enumerate(ranking):
    print(f'{p + 1}º position: {d[0]} rolled {d[1]} on the dice.')