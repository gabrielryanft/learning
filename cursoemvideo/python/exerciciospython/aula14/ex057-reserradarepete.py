r = str(input('Seu gênero[ H / M ]: ')).strip().upper()[0]
while r not in 'HhMm':
    r = str(input('Resposta invalida. Digite o seu gênero: ')).strip().upper()[0]
if r in 'Mm':
    print('Olá fêmea!')
else: print('Olá macho!')