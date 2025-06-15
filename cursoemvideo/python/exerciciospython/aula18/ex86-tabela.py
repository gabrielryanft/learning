list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for b in range(0, 3):
    for i in range(0, 3):
        list[b][i] = int(input(f'Digite o número [{b} : {i}]: '))
for b in range(0, 3):
    for i in range(0, 3):
        print(f'[{list[b][i]: ^5}]', end='')
    print()