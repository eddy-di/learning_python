from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable):
        super().__init__(i for i in iterable)
        self.__check_list(self.data)
        
    def __setitem__(self, index, item):
        if self.__check(item):
            self.data[index] = item

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data + other.data)
        if isinstance(other, list):
            if self.__check_list(other):
                return self.__class__(self.data + other)

    def __radd__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(other.data + self.data)

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.data += other.data
        if isinstance(other, list):
            if self.__check_list(other):
                self.data += other
        return self
    
    def append(self, item):
        if self.__check(item):
            self.data.append(item)

    def insert(self, i, item):
        if isinstance(item, int|float):
            self.data.insert(i, item)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
    
    def extend(self, other):
        if isinstance(other, list):
            if self.__check_list(other):
                self.data.extend(other)
        elif isinstance(other, self.__class__):
            if self.__check_list(other.data):
                self.data.extend(other.data)
        else:
            if self.__check(other):
                self.data.extend(other)
        
    @staticmethod
    def __check(value):
        if not isinstance(value, int|float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return value
    
    @staticmethod
    def __check_list(iterable):
        for i in iterable:
            if not isinstance(i, int|float):
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
            pass
        return iterable
    


# Tests

# print('TEST_1:')
# numberlist = NumberList([1, 2])
# 
# numberlist.append(3)
# numberlist.extend([4, 5])
# numberlist.insert(0, 0)
# print(numberlist)
# 
# print('TEST_2:')
# numberlist = NumberList([0, 1.0])
# 
# numberlist[1] = 1
# numberlist = numberlist + NumberList([2, 3])
# numberlist += NumberList([4, 5])
# print(numberlist)
# 
# print('TEST_3:')
# try:
    # numberlist = NumberList(['a', 'b', 'c'])
# except TypeError as error:
    # print(error)
# 
# print('TEST_4:')
# numberlist = NumberList([1, 2, 3])
# 
# try:
    # numberlist.append('4')
# except TypeError as error:
    # print(error)
# 
# print('TEST_5:')
# numberlist = NumberList([1, 2])
# 
# try:
    # numberlist += [3, '4']
# except TypeError as e:
    # print(e)
# 
# print('TEST_6:')
# numberlist1 = NumberList([1, 2])
# 
# try:
    # numberlist2 = numberlist1 + [3, '4']
# except TypeError as e:
    # print(e)
# 
# print('TEST_7:')
# data = [1, 2, 3]
# numberlist = NumberList(data)
# 
# print(numberlist)
# 
# data.extend([4, 5, 6])
# print(data)
# print(numberlist)
# 
print('TEST_8:')
numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)

print('TEST_9:')
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, '4', 3])
except TypeError as e:
    print(e)

print('TEST_10:')
n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)