listod, females , ageaa = list(), list(), list()
dictionary = dict()
sum = 0
while True:
    dictionary.clear()
    dictionary['name'] = str(input('Name: ')).strip().title()
    dictionary['sex'] = str(input('Sex: ( M / F ) '))
    while dictionary['sex'] not in 'MmFf':
        dictionary['sex'] = str(input('[Error] Please, answer with "M" or "F": '))
    dictionary['age'] = int(input('Age: '))
    sum += dictionary['age']
    a = str(input('Do you want to continue? ( y / N )'))
    listod.append(dictionary.copy())
    while a not in 'YyNn':
        a = str(input('[Error] Please, answer with "Y" or "N": '))
    if a in 'Nn':
        break
print(f'You have registered {len(listod)} people.')
print(f'The avarege age is {sum / len(listod)}.')
for p, t in enumerate(listod):
    if t['sex'] in 'Ff':
        females.append(t['name'])
    if t['age'] > (sum / len(listod)):
        ageaa.append(p)
print(f'You have registered {len(females)} female{"s" if len(females) > 1 else ""}. {"their" if len(females) > 1 else "Her"} name is: {females}.')
print(f'List with the people older than the avarage:')
for p in ageaa:
    for t, v in listod[p].items():
        print(f' {t} = {v};', end = '')
    print()