import funcoes
while True:
    preco = float(input('Preço: R$'))
    aumentoDesconto = float(input('Aumento / Desconto: '))
    print(f'O dobro de {funcoes.cifraoVirgula(preco)} é {funcoes.cifraoVirgula(funcoes.dobro(preco))}')
    print(f'A metade de {preco} é {funcoes.cifraoVirgula(funcoes.metade(preco))}')
    print(f'Se o produto aumentar {funcoes.cifraoVirgula(aumentoDesconto)}% ele custará {funcoes.cifraoVirgula(funcoes.aumentoporcent(preco, aumentoDesconto))}')
    print(f'Se o produto diminuir o preço em {funcoes.cifraoVirgula(aumentoDesconto)}% ele custara {funcoes.cifraoVirgula(funcoes.descontoporcent(preco, aumentoDesconto))}')
    resposta = str(input('Você quer continuar? (S / N)'))
    if resposta in 'nN':
        break
print('\033[35mTenha um bom dia!\033[m')