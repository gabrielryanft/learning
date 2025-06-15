import funcoes
while True:
    preco = float(input('Preço: R$'))
    aumento = float(input('Aumento: '))
    desconto = float(input('Desconto: '))
    funcoes.resumo(preco, desconto, aumento)
    resposta = str(input('Você quer continuar? (S / N)'))
    if resposta in 'nN':
        break
print('\033[35mTenha um bom dia!\033[m')