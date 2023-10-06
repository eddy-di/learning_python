from copy import deepcopy

class PermaDict:
    def __init__(self, data={}):
        self.data = deepcopy(data)


    def __iter__(self):
        yield from self.data

    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = self.data.get(key, value)

    def __getitem__(self, key):
        return self.data[key]
    
    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
    
    def __len__(self):
        return len(self.data)
    









# tests

print('TEST_1:')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))

print('TEST_2:')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

print('TEST_3:')
permadict = PermaDict()


permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))

print('TEST_4:')
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)

print('TEST_5:')
d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)

print('TEST_6:')
d = {'Ерофей Всеволодович Сидоров': '13.05.1985', 'Семенов Андрон Денисович': '24.03.1988',
     'Петухова Лукия Максимовна': '15.06.1993', 'Лидия Георгиевна Фадеева': '25.12.1980',
     'Федотова Надежда Юрьевна': '04.06.1992', 'Харитонов Варфоломей Марсович': '14.06.1994',
     'Глафира Феликсовна Фомина': '29.08.1984', 'Пелагея Николаевна Брагина': '01.04.1986',
     'Никита Ильясович Макаров': '29.08.1992', 'Лихачева Майя Алексеевна': '12.11.1991',
     'Виноградова Нина Олеговна': '07.08.1992', 'Артемьева Кира Валентиновна': '11.04.1997',
     'Василиса Федоровна Уварова': '03.05.1981', 'Денисов Варфоломей Устинович': '17.04.1990',
     'Тихонова Клавдия Филипповна': '18.11.1988', 'Зимина Любовь Викторовна': '23.06.1983',
     'Кудряшов Викторин Фомич': '27.06.1997', 'Юлия Вениаминовна Ефимова': '20.10.1987',
     'Никандр Валерианович Мельников': '10.02.1985', 'Устинова Лидия Артемовна': '30.06.1992'}

permadict = PermaDict(d)

for key in permadict.keys():
    print(key, end='; ')

print('\n')

for value in permadict.values():
    print(value, end='; ')

print('\n')

for item in permadict.items():
    print(item, end='; ')

print('TEST_7:')
permadict = PermaDict()
print('Keys:', *permadict.keys())
print('Values:', *permadict.values())
print('Items:', *permadict.items())