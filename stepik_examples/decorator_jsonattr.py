import json


def jsonattr(file):
    with open(file) as f:
        data = f.read()
    parsed = json.loads(data)
    def decorator(cls):
        for k in parsed:
            setattr(cls, k, parsed[k])
        return cls
    return decorator

# tests

print()
print('TEST_1:')
with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)

print()
print('TEST_2:')
with open('test.json', 'w') as file:
    file.write('{"name": "John", "surname": "Doe"}')


@jsonattr('test.json')
class Person:
    pass


print(Person.name)
print(Person.surname)

print()
print('TEST_3:')
with open('test.json', 'w') as file:
    file.write('{"name": "Кемаль", "breed": "Британский"}')


@jsonattr('test.json')
class Cat:
    def __init__(self, name=None, breed=None):
        self.name = name or self.name
        self.surname = breed or self.breed


cat = Cat()
print(cat.name)
print(cat.breed)

print()
print('TEST_4:')
with open('test.json', 'w') as file:
    file.write('{"shoot1": "pif", "shoot2": "paf"}')


@jsonattr('test.json')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()