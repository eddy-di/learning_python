class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.iterable = list((self.x, self.y, self.z))

    def __iter__(self):
        yield from self.iterable

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'
    
points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
print(points)