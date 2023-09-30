class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.modulus = (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __bool__(self):
        return self.x > 0 or self.y > 0
    
    def __int__(self):
        return int(self.modulus)
    
    def __float__(self):
        return float(self.modulus)
    
    def __complex__(self):
        return complex(self.x, self.y)
    

print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))