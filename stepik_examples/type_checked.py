class TypeChecked:
    def __init__(self, *args):
        self._args = args

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if type(value) not in self._args:
            raise TypeError('Некорректное значение')
        instance.__dict__[self._name] = value

    def __set_name__(self, cls, name):
        self._name = name

# tests

print('TEST_1:')
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

print(student.name)

print('TEST_2:')
class Student:
    name = TypeChecked(str)

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

print('TEST_3:')
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)

print('TEST_4:')
class Student:
    age = TypeChecked(int, float)

student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)

print('TEST_5:')
class Vector:
    x = TypeChecked(float)
    y = TypeChecked(float)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

pairs = [('12', '89'), ([1, 2], [3, 4]), ({1: 2}, {3: 4}), (True, False), (1.2, 3.4)]

for x, y in pairs:
    try:
        vector = Vector(x, y)
        print(vector)
    except TypeError as e:
        print(e)

print('TEST_6:')
class Student:
    name = TypeChecked(str)

print(Student.name.__class__)