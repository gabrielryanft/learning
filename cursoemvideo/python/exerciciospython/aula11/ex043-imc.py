p = float(input('Peso: (kg)'))
a = float(input('Altura: (m)'))
imc = p / a ** 2
print('Seu I.M.C.(Indice de Massa Corporal) é {}. Isso significa qie você está '.format(imc), end='')
if imc < 18.6:
    print('abaixo do peso.')
elif imc < 26:
    print('com o peso ideal.')
elif imc < 31:
    print('com sobrepeso.')
elif imc < 41:
    print('obeso(a).')
else: print('sofrendo de obesidade mórbida.')