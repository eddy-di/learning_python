class AdvancedList(list):
    def __init__(self, iterable):
        super().__init__(iterable)
    
    def join(self, delimiter=' '):
        return delimiter.join(map(str, self))
    
    def __setitem__(self, index, item):
        super().__setitem__(index, item)
    
    def map(self, func):
        self = [self.__setitem__(i, func(self[i])) for i in range(len(self))]
        return self
    
    def filter(self, func):
        super().__init__([self[i] for i in range(len(self)) if func(self[i])])
        return self




# tests

print('TEST_1:')
advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join('-'))

print('TEST_2:')
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)

print('TEST_3:')
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)

print('TEST_4:')
advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)

print('TEST_5:')
advancedlist = AdvancedList([1, 2, 3, 4, 5])
separators = [' - ', ' + ', ' = ', ' * ', ' / ', ' ! ', ' 0 ', ' & ', ' ^ ', ' -> ']

for separator in separators:
    print(advancedlist.join(separator))

print('TEST_6:')
advancedlist = AdvancedList(['hello', 'Gvido', 'how', 'are', 'you'])
advancedlist.map(len)
print(advancedlist)

