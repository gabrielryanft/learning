def metade(num, format = True):
    return num / 2 if not format else cifraoVirgula(num / 2)

def dobro(num, format = True):
    return num * 2 if not format else cifraoVirgula(num * 2)

def aumentoporcent(num, porcent, format = True):
    return num + (num / 100 * porcent) if not format else cifraoVirgula(num + (num / 100 * porcent))

def descontoporcent(num, porcent, format = True):
    return num - (num / 100 * porcent) if not format else cifraoVirgula(num - (num / 100 * porcent))

def cifraoVirgula(valor, moeda = 'R$'):
    valorstr = f'{valor:.2f}'
    valorstrCifraVirgula = moeda + (valorstr.replace('.', ','))
    return valorstrCifraVirgula

def resumo(preco, desconto = 50, aumento = 50):
    print('~' * 40)
    print(f'{"Lista de dados":^40}')
    print('~' * 40)
    print((f'preço analisado: \t\t{cifraoVirgula(preco)}')) # \t da uma tabulação (tabulação: Colocação de dados em colunas ou tabelas) no couso em akguns lugares eu coloquei 1 tabulaão e em putros eu coloquei 2
    print((f'preço em dobro: \t\t{dobro(preco)}'))
    print((f'Metade do preço: \t\t{metade(preco)}'))
    print((f'preço com {desconto}% de desconto: \t{descontoporcent(preco, desconto)}'))
    print((f'preço com {aumento}% de aumento: \t{aumentoporcent(preco, aumento)}'))
    print('~' * 40)