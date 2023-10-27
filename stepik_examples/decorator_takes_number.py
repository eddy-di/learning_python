import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.funct = func

    def __call__(self, *args, **kwargs):
        for i in args:
            if not isinstance(i, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        for i in kwargs:
            if not isinstance(kwargs[i], (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.funct(*args, **kwargs)

        

# tests

print()
print('TEST_1:')
@takes_numbers
def mul(a, b):
    return a * b
    
print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))

print()
print('TEST_2:')
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)

print()
print('TEST_3:')
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul('1', 2))
except TypeError as error:
    print(error)

print()
print('TEST_4:')
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul('1', '2'))
except TypeError as error:
    print(error)

print()
print('TEST_5:')
@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b='2'))
except TypeError as error:
    print(error)

print()
print('TEST_6:')
@takes_numbers
def mul(a, b=2):
    """multiplication"""
    return a * b


print(mul.__name__)
print(mul.__doc__)
print(mul(3, 4))

print()
print('TEST_7:')
print(takes_numbers)

print()
print('TEST_8:')
@takes_numbers
def mul(a, b=2):
    return a * b


print(mul(1, b=2))