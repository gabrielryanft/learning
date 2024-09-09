def line(msg):
    print('~' * (len(msg) + 6))
    print(f'   {msg}   ')
    print('~' * (len(msg) + 6))
def numinteger(numprobably):
    while True:
        num = str(input(numprobably))
        if num.isnumeric():
            line(f'You have typed the number: {num}.')
            break
        else: print(f'\033[31mType some {"integer number".upper()}.\033[m')
numinteger('Type some ineger number: ')