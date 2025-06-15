from datetime import datetime
dictionary = dict()
dictionary['name'] = str(input('Name: '))
dictionary['age'] = datetime.now().year - (int(input('Year of birth: ')))
# dictionary['age'] = datetime.now().year - yearob
dictionary['work record book'] = int(input('Work record book(Type 0 if you do not have one.): '))
if dictionary['work record book'] != 0:
    dictionary['hired'] = int(input('Hire year: '))
    dictionary['salary'] = float(input('Salary: R$'))
    dictionary['retirement'] = dictionary['age'] + (dictionary['hired'] + 35) - datetime.now().year
print('~-' * 25)
print(f'{" Result: ":^50}')
for k, v in dictionary.items():
    print(f'{k} is {v}')
