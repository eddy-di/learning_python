import functools


class ignore_exception:
    def __init__(self, *args):
        self.exceptions = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except self.exceptions as e:
                    print(f'Исключение {e.__class__.__name__} обработано')
            except Exception as e:
                raise e
        return wrapper
            
# tests

print()
print('TEST_1:')
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x
    
func(0)

print()
print('TEST_2:')
min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))

print()
print('TEST_3:')
@ignore_exception()
def func():
    raise ValueError
  
try:    
    func()
except Exception as error:
    print(type(error))

print()
print('TEST_4:')
@ignore_exception(TypeError)
def func():
    raise ValueError
  
try:    
    func()
except Exception as error:
    print(type(error))

print()
print('TEST_5:')
@ignore_exception(ValueError, TypeError, NameError)
def func():
    raise NameError
 
try:    
    func()
except Exception as error:
    print(type(error))

print()
print('TEST_6:')
@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def func():
    raise ZeroDivisionError
 
try:    
    func()
except Exception as error:
    print(type(error))

print()
print('TEST_7:')
@ignore_exception(ValueError, NameError, ZeroDivisionError, TypeError)
def func(a, b, c):
    raise NameError
 
try:    
    func(1, 2, c=10)
except Exception as error:
    print(type(error))

print()
print('TEST_8:')
@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    """beegeek"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())