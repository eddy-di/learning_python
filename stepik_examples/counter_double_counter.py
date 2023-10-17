class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def __init__(self, start=0):
        super().__init__(start)

    def inc(self, n=1):
        return super().inc((n*2))
    
    def dec(self, n=1):
        return super().dec((n*2))
    

# tests 

print('TEST_1:')
print(issubclass(DoubledCounter, Counter))

print('TEST_2:')
counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

print('TEST_3:')
counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

print('TEST_4:')
digits = [47, 158, 163, 161, 65, 68, 56, 45, 66, 115, 20, 130, 108, 93, 144, 106, 106, 73, 67, 186, 158, 32, 49, 95,
          180, 169, 115, 64, 180, 163, 146, 143, 196, 143, 132, 184, 105, 38, 104, 174, 92, 169, 162, 38, 48, 29, 91,
          25, 145, 72]

counter = Counter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos


print(counter.value)

print('TEST_5:')
digits = [122, 48, 122, 180, 176, 148, 104, 70, 168, 128, 129, 120, 63, 172, 101, 132, 195, 139, 164, 163, 196, 132,
          110, 42, 183, 49, 50, 193, 198, 187, 172, 52, 113, 164, 196, 48, 114, 186, 78, 105, 82, 142, 97, 194, 74, 115,
          107, 160, 119, 82]

counter = DoubledCounter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)