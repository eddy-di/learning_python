from keyword import kwlist

class NonKeyword:
    not_accepted_names = kwlist

    def __init__(self, name):
        self._name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')
        
    def __set__(self, obj, value):
        if value not in kwlist:
            obj.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')


# tests


print('TEST_1:')
class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)

print('TEST_2:')
class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

print('TEST_3:')
class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)

print('TEST_4:')
class Student:
    name = NonKeyword('name')

student = Student()

try:
    student.name = 'class'
except ValueError as e:
    print(e)

print('TEST_5:')
from keyword import kwlist

class Student:
    name = NonKeyword('name')

student = Student()

for kw in kwlist:
    try:
        student.name = kw
    except ValueError as e:
        print(e)

print('TEST_6:')
class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)

print('TEST_7:')
class Student:
    name = NonKeyword('name')

print(Student.name.__class__)