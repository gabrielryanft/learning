#modo gabriel(o jeiot do gabriel acabou sendo o mesmo jeito do guanabara.):

vel = int(input('Qual é a sua velocidade? '))

if vel > 80:
    vel = (vel - 80) * 7.00
    print('Você foi multado em R${:.2f}.'.format(vel))
else: print('Tá tudo de boa.')