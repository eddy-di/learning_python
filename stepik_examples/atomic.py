from copy import copy, deepcopy

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy_data = (deepcopy(data) if self.deep else copy(data))

    def __enter__(self):
        return self.copy_data
    
    def __exit__(self, exc_value, exc_type, traceback):
        if exc_type:
            return True
        if isinstance(self.copy_data, list):
            self.data[:] = self.copy_data
            return self.data
        elif isinstance(self.copy_data, set|dict):
            self.data.update(self.copy_data)
            return self.data
        

# tests

print('TEST_1:')
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

print('TEST_2:')
numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)

print('TEST_3:')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

print('TEST_4:')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

print('TEST_5:')
numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))

print('TEST_6:')
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

with Atomic(data, True) as atomic:          # deep = True
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

with Atomic(data) as atomic:                # deep = False
    atomic['birthday']['month'] = 'April'   # изменение вложенной структуры
    print(atomic['name'])                   # обращение по несуществующему ключу

print(data)

print('TEST_7:')
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2   # изменение структуры

print(data)

print('TEST_8:')
matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)

print(matrix)