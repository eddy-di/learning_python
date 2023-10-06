class HistoryDict:
    def __init__(self, data=()):
        self.data = dict(data) or {}
        self.history_data = {}
        self.history_data.update(dict(data))
        self.history_data = {key: [value] for key, value in self.history_data.items()}
            
    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    def history(self, key):
        if key not in self.history_data:
            self.history_data[key] = []
        return self.history_data[key]
    
    def all_history(self):
        self.synchronize_dicts(self.data, self.history_data)
        return self.history_data
    
    def __iter__(self):
        yield from self.data

    def __len__(self):
        return len(self.data)
    
    def __setitem__(self, key, value):
        if key in self.data or key not in self.data:
            self.data[key] = value
        if key in self.history_data:
            self.history_data[key].append(value)

    def __getitem__(self, key):
        return self.data[key]
    
    def __delitem__(self, key):
        if key in self.data and key in self.history_data:
            del self.history_data[key]
            del self.data[key]
        elif key not in self.data and key in self.history_data:
            del self.history_data[key]

    @staticmethod
    def synchronize_dicts(main_dict, dependent_dict):
        # Add missing keys from the main dictionary to the dependent dictionary
        for key, value in main_dict.items():
            if key not in dependent_dict:
                dependent_dict[key] = [value]

        # Remove keys from the dependent dictionary that are not in the main dictionary
        keys_to_remove = [key for key in dependent_dict if key not in main_dict]
        for key in keys_to_remove:
            del dependent_dict[key]
    


# tests

print('TEST_1:')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

print('TEST_2:')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

print('TEST_3:')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

print('TEST_4:')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

print('TEST_5:')
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
# print(historydict.__dict__)
del historydict['ducks']
del historydict['cats']
print(len(historydict))

print('TEST_6:')
d = {'name': 'Иннокентий Елисеевич Архипов', 'age': 34, 'year': 1989}
historydict = HistoryDict(d)

names = ['Регина Ефимовна Костина', 'Мина Викторович Лаврентьев', 'Голубева Юлия Робертовна',
         'Чернова Варвара Максимовна', 'Юдин Матвей Иосипович', 'Степанов Мечислав Ерофеевич',
         'Абрамов Амос Августович', 'Ольга Егоровна Константинова', 'Хохлов Ираклий Ефимьевич',
         'Нестеров Никон Ермилович', 'Третьякова София Юльевна', 'Кудряшова Нина Юльевна', 'Казакова Раиса Феликсовна',
         'Александрова Надежда Николаевна', 'Никон Давыдович Васильев', 'Пахом Ильясович Морозов',
         'Дмитрий Тихонович Панов', 'Лебедева Галина Валериевна', 'Кузьмина Анастасия Викторовна',
         'Севастьян Жанович Якушев']

ages = [37, 20, 31, 21, 38, 24, 31, 24, 37, 20, 22, 39, 25, 21, 28, 28, 30, 30, 36, 23]

years = [1986, 2003, 1992, 2002, 1985, 1999, 1992, 1999, 1986, 2003, 2001, 1984, 1998, 2002, 1995, 1995, 1993, 1993,
         1987, 2000]

for name, age, year in zip(names, ages, years):
    historydict['name'] = name
    historydict['age'] = age
    historydict['year'] = year

print(*historydict.items())
print(historydict.history('name'))
print(historydict.history('age'))
print(historydict.history('year'))

print('TEST_7:')
historydict = HistoryDict()
print('Keys:', *historydict.keys())
print('Values:', *historydict.values())
print('Items:', *historydict.items())
print('History(key=1):', historydict.history(1))
print('History(key=1):', historydict.history(1))
print('All history:', historydict.all_history())

print('TEST_8:')
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())

print('TEST_9:')
d = dict.fromkeys(range(100), None)
attrdict = HistoryDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)