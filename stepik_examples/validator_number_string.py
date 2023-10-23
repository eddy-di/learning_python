from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if self._attr in instance.__dict__:
            return instance.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')
    
    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self._attr] = value

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None) -> None:
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, item):
        if not isinstance(item, int|float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue != None and self.minvalue > item:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue != None and self.maxvalue < item:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True
    

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, item):
        if not isinstance(item, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize != None and len(item) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize != None and len(item) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate != None and not self.predicate(item):
            raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True

        
# tests


print('TEST_1:')
class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)

print('TEST_2:')
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)

print('TEST_3:')
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)

print('TEST_4:')
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)

print('TEST_5:')
class Student:
    age = Number(18)


student = Student()
student.age = 101
print(student.age)

try:
    student.age = 15
except ValueError as error:
    print(error)

print('TEST_6:')
class Student:
    age = Number(maxvalue=100)


student = Student()
student.age = 11
print(student.age)

try:
    student.age = 101
except ValueError as error:
    print(error)

print('TEST_7:')
class Student:
    age = Number(18, 99)


student = Student()
student.age = 18
print(student.age)

student.age = 99
print(student.age)

print('TEST_8:')
class Student:
    age = Number()


student = Student()
student.age = -1000
print(student.age)

student.age = 99999
print(student.age)

print('TEST_9:')
class Person:
    name = String(6, 10)


person = Person()
person.name = 'Андрей'
print(person.name)

person.name = 'Абдурахман'
print(person.name)

print('TEST_10:')
class Person:
    name = String(6, 10)


person = Person()

try:
    person.name = 'Ян'
except ValueError as e:
    print(e)


try:
    person.name = 'Аполлинария'
except ValueError as e:
    print(e)

try:
    person.name = 1
except TypeError as e:
    print(e)

print('TEST_11:')
class Person:
    name = String(6, 10, predicate=lambda x: x.startswith('А'))


person = Person()

try:
    person.name = 'Василий'
except ValueError as e:
    print(e)

print('TEST_12:')
class Person:
    name = String(6)


person = Person()
person.name = 'Пабло Диего Хосе Франциско де Паула Хуан Непомукено Криспин Криспиано де ла Сантисима Тринидад Руиз Пикассо'
print(person.name)

try:
    person.name = 'Ира'
except ValueError as e:
    print(e)

print('TEST_13:')
class Person:
    name = String(maxsize=10)


person = Person()
person.name = 'Ярик'
print(person.name)

try:
    person.name = 'Пабло Диего Хосе Франциско де Паула Хуан Непомукено Криспин Криспиано де ла Сантисима Тринидад Руиз Пикассо'
except ValueError as e:
    print(e)

print('TEST_14:')
class Person:
    name = String()


person = Person()
person.name = 'О'
print(person.name)

person.name = 'Выквырагтыргыргын Валерий'
print(person.name)

print('TEST_15:')
class PositiveNumber:
    num = Number(0)


positivenumber = PositiveNumber()
positivenumber.num = 0
print(positivenumber.num)

try:
    positivenumber.num = -1
except ValueError as e:
    print(e)

print('TEST_16:')
class Student:
    age = Number(18, 99)


student = Student()
try:
    print(student.age)
except AttributeError as e:
    print(e)

print('TEST_17:')
class Student:
    age = Number(18, 99)

print(Student.age.__class__)