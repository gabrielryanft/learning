from random import randint
from time import sleep
def numbers(*listovs):
    print('=' * 30)
    sleep(.3)
    print('Creating values...')
    sleep(.3)
    print(f'Values = {listovs[0]}, {len(listovs[0])} values in total.')
    sleep(.3)
    print(f'The highest value in the list is {max(listovs[0])}.')
    sleep(.3)
    print('=' * 30)
    sleep(.3)
def numbersc(size):
    listn = [randint(0, 100) for c in range(size + 1)]
    numbers(listn)
while True:
    print('What do you want?')
    print(f'{"You want me to create one list":<36} : Press 1.')
    print(f'{"You want to create one list yourself":<36} : Press 2.')
    typeol = int(input('Answer: '))
    while typeol > 2 or typeol < 1:
        typeol = int(input('Please, answer with 1 or 2: '))
    if typeol == 1:
        n = int(input('How many lists do you want me to generate? '))
        for p in range(1, n + 1):
            numbersc(randint(0, 10))
    else:
        listpc = list()
        numberslist = int(input('how many values will your list have? '))
        for p in range(0, numberslist):
            listpc.append(int(input(f'Value Nº {p + 1}: ')))
        numbers(listpc)
    answer = str(input('Do you want to continue? ( Y / N ) '))
    if answer in 'Nn':
        break