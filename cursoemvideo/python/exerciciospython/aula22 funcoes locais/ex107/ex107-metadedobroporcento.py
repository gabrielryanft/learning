import funcoes
while True:
    preco = float(input('Preço: R$'))
    aumentoDesconto = float(input('Aumento / Desconto: '))
    print(f'O dobro de {preco:.2f} é {funcoes.dobro(preco):.2f}')
    print(f'A metade de {preco:.2f} é {funcoes.metade(preco):.2f}')
    print(f'Se o produto aumentar {aumentoDesconto:.2f}% ele custará {funcoes.aumentoporcent(preco, aumentoDesconto):.2f}')
    print(f'Se o produto diminuir o preço em {aumentoDesconto:.2f}% ele custara {funcoes.descontoporcent(preco, aumentoDesconto):.2f}')
    resposta = str(input('Você quer continuar? (S / N)'))
    if resposta in 'nN':
        break
print('\033[35mTenha um bom dia!\033[m')