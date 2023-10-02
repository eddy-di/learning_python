class ColoredPoint:
    def __init__(self, x: int|float, y: int|float, color: str) -> None: # color: tuple=(0, 0, 0)
        self._x = x
        self._y = y
        self._color = color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, '{self.color}')"
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)
    
    def __neg__(self):
        return self.__class__(-1 * self.x, -1 * self.y, self.color)
    
    # def __invert__(self):
        # return self.__class__(self.y, self.x, tuple(255 - i for i in self.color))

    def __eq__(self, __value) -> bool:
        if isinstance(__value, self.__class__):
            return self.x == __value.x and self.y == __value.y and self.color == __value.color
        return NotImplemented
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def color(self):
        return self._color
        
    @property
    def attrs(self):
        return self.x, self.y, self.color
    
    def __hash__(self) -> int:
        return hash(self.attrs)

    
coloredpoint = ColoredPoint(1, 2, 'yellow')

# try:
    # coloredpoint.x = 2
# except AttributeError as e:
    # print(type(e))
# 
# try:
    # coloredpoint.y = 3
# except AttributeError as e:
    # print(type(e))
# 
# try:
    # coloredpoint.color = 'black'
# except AttributeError as e:
    # print(type(e))
