class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._name not in instance.__dict__:
            if self._default is None:
                raise AttributeError("Атрибут не найден")
            return self._default

        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Некорректное значение")

        instance.__dict__[self._name] = value
    

# tests

# print('TEST_1:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# student = Student()
# student.score = 90
# print(student.score)
# 
print('TEST_2:')
class Student:
    score = NonNegativeInteger('score', 0)
    print(score.__dict__)

student = Student()

# print(student.__class__.__dict__)
print(student.__dict__)
print(student.score)
print(student.__dict__)
student.score = 0
print(student.__dict__)
print(student.score)

# print('TEST_3:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# student = Student()
# 
# try:
    # print(student.score)
# except AttributeError as e:
    # print(e)
# 
# print('TEST_4:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# student = Student()
# 
# try:
    # student.score = -90
# except ValueError as e:
    # print(e)
# 
# print('TEST_5:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# student = Student()
# student.score = 90
# 
# try:
    # student.score = -90
# except ValueError as e:
    # print(e)
# 
# print('TEST_6:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# student = Student()
# 
# not_supported = [1.2, {1: 'one'}, {1, 2, 3}, [4, 5, 6], (7, 8, 9), '14']
# 
# for item in not_supported:
    # try:
        # student.score = item
    # except ValueError as e:
        # print(e)
# 
# print('TEST_7:')
# class Student:
    # score = NonNegativeInteger('score')
# 
# print(Student.score.__class__)