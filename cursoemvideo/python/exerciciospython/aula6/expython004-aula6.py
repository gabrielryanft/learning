val = input('digite algo: ')

print('tipo primitivo do valor dado é: {}'.format(type(val)))
print('o valor é uma string? {}'.format(val.isalpha()))
print('o valor é um número? {}'.format(val.isnumeric()))
print('o valor é uma string e/ou um número? {}'.format(val.isalnum()))
print('o valor é so espaços? {}'.format(val.isspace()))
print('o valor está somente em letras maiusculas? {}'.format(val.isupper()))
print('o valor está somente em letras minusculas? {}'.format(val.islower()))
print('o valor está capitalizada? {}'.format(val.istitle()))#testa se está capitalizada, com a primeira em maiusculas.
print('o valor é? {}'.format(val.isascii()))