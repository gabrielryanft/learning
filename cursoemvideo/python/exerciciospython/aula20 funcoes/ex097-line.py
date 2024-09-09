def line(msg):
    print('~' * (len(msg) + 2))
    print(f' {msg} ')
    print('~' * (len(msg) + 2))

while True:
    line(input('Type some thing: '))
    a = str(input('Do you want to continue? ( Y / N ) '))
    if a in 'Nn':
        break