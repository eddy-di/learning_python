def auto_repr(**kwargs):
    def wrapper(cls):
        arg = kwargs['args']
        kwarg = kwargs['kwargs']
        def set_repr(self):
            temp_args = []
            for k, v in self.__dict__.items():
                if k in arg:
                    temp_args.append(f'{self.__dict__[k]!r}')
                if k in kwarg:
                    dict_key = f'{k}={v!r}'
                    temp_args.append(dict_key)
            res = ", ".join(map(str, temp_args))
            return f'{cls.__name__}({res})'
        
        cls.__repr__ = set_repr
        
        return cls
    return wrapper

# tests

print()
print('TEST_1:')
@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)

point.x = 10
point.y = 20
print(point)

print()
print('TEST_2:')
@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')

print(person)

print()
print('TEST_3:')
@auto_repr(args=[], kwargs=['name', 'breed'])
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


cat = Cat('Кемаль', 'Британский')

print(cat)

print()
print('TEST_4:')
@auto_repr(args=[], kwargs=[])
class Gun:
    pass


gun = Gun()

print(gun)