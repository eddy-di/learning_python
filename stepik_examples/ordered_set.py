from copy import deepcopy

class OrderedSet:
    def __init__(self, iterable=[]):
        self.first = deepcopy(iterable)
        indexes = {}
        for i in self.first:
            indexes[i] = indexes.get(i, 0) + 1
        
        self.iterable = []
        for keys in indexes.keys():
            self.iterable.append(keys)
    
    @staticmethod
    def ordering(sequence):
        indexes = {}
        for i in sequence:
            indexes[i] = indexes.get(i, 0) + 1
        result = []
        for keys in indexes.keys():
            result.append(keys)
        return result

    def __iter__(self):
        yield from self.ordering(self.iterable)
    
    def __contains__(self, value):
        return value in self.iterable
    
    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key]
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.iterable == other.iterable
        elif isinstance(other, set):
            return set(self.iterable) == other
        return NotImplemented
    
    def add(self, value):
        self.iterable.append(value)

    def discard(self, value):
        value_index = -1
        if value in self.iterable:
            for i in self.iterable:
                value_index += 1
                if i == value:
                    break
            del self.iterable[value_index]


print('TEST_1:')
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

print('TEST_2:')
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

print('TEST_3:')
orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

print('TEST_4:')
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)

print('TEST_5:')
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

print('TEST_6:')
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)

print('TEST_7:')
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))
