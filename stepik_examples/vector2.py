class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
     
    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    

coordinates = [(-2, -12), (-78, -22), (-90, 58), (10, -37), (25, 60)]
vectors = [Vector(x, y) for x, y in coordinates]
print(vectors)