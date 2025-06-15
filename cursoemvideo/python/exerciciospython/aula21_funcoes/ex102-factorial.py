def line(msg):
    print('~' * (len(msg) + 2))
    print(f' {msg} ')
    print('~' * (len(msg) + 2))

def trufal(value):
    if value in 'Yy':
        return True
    else: return False

def factorial(x, show = False):
    """
    -> Calculate the factorial of a number.
    :param x: The number you want to know the factorial of.
    :param show: (optional) show the calc or do not.
    :return: x's factorial.
    """
    line(f'Factorial of {x}:')
    f = 1
    for c in range(x, 0, -1):
        if show:
            if c != 1:
                print(f'{c} x ',end = '')
            else: print(f'{c} = ', end = '')
        f *= c
    print(f)

while True:
    factorial(int(input('Number: ')), show = trufal(str(input('Show calc or do not? ( Y / N ) '))))
    answer = str(input('Do you want to continue? ( Y / N ) '))
    if answer in 'Nn':
        break
help(factorial)