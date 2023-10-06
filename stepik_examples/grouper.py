from copy import deepcopy

class Grouper:
    def __init__(self, sequence, key):
        # sequence is an iterable obj, key is a func
        self.iterable = deepcopy(sequence)
        self.key = key
        self.groups = {}
        for item in self.iterable:
            self.add(item)
        
    def __len__(self):
        return len(self.groups)
    
    def __iter__(self):
        for key in self.groups:
            yield key, self.groups[key]

    def __getitem__(self, key):
        return self.groups[key]
    
    def __delitem__(self, key):
        del self.groups[key]

    def add(self, item, key=None):
        key = self.group_for(item)
        if key in self.groups:
            self.groups[key].append(item)
        self.groups.setdefault(key, [item])

    def group_for(self, obj):
        return self.key(obj)
    
    def __contains__(self, key):
        return key in self.groups
        

# tests

print('TEST_1:')
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])

print('TEST_2:')
grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(3 in grouper)
print('bee' in grouper)

print('TEST_3:')
grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))
# print(grouper.__dict__)

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(len(grouper))

print('TEST_4:')
grouper = Grouper(['hi'], key=lambda s: s[0])

print(grouper.group_for('hello'))
print(grouper.group_for('bee'))
print(grouper['h'])
print('b' in grouper)

print('TEST_5:')
data = [504, 506, 503, 507, 507, 508, 504, 510, 500, 503, 501, 502, 503, 502, 502, 510, 502, 500, 503, 508, 508, 502,
        507, 500, 502, 501, 502, 504, 505, 505, 500, 501, 507, 504, 509, 507, 508, 508, 502, 510, 503, 501, 505, 501,
        510, 505, 500, 507, 510, 507, 506, 507, 501, 502, 504, 506, 501, 501, 506, 502, 508, 505, 509, 509, 502, 506,
        507, 505, 505, 507, 503, 505, 504, 510, 505, 503, 508, 508, 504, 504, 510, 501, 506, 503, 502, 508, 507, 503,
        501, 506, 505, 506, 504, 504, 505, 503, 507, 504, 507, 510]

grouper = Grouper(data, key=lambda x: x % 2 == 0)
print(grouper[True])
print(grouper[False])

print('TEST_6:')
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


grouper = Grouper(persons, key=lambda x: x.height)
# print(grouper.__dict__)
print(sorted(grouper))

print('TEST_7:')
grouper = Grouper([], key=lambda x: x)
print(*grouper)

print('TEST_8:')
d = list(range(1, 100))
grouper = Grouper(d, bool)
print(*grouper)

d.append(100)
print(*grouper)

print('TEST_9:')
d = range(1, 100)
grouper = Grouper(d, bool)
print(*grouper)

grouper.add(100)
print(*grouper)