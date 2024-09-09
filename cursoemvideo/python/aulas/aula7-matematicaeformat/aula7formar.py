nome = input('Qual é o seu nome? ')

print('Olá {}!(nada)'.format(nome))
print('Olá {:20}!(20 espaços)'.format(nome)) #escreve o nome com 20 espaços.
print('Olá {:>20}!(á direita)'.format(nome))#usando alinhamentos á direita(sinais de maior e menor)
print('Olá {:<20}!(á esquerda)'.format(nome))#usando alinhamentos á esquerda(sinais de maior e menor)
print('Olá {:^20}!(ao centro)'.format(nome))#alinhando ao centro
print('Olá {:=^20}!(ao centro com igual)'.format(nome))#bota o sinal de igual