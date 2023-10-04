class AttrsIterator:
    def __init__(self, obj):
        self.obj_attrs = [(k, v) for k, v in obj.__dict__.items()]
        self.count = -1

    def __iter__(self):
        yield from self.obj_attrs

    def __next__(self):
        if self.__next__ and self.count == len(self.obj_attrs)-1:
            raise StopIteration
        self.count += 1
        return self.obj_attrs[self.count]

        

class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))