class ArithmeticProgression:
    def __init__(self, start: int, increment: int):
        self.start = start
        self.increment = increment
        self.value = 0
        self.iteration = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iteration == 0:
            self.value = self.start
        else:
            self.value += self.increment 
        self.iteration += 1
        return self.value

class GeometricProgression:
    def __init__(self, start: int, increment: int):
        self.start = start
        self.increment = increment
        self.value = 0
        self.iteration = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iteration == 0:
            self.value = self.start
        else:
            self.value *= self.increment 
        self.iteration += 1
        return self.value


# tests

print()
print('TEST_1:')
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print()
print('TEST_2:')
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print()
print('TEST_3:')
progression = ArithmeticProgression(0, -1)

for _ in range(20):
    print(next(progression), end=' ')

print()
print('TEST_4:')
progression = GeometricProgression(4, -2)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print()
print('TEST_5:')
progression = ArithmeticProgression(100, -10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print()
print('TEST_6:')
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print()
print('TEST_7:')
progression = GeometricProgression(2, 2)

for _ in range(20):
    print(next(progression), end=' ')