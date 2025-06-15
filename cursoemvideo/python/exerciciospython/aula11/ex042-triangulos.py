s1 = float(input('Segmento 1: '))
s2 = float(input('Segmento 2: '))
s3 = float(input('Segmento 3: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('É possivel fazer um triângulo ', end='')
    if s1 == s2 == s3: #tudo igual
        print('Equilatero!!!')
    elif s1 != s2 != s3 != s1: #tudo diferente
        print('Escaleno!')
    else: print('Isósceles!!') #dois iguais
else: print('Não é possivel fazer um triângulo.')