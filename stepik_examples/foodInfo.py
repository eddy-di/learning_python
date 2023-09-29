class FoodInfo:
    def __init__(self, proteins, fats, carbs):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbs

    def __repr__(self):
        return f'{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return __class__(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return __class__(self.proteins * num, self.fats * num, self.carbohydrates * num)
        return NotImplemented
        
    def __truediv__(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return __class__(self.proteins / num, self.fats / num, self.carbohydrates / num)
        return NotImplemented
    
    def __floordiv__(self, num):
        if isinstance(num, int) or isinstance(num, float):
            return __class__(self.proteins // num, self.fats // num, self.carbohydrates // num)
        return NotImplemented


food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
    