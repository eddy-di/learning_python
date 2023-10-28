import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)
    
    cls.__init__ = new_init
    return cls


#tests

print()
print('TEST_1:')
@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


obj1 = Person('object 1')
obj2 = Person('object 2')

print(Person.instances)

print()
print('TEST_2:')
@track_instances
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'Cat({self.name!r}, {self.breed!r})'


for _ in range(10):
    cat = Cat('Кемаль', 'Британский')

print(len(Cat.instances))

print()
print('TEST_3:')
@track_instances
class Gun:
    def __repr__(self):
        return 'Gun()'


for _ in range(10000):
    cat = Gun()

print(len(Gun.instances))
print(Gun.instances[3245])