from uteis.formatacaodados import resumo, aprovado

while True:
    preco = aprovado('Preço: R$')
    aumento = aprovado('Aumento: ')
    desconto = aprovado('Desconto: ')
    resumo(preco, desconto, aumento)
    resposta = str(input('Você quer continuar? (S / N)'))
    if resposta in 'Nn':
        break
print('\033[32mTenha um bom dia!\033[m')