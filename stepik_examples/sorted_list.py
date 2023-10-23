from collections.abc import Iterator, Sequence


class SortedList(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = sorted(iterable[:])

    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key]
    
    @staticmethod
    def find(obj, iterable):
        for i in range(len(iterable)):
            if iterable[i] == obj:
                return i
    
    def add(self, obj):
        self.iterable.append(obj)
        self.iterable = sorted(self.iterable)
        return self.iterable

    def discard(self, obj):
        del_index = self.find(obj, self.iterable)
        while True:
            if self.iterable[del_index] == obj:
                self.iterable.pop(del_index)
            else:
                break
        self = self.iterable
        return self
    
    def update(self, other):
        self.iterable = self.iterable + other
        self.iterable = sorted(self.iterable)
        return self

    
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.iterable})'
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(sorted(self.iterable + other.iterable))
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            res = self.iterable.__add__(other.iterable)
            self.iterable.clear()
            self.iterable = [i for i in res]
            return self
        return NotImplemented

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(sorted(self.iterable * num))
        return NotImplemented
    
    def __imul__(self, num):
        if isinstance(num, int):
            res = self.iterable.__mul__(num)
            self.iterable.clear()
            self.iterable = [i for i in sorted(res)]
            return self
        return NotImplemented
    
    def __delitem__(self, key):
        del self.iterable[key]

    def __setitem__(self, key, value):
        raise NotImplementedError
    
    def append(self, obj):
        raise NotImplementedError
    
    def insert(self, index, obj):
        raise NotImplementedError
    
    def extend(self, obj):
        raise NotImplementedError
    
    def reverse(self):
        raise NotImplementedError
    
    def __reversed__(self) -> Iterator:
        raise NotImplementedError

    # @staticmethod
    # def bubble_sort(sequence):
        # a = sequence
        # n = len(sequence)
        # for i in range(n - 1):
            # exchange = 0
            # for j in range(n - i - 1):
                # if a[j] > a[j + 1]:
                    # a[j], a[j + 1] = a[j + 1], a[j]
                    # exchange += 1
            # if exchange == 0:
                # break
        # return sequence

#tests
# print('TEST_1:')
# numbers = SortedList([5, 3, 4, 2, 1])


# print(numbers)
# print(numbers[1])
# print(numbers[-2])
# numbers.add(0)
# print(numbers)
# numbers.discard(4)
# print(numbers)
# numbers.update([4, 6])
# print(numbers)

# print('TEST_2:')
# numbers = SortedList([5, 3, 4, 2, 1])

# print(len(numbers))
# print(*numbers)
# print(1 in numbers)
# print(6 in numbers)

# print('TEST_3:')
# numbers1 = SortedList([1, 3, 5])
# numbers2 = SortedList([2, 4])

# print(numbers1 + numbers2)
# print(numbers1 * 2)
# print(numbers2 * 2)

# print('TEST_4:')
# numbers = SortedList([5, 4, 3, 2, 1])

# print(numbers)
# del numbers[1]

# print(numbers)
# del numbers[-1]

# print(numbers)

# try:
#     numbers[0] = 7
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# print('TEST_5:')
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.append(6)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# print('TEST_6:')
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.insert(0, 0)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# print('TEST_7:')
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.extend([6, 7, 8, 9, 10])
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# print('TEST_8:')
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.reverse()
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# print('TEST_9:')
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     reversed(numbers)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

print('TEST_10:')
numbers = SortedList([5, 4, 3, 2, 1])

numbers.update([5, 4, 3, 2, 1])
print(*numbers)

numbers *= 3
print(*numbers)

numbers.discard(4)
print(*numbers)

print('TEST_11:')
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

print('TEST_12:')
data = [5, 4, 3, 2, 1]
numbers = SortedList(data)

print(numbers)
data.pop()

print(data)
print(numbers)

print('TEST_13:')
numbers = SortedList()
print(numbers)

print('TEST_14:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 + numbers2
print(numbers1, type(numbers1))

numbers2 = numbers2 * 2
print(numbers2, type(numbers2))

print('TEST_15:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 += numbers2
print(numbers1, type(numbers1))

numbers2 *= 2
print(numbers2, type(numbers2))

print('TEST_16:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 * -100
print(numbers1)

numbers2 *= 0
print(numbers2)

print('TEST_17:')
numbers = SortedList([5, 3, 4, 2, 1])
print(numbers.__add__(1))
print(numbers.__iadd__(1.1))
print(numbers.__mul__([1, 2, 3]))
print(numbers.__imul__({4, 5, 6}))