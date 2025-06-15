from time import sleep
for c in range(0, 51, 2):
    print(c)
    sleep(0.2)
print('Ou:')
sleep(.5)
for c2 in range(0, 51, 2):
    print(c2, end=' ')
    sleep(0.2)