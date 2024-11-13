from time import sleep
from random import randint
def randomnum(existinglist):
    print('Generating numbers... ')
    for c in range(0, 5):
        existinglist.append(randint(0, 10))
        print(f'{existinglist[c]}, ', end = '')
        sleep(.3)
    print('The end!')
def sumofevenn(existinglist):
    sum = 0
    for number in existinglist:
        if number % 2 == 0:
            sum += number
    print(f'The sum of the even numbers in {existinglist} is {sum}.')
mylist = list()
randomnum(mylist)
sumofevenn(mylist)