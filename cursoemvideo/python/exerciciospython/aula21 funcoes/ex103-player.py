def player(playern='<Undefined>', maches = 0):
    print(f'The player \033[32m{playern}\033[m played \033[32m{maches}\033[m maches.')

name = str(input('Player name: ')).strip().title()
nummaches = str(input('Number of maches: '))
if not nummaches.isnumeric() and not name:
    player()
elif not name:
    player(maches = nummaches)
elif not nummaches.isnumeric():
    player(playern = name)
else: player(name, nummaches)