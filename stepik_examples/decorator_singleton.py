import functools

def singleton(cls):
    cls.attr = None
    old_new = cls.__new__
    old_init = cls.__init__

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        if cls.attr is None:
            cls.attr = super(cls, cls).__new__(cls)
        return cls.attr

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)

    cls.__init__ = new_init
    cls.__new__ = new_new  # Assign the modified __new__ method

    return cls


# tests

print()
print('TEST_1:')
@singleton
class MyClass:
    pass
    
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)

print()
print('TEST_2:')
@singleton
class MyClass:
    pass


instances = [MyClass() for _ in range(100)]
obj = MyClass()
print(all(instance is obj for instance in instances))

print()
print('TEST_3:')
@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))