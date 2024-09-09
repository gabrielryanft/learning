p = ('lapis', 1.25,
     'borracha', 2,
     'caderno', 5.99,
     'teto', 100.55,
     'roupas amarelas', 30.9,
     'frente e traz', 200.5)
for n in range(0, len(p)):
    if n % 2 == 0:
        print(f'{p[n]:.<20}', end='')
    else:
        print(f'R$ {p[n]:.2f}')