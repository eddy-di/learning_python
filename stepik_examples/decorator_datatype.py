import functools


class returns:
    def __init__(self, datatype):
        self.dataype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs) 
            if not isinstance(value, self.dataype):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper
    

# tests

print()
print('TEST_1:')
@returns(int)
def add(a, b):
    return a + b

print(add(1, 2))

print()
print('TEST_2:')
@returns(int)
def add(a, b):
    return a + b

try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))

print()
print('TEST_3:')
@returns(list)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))

print()
print('TEST_4:')
@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))

print()
print('TEST_5:')
@returns(tuple)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2, 3], [4, 5, 6]))
except TypeError as e:
    print(type(e))

print()
print('TEST_6:')
@returns(int)
def add(a, b):
    return a + b

print(add(a=10, b=5))