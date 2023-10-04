class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.it = iter(iterable)
        self.cnt = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cnt += 1
        return next(self.it)
    
    def peek(self, default=StopIteration):
        try:
            elem = self.iterable[self.cnt]
            return elem
        except:
            if default == StopIteration:
                raise StopIteration
            else:
                return default
            

iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')
