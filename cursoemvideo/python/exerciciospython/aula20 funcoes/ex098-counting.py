from time import sleep
def line(msg):
    print('=' * (len(msg) + 2))
    sleep(.3)
    print(f' {msg} ')
    sleep(.3)
    print('=' * (len(msg) + 2))
    sleep(.3)
def counting(start, end, step):
    line(f'From {start} to {end} {step} by {step}.')
    if end < start:
        step *= -1
    if step > 0:
        end += 1
    if step < 0:
        end -= 1
    for c in range(start, end, step):
        print(f'{c} ', end = '')
        sleep(.3)
    print('The End!')

counting(1, 10, 1)
counting(10, 1, 2)
line(f'Do it your self:')
while True:
    counting(int(input('Start: ')), int(input('End: ')), int(input('Step: (Do not use negative numbers.) ')))
    a = str(input('Do you whant to continue? ( S / N ) '))
    if a in "Nn":
        break