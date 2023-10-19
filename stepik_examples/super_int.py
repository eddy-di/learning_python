class SuperInt(int):
    def __new__(cls, value):
        return super().__new__(cls, value)
    
    def __init__(self, num: int):
        self.initial = num
        self.num = str(abs(num))
    
    def repeat(self, num=2):
        res = str(self.initial) + (self.num * (num - 1))
        return self.__class__(int(res))
    
    def to_bin(self):
        res = bin(self)
        if res[0] == '-' and res[1:3] == '0b':
            res = res[0] + res[3:]
        else:
            res = res[2:]
        return res

    def next(self):
        res = self.initial + 1
        return self.__class__(res)
    
    def prev(self):
        res = self.initial - 1
        return self.__class__(res)

    def __len__(self):
        res = [c for c in self.num]
        return len(res)
    
    def __iter__(self):
        return (self.__class__(int(c)) for c in self.num)


# tests


print('TEST_1:')
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

print('TEST_2:')
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

print('TEST_3:')
superint = SuperInt(17)

print(superint.prev())
print(superint.next())

print('TEST_4:')
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)

print('TEST_5:')
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
superint = SuperInt(30)

for n in digits:
    print(superint.repeat(n))

print('TEST_6:')
superint = SuperInt(30)

for i in range(10):
    superint = superint.next()
    print(superint)

print('TEST_7:')
superint = SuperInt(30)

for i in range(10):
    superint = superint.prev()
    print(superint)

print('TEST_8:')
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(superint.to_bin())

print('TEST_9:')
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(superint.to_bin())

print('TEST_10:')
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(*superint)

print('TEST_11:')
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(*superint)

print('TEST_12:')
superint = SuperInt(100)
print(type(superint))
print(type(superint.next()))
print(type(superint.prev()))
print(type(superint.repeat()))

print('TEST_13:')
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))