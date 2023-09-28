from functools import singledispatchmethod

class Vector:
    @singledispatchmethod
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @__init__.register(int)
    @__init__.register(float)
    def _int_float_coords(self, x, y):
        self.x = x
        self.y = y

    # @__init__.register(tuple)
    # def _tuple_coords(self, data):
        # self.x = data[0]
        # self.y = data[1]
    
    # def __str__(self):
        # return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented
    
vector = Vector(0, 1)

print(vector.__eq__(1))
print(vector.__ne__(1.1))
# print(vector.__gt__(range(5)))
# print(vector.__lt__([1, 2, 3]))
# print(vector.__ge__({4, 5, 6}))
# print(vector.__le__({1: 'one'}))


