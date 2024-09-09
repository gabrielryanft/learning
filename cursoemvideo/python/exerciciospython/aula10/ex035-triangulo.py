t1 = float(input('Digite o tamanho do primairo segmento do triângulo: '))
t2 = float(input('digite o tamanho do segundo segmento: '))
t3 = float(input('Digite o tamanho do tercero segmento: '))

if t1 < t2 + t3 and t2 < t3 + t1 and t3 < t2 + t1:
    print('É possivel fazer um triângulo.')
else: print('Não é possivel fazer um triangulo.')