from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.custom_range = []
        for el in args:
            if isinstance(el, int):
                self.custom_range.append(el)
            elif isinstance(el, str) and '-' in el:
                a, b = el.split('-')
                temp = []
                for i in range(int(a), int(b) + 1):
                    temp.append(i)
                self.custom_range += temp

    def __len__(self):
        return len(self.custom_range)
    
    def __getitem__(self, key):
        return self.custom_range[key]
    

# tests

print('TEST_1:')
customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])

print('TEST_2:')
customrange = CustomRange(1, '2-5', 3, '1-4')

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)

print('TEST_3:')
customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))

print('TEST_4:')
customrange = CustomRange('0-1000')

print(len(customrange))
print(*customrange)

print('TEST_5:')
customrange = CustomRange('0-50', '25-75', '50-100')

for digit in customrange:
    print(digit, end=' ')

print('TEST_6:')
customrange = CustomRange(1, 212, '89-323', 87, '17-82', 124, '300-312', 832, 1234)

print(*customrange)
print(customrange[11])
print(customrange[44])
print(customrange[-12])
print(customrange[-38])
print(82 in customrange)
print(17 in customrange)