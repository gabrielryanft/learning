from datetime import date
def vote(year):
    age = date.today().year - year
    size = len(f'To vote or not to vote with {age} years old, that is the question.')
    print('~' * (size + 2))
    print(f' to vote or not to vote with {age} years old, that is the question. ')
    print('~' * (size + 2))
    if age <= 15:
        return print('Do not vote. (Too young.)')
    elif age <= 18 or age > 65:
        return print('It is not mandatory. (If you want to, vote.)')
    else: return print('It is mandatory. (You are obliged to vote)')

while True:
    vote(int(input('Year of born: ')))
    a = str(input('Do you want to continue? '))
    if a in 'Nn':
        break