from copy import deepcopy

class AttrDict:
    def __init__(self, data={}):
        self._data = deepcopy(data)
        self.__dict__.update(data)

    @property
    def data(self):
        return self._data

    def __iter__(self):
        yield from self.data

    def __len__(self):
        return len(self.data)
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]


        



print('TEST_1:')
attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))

print('TEST_2:')
attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

print('TEST_3:')
attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)

print('TEST_4:')
d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')

print('TEST_5:')
d = dict.fromkeys(range(100), None)
print(d)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)