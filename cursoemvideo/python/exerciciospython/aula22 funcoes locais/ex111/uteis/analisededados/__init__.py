from uteis.formatacaodados import cifraoVirgula

def metade(num, format = True):
    return num / 2 if not format else cifraoVirgula(num / 2)

def dobro(num, format = True):
    return num * 2 if not format else cifraoVirgula(num * 2)

def aumentoporcent(num, porcent, format = True):
    return num + (num / 100 * porcent) if not format else cifraoVirgula(num + (num / 100 * porcent))

def descontoporcent(num, porcent, format = True):
    return num - (num / 100 * porcent) if not format else cifraoVirgula(num - (num / 100 * porcent))