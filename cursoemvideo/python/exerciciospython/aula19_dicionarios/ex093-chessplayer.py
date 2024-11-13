dictionary = dict()
dictionary['name'] = str(input('Chess player name: ')).strip().title()
number = int(input(f'How many maches did {dictionary["name"]} played? '))
dictionary['maches'] = list()
dictionary['wins'] = 0
for c in range(1, number + 1):
    dictionary['maches'].append(str(input(f'Did {dictionary["name"]} won the{f" {c}º" if number > 1 else ""} mach? ( Y / N ) ')))
    if dictionary['maches'][c - 1] in 'Yy': dictionary['wins'] += 1
print('\033[0;30;40m  \033[0;37;47m  \033[m' * 25)
print(dictionary)
print('\033[0;30;40m  \033[0;37;47m  \033[m' * 25)
for k, v in dictionary.items():
    print(f'{k} is {v}.')
print('\033[0;30;40m  \033[0;37;47m  \033[m' * 25)
print(f'The chess player {dictionary["name"]} payed {len(dictionary["maches"])}')
for p, v in enumerate(dictionary['maches']):
    print(f'  => Did he won the{f" {p + 1}º" if len(dictionary["maches"]) > 1 else ""} mach? {v}.')
print(f'Wins = {dictionary["wins"]} of {len(dictionary["maches"])}.')