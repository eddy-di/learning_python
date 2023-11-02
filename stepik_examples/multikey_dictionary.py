from collections import UserDict
from typing import Any


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.data = kwargs
        elif args:
            self.data = {}
            for i in args:
                for el in i:
                    self.data.setdefault(el[0], el[1])
        self.aliases = {}

    def alias(self, old_key, alias_key):
        self.aliases[alias_key] = self.data[old_key]
    
    def __getitem__(self, key: Any) -> Any:
        if key in self.data:
            return self.data[key]
        return self.aliases[key]
            
    def __setitem__(self, key: Any, value: Any) -> None:
        value_change = None
        if key in self.data:
            value_change = self.data[key]
        elif key in self.aliases:
            value_change = self.aliases[key]
        else:
            self.data[key] = value
        for k, v in self.data.items():
            if v == value_change:
                self.data.__setitem__(k, value)
        for k, v in self.aliases.items():
            if v == value_change:
                self.aliases[k] = value
        
        


# tests

print()
print('TEST_1:')
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
print(multikeydict['z'])
multikeydict['t'] += 1
print(multikeydict['x'])

multikeydict.alias('y', 'z')
multikeydict['z'] += [30]
print(multikeydict['y'])

print()
print('TEST_2:')
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])

try:
    print(multikeydict['x'])
except KeyError:
    print('Ключ отстутствует')

print()
print('TEST_3:')
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])

multikeydict['y'] += [30]
print(multikeydict['y'])

print()
print('TEST_4:')
multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])

print()
print('TEST_5:')
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['x'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

print()
print('TEST_6:')
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['y'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

print()
print('TEST_7:')
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])
print(multikeydict1['y'])
print(multikeydict2['z'])

multikeydict1['a'] = 4
print(multikeydict1['a'])

print()
print('TEST_8:')
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
del multikeydict['x']
multikeydict['z'] += 1
print(multikeydict['z'])
print(multikeydict['t'])