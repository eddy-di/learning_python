from math import pi
from functools import lru_cache

class Circle:
    @lru_cache
    def __init__(self, radius: float):
        self._radius = radius
        self._diameter = self._radius * 2
        self._area = pi * self._radius**2

    def get_radius(self):
        return self._radius
    
    def get_diameter(self):
        return self._diameter
    
    def get_area(self):
        return self._area
    

circle = Circle(10)
print(hasattr(circle, '_radius'))
print(hasattr(circle, '_diameter'))
print(hasattr(circle, '_area'))
print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))