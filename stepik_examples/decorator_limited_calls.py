import functools


class MaxCallsException(Exception):
    def __init__(self, message='Превышено допустимое количество вызовов') -> None:
        super().__init__(message)


class limited_calls:
    def __init__(self, n: int) -> None:
        self.n = n
        self.counter = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.counter += 1
            if args and self.counter <= self.n:
                return func(*args, **kwargs)
            else: 
                raise MaxCallsException
        return wrapper

            
    

# tests


print('TEST_1:')
@limited_calls(3)
def add(a, b):
    return a + b
    
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)

print()
print('TEST_2:')
import random


@limited_calls(5)
def positive_sum(*args):
    return sum(args)


for _ in range(4):
    positive_sum(*(random.randint(1, 100) for _ in range(10)))

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

try:
    print(positive_sum(10, 124, 124, 786, 11))
except MaxCallsException as e:
    print(e)

print()
print('TEST_3:')
@limited_calls(5)
def concat(a, b, c):
    return a + b + c


for _ in range(5):
    print(concat('123', '456', '789'))

try:
    print(concat('123', '456', '789'))
except MaxCallsException as e:
    print(e)

print()
# print('TEST_4:')
# @limited_calls(10)
# def power(a, n):
    # return a ** n
# 
# 
# for _ in range(10):
    # power(2, 3)
# 
# try:
    # print(power(2, 3))
# except MaxCallsException as e:
    # print(e)
# 
print()
print('TEST_5:')
@limited_calls(10)
def power(a, n):
    """degree"""
    return a ** n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))