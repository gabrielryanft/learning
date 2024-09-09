s = str(input('Digite algumas palavras: ')).lower().strip()

print("N° da A's: {}".format(s.count('a')))
print('Posição do primeiro A: {}'.format(s.find('a') + 1))
print('Posição do ultimo A: {}'.format(s.rfind('a') + 1))