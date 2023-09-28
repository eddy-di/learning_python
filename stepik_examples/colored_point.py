class ColoredPoint:
    def __init__(self, x: int|float, y: int|float, color: tuple=(0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)
    
    def __neg__(self):
        return self.__class__(-1 * self.x, -1 * self.y, self.color)
    
    def __invert__(self):
        return self.__class__(self.y, self.x, tuple(255 - i for i in self.color))

    
point = ColoredPoint(0, 0, (0, 0, 0))

print(f'{+point}; {-point}; {~point}')
print(point.color)

