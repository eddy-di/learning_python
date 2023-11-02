from typing import Any

class Anything:
    def __lt__(self, other: Any):
            return True
    
    def __gt__(self, other: Any):
            return True
    
    def __ne__(self, other: Any):
            return True
    
    def __eq__(self, other: Any):
            return True
    
    def __ge__(self, other: Any):
            return True
    
    def __le__(self, other: Any):
            return True

def anything():
    obj = Anything()
    return obj

# tests


print()
print('TEST_1:')
import math, re

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)

print()
print('TEST_2:')
print(anything() != set())
print(anything() < {})
print(anything() > ())
print(anything() >= True)
print(anything() <= False)
print(anything() == id)

print()
print('TEST_3:')
print(anything() != (1, 2, 3))
print(anything() < {4, 5, 6})
print(anything() > range(180))
print(anything() >= {1: 'one'})
print(anything() <= ['', [], (), set])
print(anything() == any)
print(anything() != any)
print(anything() > any)
print(anything() < all)
print(anything() <= all)
print(anything() >= all)

print()
print('TEST_4:')
print(anything() == filter)
print(anything() != filter)
print(anything() < filter)
print(anything() > filter)
print(anything() >= filter)
print(anything() <= filter)
print(anything() == anything())
print(anything() != anything())
print(anything() < anything())
print(anything() > anything())
print(anything() >= anything())
print(anything() <= anything())