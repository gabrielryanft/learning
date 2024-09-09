from time import sleep
while True:
    t = int(input('Quer ver a tabuada de qual número (Digite um N° negativo (Ex: -1) para encerrar.)? '))
    if t < 0: break
    for c in range(1, 11):
        print(f'{c} x {t} = {c * t}')
        sleep(.2)
print('Programa encerrado.')