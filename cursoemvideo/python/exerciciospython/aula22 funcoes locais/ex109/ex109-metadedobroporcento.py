import funcoes
while True:
    preco = float(input('Preço: R$'))
    aumentoDesconto = float(input('Aumento / Desconto: '))
    print(f'O dobro de {funcoes.cifraoVirgula(preco)} é {funcoes.dobro(preco, True)}')
    print(f'A metade de {funcoes.cifraoVirgula(preco)} é {funcoes.metade(preco, False)}')
    print(f'Se o produto aumentar {aumentoDesconto}% ele custará {funcoes.aumentoporcent(preco, aumentoDesconto, False)}')
    print(f'Se o produto diminuir o preço em {aumentoDesconto}% ele custara {funcoes.descontoporcent(preco, aumentoDesconto, True)}')
    resposta = str(input('Você quer continuar? (S / N)'))
    if resposta in 'nN':
        break
print('\033[35mTenha um bom dia!\033[m')