def littlehelp(term):
    line(f'searching about {term}...')
    print(f'\033[7;49;39m', end='')
    help(term)
    print(f'\033[m', end='')

def line(title):
    print("~" * (len(title) + 6))
    print(f'   {title}')
    print("~" * (len(title) + 6))

while True:
    line('What do you want to know?')
    answer = str(input('What function / library you want to see? (Type "end" to exit) ')).lower()
    if answer == 'end':
        break
    else: 
        littlehelp(answer)
line('Bye!!!')