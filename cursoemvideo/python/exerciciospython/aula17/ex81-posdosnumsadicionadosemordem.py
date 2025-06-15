l = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print('Foi adicionado ao final da lista.')
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                print(f'Foi inserido na {p + 1}° posiçõ.')
                break
            p += 1
print(f'Você dogitou os valores: {l}.')