class Shape:
    pass


class Polygon(Shape):
    pass


class Triangle(Polygon):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


class Quadrilateral(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Quadrilateral):
    pass


class Square(Quadrilateral):
    pass


class Circle(Shape):
    pass


# tests

print('TEST_1:')
print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))

print('TEST_2:')
print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))

print('TEST_3:')
print(issubclass(Parallelogram, Quadrilateral))
print(issubclass(Rectangle, Quadrilateral))
print(issubclass(Square, Quadrilateral))

print('TEST_4:')
print(issubclass(IsoscelesTriangle, Quadrilateral))
print(issubclass(EquilateralTriangle, Quadrilateral))

print(issubclass(Parallelogram, Triangle))
print(issubclass(Rectangle, Triangle))
print(issubclass(Square, Triangle))

print('TEST_5:')
print(issubclass(IsoscelesTriangle, Circle))
print(issubclass(EquilateralTriangle, Circle))

print(issubclass(Parallelogram, Circle))
print(issubclass(Rectangle, Circle))
print(issubclass(Square, Circle))

print('TEST_6:')
print(issubclass(Square, Shape))
print(issubclass(IsoscelesTriangle, Shape))
print(issubclass(EquilateralTriangle, Shape))
print(issubclass(Circle, Shape))