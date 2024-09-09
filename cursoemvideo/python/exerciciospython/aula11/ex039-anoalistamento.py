from datetime import date

a = int(input('Digite o seu ano de nascimento: '))
print('Você é:\n - Homem [ H ](Digite a letra H);\n - Mulher [ M ](Digite a letra M).')
hm = str(input('Resposta: ')).upper()
if hm == 'M':
 print('Olá, fêmea.')
else:
 aa = date.today().year

 print('Você tem {} anos.'.format(aa - a))

 if (aa - a) < 18:
  print('Está muito novo.')
  print('Você não precisa se alistar, Mas daqui a {} anos você vai.'.format(18 - (aa - a)))
  print('Seu alistamento será em: {}'.format(a + 18))
 elif (aa - a) == 18:
  print('Está na idade perfeita para se alistar.')
  print('Você precisa se alistar.')
 elif (aa - a) > 18:
  print('Está valho.')
  print('Você se alistou a {} anos atrás (Eu espero).'.format(aa - a - 18))
  print('seu alistamento foi em: {}'.format(a + 18))