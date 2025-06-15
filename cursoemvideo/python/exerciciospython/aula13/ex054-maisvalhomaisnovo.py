from datetime import date 
d = date.today().year
mei = 0
mai = 0
for n in range(1, 8):
    a = int(input('Qual é a idade da {}° pessoa?'.format(n)))
    i = d - a
    if i < 19:
        mei += 1
        if mei > 1:
            esme = 'es'
            sme = 's'
        else:
            esme = ''
            sme = ''
    else:
        mai += 1
        if mai > 1:
            esma = 'es'
            sma = 's'
        else:
            esma = ''
            sma = ''
print('Na lista tem {} pessoa{} menor{} de idade;\nE {} pessoa{} maior{} de idade.'.format(mei, sme, esme, mai, sma, esma))