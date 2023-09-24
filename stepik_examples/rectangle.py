class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        self._perimeter = (self.length + self.width) * 2
        return self._perimeter
    
    def get_area(self):
        self._area = self.length * self.width
        return self._area
    
    perimeter = property(fget=get_perimeter)
    area = property(fget=get_area)



rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')