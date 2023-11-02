import functools
from typing import Any


class predicate:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        value = self.func(*args, **kwargs)
        return value
    
    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))
    
    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))
    
    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self.func(*args, **kwargs))
    

# tests

print()
print('TEST_1:')
@predicate
def to_be():
    return True

print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()

@predicate
def is_equal(a, b):
    return a == b

@predicate
def is_less_than(a, b):
    return a < b

print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)

print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)

print()
print('TEST_2:')
@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0

print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
print((~is_even & is_positive)(3))            # True; равнозначно not is_even(4) and is_positive(4)

print()
print('TEST_3:')
@predicate
def is_less_than(a, b):
    return a < b

print(is_less_than(1, 2))
print(is_less_than(2, 2))
print(is_less_than(3, 2))

print()
print('TEST_4:')
@predicate
def char_in_word(char, word):
    return char in word


print(char_in_word('e', 'beegeek'))
print((~char_in_word & char_in_word)('e', 'beegeek'))
print((char_in_word | ~char_in_word)(word='beegeek', char='e'))

print()
print('TEST_5:')
@predicate
def is_arithmetic_mean(iterable):
    result = {iterable[i + 1] - iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


@predicate
def is_geometric_mean(iterable):
    result = {iterable[i + 1] // iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


print(is_arithmetic_mean([1, 2, 3, 4, 5]))
print(is_geometric_mean([1, 2, 4, 8, 16]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 3, 4, 5]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 3, 4, 5]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 4, 8, 16]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 4, 8, 16]))

print((~is_arithmetic_mean & ~is_geometric_mean)([1, 2, 4, 5]))
print((~is_arithmetic_mean | ~is_geometric_mean)([1, 2, 3, 4, 5]))

