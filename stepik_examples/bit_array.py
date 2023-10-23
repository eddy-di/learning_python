from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = iterable[:]

    def __str__(self):
        return str(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key]
    
    def __len__(self):
        return len(self.iterable)
    
    def __invert__(self):
        temp = self.iterable[:]
        for i in range(len(temp)):
            if temp[i] == 1:
                temp[i] = 0
            elif temp[i] == 0:
                temp[i] = 1
        return self.__class__(temp)
    
    def __and__(self, other):
        temp = []
        if isinstance(other, self.__class__):
            for i in range(len(self.iterable)):
                if self.iterable[i] == 1 and other.iterable[i] == 1:
                    temp.append(1)
                else:
                    temp.append(0)
            return self.__class__(temp)
        return NotImplemented
    
    def __or__(self, other):
        temp = []
        if isinstance(other, self.__class__):
            for i in range(len(self.iterable)):
                if self.iterable[i] == 1 or other.iterable[i] == 1:
                    temp.append(1)
                else:
                    temp.append(0)
            return self.__class__(temp)
        return NotImplemented


#tests

# print('TEST_1:')
# bitarray = BitArray([1, 0, 1, 1])
# 
# print(bitarray)
# print(~bitarray)
# print(bitarray[0])
# print(bitarray[1])
# print(bitarray[-1])
# print(0 in bitarray)
# print(1 not in bitarray)
# 
# print('TEST_2:')
# bitarray1 = BitArray([1, 0, 1, 1])
# bitarray2 = BitArray([0, 0, 0, 1])
# 
# bitarray3 = bitarray1 | bitarray2
# bitarray4 = bitarray1 & bitarray2
# bitarray5 = ~bitarray1
# 
# print(bitarray3, type(bitarray3))
# print(bitarray4, type(bitarray4))
# print(bitarray5, type(bitarray5))
# 
# print('TEST_3:')
# data = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1,
        # 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
# 
# bitarray = BitArray(data)
# 
# print(*bitarray)
# print(*reversed(bitarray))
# print(~bitarray)
# 
# print('TEST_4:')
# data = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
        # 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
# 
# bitarray = BitArray(data)
# 
# print(bitarray)
# data.extend([0, 0, 1, 0, 1, 1])
# 
# print(data)
# print(bitarray)
# 
print('TEST_5:')
data1 = [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]

data2 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1,
        1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]

bitarray1 = BitArray(data1)
bitarray2 = BitArray(data2)


print(len(bitarray1) == len(bitarray2))
print(bitarray1 | bitarray2)
print(bitarray1 & bitarray2)

print('TEST_6:')
bitarray = BitArray([1, 0, 1, 1])
print(bitarray.__or__(1))
print(bitarray.__and__(1.1))

print('TEST_7:')
bitarray = BitArray()
print(bitarray)