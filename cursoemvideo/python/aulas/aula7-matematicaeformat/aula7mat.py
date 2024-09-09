"""
    operadires aritimeticos em ordem: 
    () oque estiver dentro de um parenteses
    ** potencia ou pow(4, 2) = 4² = 16
    * multiplicação, / divisão(cum virgila se nascessario), // divisão inteira, % resto da divisão
    + soma, - sobtração
"""

#ex:

"""
    5 + 3 * 2
        primeiro

    5 + 6
    segundo

    11
    ----//----

    3 * 5 + 4 ** 2
            primeiro(4²)

    3 * 5 + 16
    segundo

    15 + 16
    terceiro

    31
    ----//----

    3 * (5 + 4) ** 2
        primeiro

    3 * 9 ** 2
        segundo(9²)

    3 * 81
    terceiro

    243  
"""

#prova real: 

print(5 + 3 * 2) 

print(3 * 5 + 4 ** 2)

print(3 * (5 + 4) ** 2)

#bgl legal: 

print('Olá'*5) #imprimi Ola 5 vazes