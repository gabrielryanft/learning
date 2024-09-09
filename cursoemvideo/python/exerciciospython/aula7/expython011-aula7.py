l = int(input('Largura da parede: '))
a = int(input('Altura da parede: '))

ar = l * a
re = ar / 2

print('A quantidade de baldes de tinta nescessarios para pintar sua parede de {}x{} com a aera de {}m são (Considerando que um balde de tinta tem tinta o suficiente para pntar 2m²) {} baldes.'.format(l, a, ar, re))