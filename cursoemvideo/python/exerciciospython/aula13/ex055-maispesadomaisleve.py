for p in range(1, 6):
    k = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        mp = k
        ml = k
    else:
        if k < ml:
            ml = k
        elif k > mp:
            mp = k
print('A pessoa mais pesada tem: {}kg;\nE a pessoa mais leve tem: {}kg.'.format(mp, ml))