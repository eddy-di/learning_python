class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x + other.x, self.y + other.y)
        return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.x - other.x, self.y - other.y)
        return NotImplemented
        
    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return self.__class__(self.x * num, self.y * num)
        return NotImplemented
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __truediv__(self, num):
        if isinstance(num, (int, float)):
            return self.__class__(self.x / num, self.y / num)
        return NotImplemented
    
    def __rtruediv__(self, num):
        return self.__truediv__(num)
    
    def __floordiv__(self, num):
        if isinstance(num, (int, float)):
            return self.__class__(self.x // num, self.y // num)
        return NotImplemented
    
    def __rfloordiv__(self, num):
        return self.__floordiv__(num)
    


a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)

