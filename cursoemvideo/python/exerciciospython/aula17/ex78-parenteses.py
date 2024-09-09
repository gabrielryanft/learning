e = str(input('Digite uma expressão com parenteses: '))
l = []
for p in e:
    if p == '(':
        l.append(p)
    elif p == ')': 
        if len(l) > 0 and '(' in l:
            l.remove('(')
        else:
            l.append(p)
print('Expressão válida.' if len(l) == 0 else 'A expressão não é válida.')