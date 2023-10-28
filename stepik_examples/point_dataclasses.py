from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = 0

    def __post_init__(self):
        if self.x == 0.0 or self.y == 0.0:
            self.quadrant = 0
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4

    def symmetric_x(self):
        return self.__class__(x=self.x,  y=(-1 * self.y))
    
    def symmetric_y(self):
        return self.__class__(x=(-1 * self.x), y=self.y)
    

# tests

print()
print('TEST_1:')
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

print()
print('TEST_2:')
point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())

print()
print('TEST_3:')
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)

print()
print('TEST_4:')
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point)

print()
print('TEST_5:')
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_x())

print()
print('TEST_6:')
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_y())