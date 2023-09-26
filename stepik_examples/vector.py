class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'