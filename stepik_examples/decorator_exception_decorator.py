import functools
from typing import Any


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            value = self.func(*args, **kwds)
            return value, None
        except Exception as e:
            return None, type(e)
        
    
# tests

print()
print('TEST_1:')
@exception_decorator
def func(x):
    return 2*x + 1
    
print(func(1))
print(func('bee'))

print()
print('TEST_2:')
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 10))

print()
print('TEST_3:')
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 'stepik'))

print()
print('TEST_4:')
@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(f(1, 2, 3, param1=4, param2=10))

print()
print('TEST_5:')
@exception_decorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2='10'))

print()
print('TEST_6:')
sum = exception_decorator(sum)

print(sum(['199', '1', 187]))