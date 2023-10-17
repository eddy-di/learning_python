from typing import Any


class FieldTracker:
    fields = ...
    history = {}
    changed_res = {}

    def __init__(self, *args):
        pass
    
    def base(self, attr_name):
        if len(self.history[attr_name]) > 1:
            return self.history[attr_name][0]
        elif len(self.history[attr_name]) == 1:
            return self.__dict__[attr_name]
    
    def has_changed(self, attr_name):
            return True if len(self.history[attr_name]) > 1 else False
        
    def changed(self):
        for key in self.history.keys():
            if len(self.history[key]) > 1:
                self.changed_res[key] = self.history[key][0]
            pass
        return self.changed_res

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value
        if __name in self.history:
            self.history[__name].append(__value)
        elif __name not in self.history:
            self.history[__name] = [__value]

    def save(self):
        for k in self.__dict__.keys():
            self.history[k] = [self.__dict__[k]]
        self.__dict__['changed_res'] = {}
        

    


print('TEST_1:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())

print('TEST_2:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

print('TEST_3:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

print('TEST_4:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())

print('TEST_5:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.x = 4
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.z = 6
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.y = 8
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))

print('TEST_6:')
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.base('x'))
p.x = 4
print(p.base('x'))
print(p.x)
p.z = 6
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.save()
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.y = 8
print(p.base('y'))
print(p.y)
p.save()
print(p.base('y'))