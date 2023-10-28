import re

def camel_to_snake(text):
    pattern = re.compile(r'([a-z])([A-Z])')
    snake_case = re.sub(pattern, r'\1_\2', text)
    return snake_case.lower()

def snake_case(attrs=False):
    def decorator(cls):
        if not attrs:
            class NewClass(cls):
                pass
            
            for name, attr in cls.__dict__.items():
                if not name.startswith('__') and callable(attr):
                    new_name = camel_to_snake(name)
                    setattr(NewClass, new_name, attr)

            return NewClass
        else:
            old_dict = dir(cls)
            temp = []
            for name in old_dict:
                if not name.startswith('__'):
                    temp.append(name)
            for name in temp:
                if name in cls.__dict__:
                    attribute, value = name, cls.__dict__[name]
                    new_attribute = camel_to_snake(attribute)                    
                    delattr(cls, name)
                    setattr(cls, new_attribute, value)
            return cls

    return decorator


# tests

print()
print('TEST_1:')
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1
    
    def superSecondMethod(self):
        return 2

obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())

print()
print('TEST_2:')
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)

print()
print('TEST_3:')
@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())

print()
print('TEST_4:')
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = 'John Doe'


obj = MyClass()
print(obj.MyName)

myclass_attrs = ['FirstAttr', 'superSecondAttr']

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print('атрибут отсутствует')

print()
print('TEST_5:')
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

myclass_attrs = ['FirstMethod', 'superSecondMethod']

for method in myclass_attrs:
    try:
        print(obj.__dict__[method])
    except KeyError:
        print('метод отсутствует')

print()
print('TEST_6:')
@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())