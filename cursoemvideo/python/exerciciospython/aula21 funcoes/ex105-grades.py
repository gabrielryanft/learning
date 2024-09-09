#-*- coding: utf-8 -*-

def grades(*tuple, situation=False):
    """
    -> analisa notas.
    :param tuple: as notas.
    :param situation: mostra ou não a situação.
    :return: lista com varias informações.
    """.encode('utf-8').decode('utf-8')
    dictionary = dict()
    dictionary['grades'] = len(tuple)
    dictionary['highest'] = max(tuple)
    dictionary['lowest'] = min(tuple)
    dictionary['avarege'] = sum(tuple) / dictionary['grades']
    if situation:
        if dictionary['avarege'] <= 4:
            dictionary['situation'] = 'bad'
        elif dictionary['avarege'] <= 6:
            dictionary['situation'] = 'recovery'
        else: dictionary['situation'] = 'good'
    return dictionary
test = grades(1.5 , 4, 5.5, 7.5, 7, 9, 1, 10, situation = True)
print(test)
help(grades)