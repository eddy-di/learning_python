import functools


class type_check:
    def __init__(self, types_list: list):
        self.types = types_list

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for_check = zip(args, self.types)
            for i in for_check:
                if not isinstance(i[0], i[1]):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    

# tests

print()
print('TEST_1:')
@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))

print()
print('TEST_2:')
@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))

print()
print('TEST_3:')
@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))

print()
print('TEST_4:')
@type_check([int, int])
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3.0))

print()
print('TEST_5:')
@type_check([])
def add(a, b):
    return a + b


print(add(1, 2))

print()
print('TEST_6:')
@type_check([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))
