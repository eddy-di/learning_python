from random import randrange

class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool=False):
        self._start = start
        self._end = end
        self.cache = cache

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if self.cache == False:
            return randrange(self._start, self._end + 1)
        return self._start
    
    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')
    

# tests


print('TEST_1:')
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])

print('TEST_2:')
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])

print('TEST_3:')
class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)

print('TEST_4:')
class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)

print('TEST_5:')
class MagicPoint:
    x = RandomNumber(20, 100, True)


magicpoint = MagicPoint()

value = magicpoint.x

for _ in range(20):
    print(magicpoint.x == value)

print('TEST_6:')
class MagicPoint:
    x = RandomNumber(-1000, 1000)

magicpoint = MagicPoint()

for _ in range(50):
    print(magicpoint.x in range(-1000, 1001))

print('TEST_7:')
class MagicPoint:
    x = RandomNumber(-1000, 1000)

    def __init__(self, x):
        self.x = x


try:
    magicpoint = MagicPoint(150)
except AttributeError as e:
    print(e)

print('TEST_8:')
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

print(MagicPoint.x.__class__)
print(MagicPoint.y.__class__)
print(MagicPoint.z.__class__)