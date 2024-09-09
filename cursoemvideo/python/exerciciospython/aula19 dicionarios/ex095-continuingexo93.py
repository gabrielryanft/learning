dictionary = dict()
listod = list()
while True:
    dictionary.clear()
    dictionary['name'] = str(input('Chess player name: ')).strip().title()
    number = int(input(f'How many maches did {dictionary["name"]} played? '))
    dictionary['maches'] = list()
    dictionary['wins'] = 0
    for c in range(1, number + 1):
        dictionary['maches'].append(str(input(f'Did {dictionary["name"]} won the{f" {c}º" if number > 1 else ""} mach? ( Y / N ) ')))
        if dictionary['maches'][c - 1] in 'Yy':
            dictionary['wins'] += 1
    listod.append(dictionary.copy())
    r = str(input('Do you want to continue? ( Y / N ) '))
    while r not in 'YyNn':
        r = str(input('Please, answer with "Y" or "N": '))
    if r in 'Nn':
        break
print('\033[0;30;40m  \033[0;37;47m  \033[m' * 25)
print(f'{"Nº":^12}{"Name":^20}{"Maches":^14}{"Wins":>5}')
for p, l in enumerate(listod):
    print(f'Player {p + 1} - {l["name"] if len(l["name"]) < 12 else str(l["name"])[:12] + "...":^20}{len(l["maches"]):^14}{l["wins"]:^5}')
print('\033[0;30;40m  \033[0;37;47m  \033[m' * 25)
while True:
    a = int(input("You want to see the maches of which player?(Type the player's number)(Type 999 to exit) "))
    if a == 999:
        break
    elif a - 1 >= len(listod):
        print(f"[Error] Player Nº {a} do not exist. Try again.")
    else:
        for p, v in enumerate(listod[a - 1]['maches']):
            print(f'Did {listod[a - 1]["name"]} won the {p + 1}º mach? {"Yes" if v in "Yy" else "No"}.')