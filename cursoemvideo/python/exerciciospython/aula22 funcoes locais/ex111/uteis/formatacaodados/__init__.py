def cifraoVirgula(valor, moeda = 'R$'):
    valorstr = f'{valor:.2f}'
    valorstrCifraVirgula = moeda + (valorstr.replace('.', ','))
    return valorstrCifraVirgula

def resumo(preco, desconto = 50, aumento = 50):
    from uteis.analisededados import descontoporcent, aumentoporcent, dobro, metade
    print('~' * 40)
    print(f'{"Lista de dados":^40}')
    print('~' * 40)
    print((f'preço analisado: \t\t{cifraoVirgula(preco)}')) # \t da uma tabulação (tabulação: Colocação de dados em colunas ou tabelas) no couso em akguns lugares eu coloquei 1 tabulaão e em putros eu coloquei 2
    print((f'preço em dobro: \t\t{dobro(preco)}'))
    print((f'Metade do preço: \t\t{metade(preco)}'))
    print((f'preço com {desconto}% de desconto: \t{descontoporcent(preco, desconto)}'))
    print((f'preço com {aumento}% de aumento: \t{aumentoporcent(preco, aumento)}'))
    print('~' * 40)

def aprovado(msg):
    while True:
        valor = str(input(msg)).strip().replace(',', '.')
        if not valor.replace('.', '', 1).isnumeric():
            print(f'\033[31m["{valor}" não é valido.]\033[m Digite somente números: {msg}')
        else: 
            break
    return float(valor)