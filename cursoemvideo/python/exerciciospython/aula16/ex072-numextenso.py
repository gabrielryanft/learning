n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    r = int(input('Digite um número( 0 a 10 ): '))
    if r < 0 or r > 20: 
        r = int(input('Valor invalido. Digite um número( 0 a 10 ): '))
    print(f'Você digitou o número {n[r]}.')
    c = str(input('quer continuar? '))
    if c in 'Nn':
        break
print('Tchau!')