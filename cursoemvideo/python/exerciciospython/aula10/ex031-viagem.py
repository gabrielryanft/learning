d = int(input('Distancia da viagem: '))
if d > 200:
    d = d * 0.45
    print('Preço: R${:.2f}'.format(d))
else: 
    d = d * 0.50
    print('Preço: R${:.2f}'.format(d))