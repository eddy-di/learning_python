class MaxCallsException(Exception):
    def __init__(self, message="Превышено количество доступных обращений"):
        super().__init__(message)

class LimitedTakes:
    def __init__(self, times):
        self._times = times
        self._call_count = 0

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._call_count >= self._times:
            raise MaxCallsException()

        self._call_count += 1

        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        self._name = self._name if hasattr(self, '_name') else None
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name
        

    

# tests

print('TEST_1:')
class Student:
    name = LimitedTakes(3)

student = Student()
print(student.__dict__)
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)
print(student.__dict__)
try:
    print(student.name)
except MaxCallsException as e:
    print(e)

print('TEST_2:')
class Student:
    name = LimitedTakes(3)

student = Student()

for _ in range(100):
    student.name = 'Gwen'
    
print(student.name)

print('TEST_3:')
class Programmer:
    name = LimitedTakes(1)


programmer = Programmer()

try:
    print(programmer.name)
except AttributeError as e:
    print(e)

print('TEST_4:')
class Programmer:
    name = LimitedTakes(1000)


programmer = Programmer()
programmer.name = 'Gvido'

for _ in range(1000):
    programmer.name

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)

print('TEST_5:')
class Student:
    name = LimitedTakes(3)


class Programmer:
    name = LimitedTakes(1)


student = Student()
programmer = Programmer()

student.name = 'Gwen'
programmer.name = 'Mantrida'

for _ in range(3):
    print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)


print(programmer.name)

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)

print('TEST_6:')
class Student:
    first_name = LimitedTakes(3)
    last_name = LimitedTakes(1)


student = Student()

student.first_name = 'Gwen'
student.last_name = 'Stacy'


for _ in range(3):
    print(student.first_name)

try:
    print(student.first_name)
except MaxCallsException as e:
    print(e)

print(student.last_name)
try:
    print(student.last_name)
except MaxCallsException as e:
    print(e)

print('TEST_7:')
class Student:
    name = LimitedTakes(3)

print(Student.name.__class__)