from copy import deepcopy

class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        res_iter = deepcopy(iterable)
        res = tuple(i % size for i in res_iter)
        instance = super().__new__(cls, res)
        return instance
    

# tests

print('TEST_1:')
modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))

print('TEST_2:')
modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)

print('TEST_3:')
modulartuple = ModularTuple()
print(modulartuple)

print('TEST_4:')
modulartuple = ModularTuple([1, 2, 3, 4, 5], 1)

print(modulartuple)

print('TEST_5:')
data = [1, 2, 3, 4, 5]
modulartuple = ModularTuple(data, -5)

print(modulartuple)

data.extend([6, 7, 8, 9, 10])
print(data)
print(modulartuple)