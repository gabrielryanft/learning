def metade(num, format = False):
    return num / 2 if not format else cifraoVirgula(num / 2)

def dobro(num, format = False):
    return num * 2 if not format else cifraoVirgula(num * 2)

def aumentoporcent(num, porcent, format = False):
    return num + (num / 100 * porcent) if not format else cifraoVirgula(num + (num / 100 * porcent))

def descontoporcent(num, porcent, format = False):
    return num - (num / 100 * porcent) if not format else cifraoVirgula(num - (num / 100 * porcent))

def cifraoVirgula(valor, moeda = 'R$'):
    valorstr = f'{valor:.2f}'
    valorstrCifraVirgula = moeda + (valorstr.replace('.', ','))
    return valorstrCifraVirgula