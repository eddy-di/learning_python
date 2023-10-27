import functools
from typing import Any


# def reverse_args(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args = reversed(args)
#         return func(*args, **kwargs)
#     return wrapper

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        args = reversed(args)
        return self.func(*args, **kwds)
    
# tests

print()
print('TEST_1:')
@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))

print()
print('TEST_2:')
@reverse_args
def concat(a, b, c):
    return a + b + c
    
print(concat('apple', 'cherry', 'melon'))

print()
print('TEST_3:')
@reverse_args
def operation(a, b, c):
    return a // b + c
    
print(operation(10, 20, 80))

print()
print('TEST_4:')
@reverse_args
def operation(a, b):
    """integer division"""
    return a // b


print(operation.__name__)
print(operation.__doc__)
print(operation(90, 0))

print()
print('TEST_5:')
@reverse_args
def operation(a, b):
    return a // b

try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

print()
print('TEST_6:')
@reverse_args
def operation(a, b, name):
    return a // b + name
    
print(operation(10, 90, name=1))

print()
print('TEST_7:')
@reverse_args
def operation(a, b, value=10):
    return a // b + value

try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

print()
print('TEST_8:')
@reverse_args
def operation(a, b, value1=10, value2=30):
    return a // b - value1 + value2

print(operation(140, 70, value1=50, value2=100))

print()
print('TEST_9:')
print(reverse_args)
print(type(reverse_args))