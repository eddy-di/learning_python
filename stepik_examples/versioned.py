class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        if self._attr in instance.__dict__:
            return instance.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, instance, value):
        instance.__dict__[self._attr] = value
        instance.counter = instance.counter + 1 if hasattr(instance, 'counter') else 1
        instance.__dict__[instance.counter] = value
    
    def get_version(self, instance, n: int):
        return instance.__dict__[n]

    def set_version(self, instance, n: int):
        val = instance.__dict__[n]
        instance.__dict__[self._attr] = val
        
    def set_counter(self, instance, counter=1):
        instance.counter = counter

# tests

print('TEST_1:')
class Student:
    age = Versioned()
    
student = Student()

student.age = 18
student.age = 19

print(student.age)

print('TEST_2:')
class Student:
    age = Versioned()
    
student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))

print('TEST_3:')
class Student:
    age = Versioned()
    
student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)

print('TEST_4:')
class Student:
    name = Versioned()

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

print('TEST_5:')
class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

for i in range(51):
    print(Person.age.get_version(person, i + 1))

print('TEST_6:')
class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

print(person.age)
Person.age.set_version(person, 32)
print(person.age)

print('TEST_7:')
class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 1)
print(student1.age)
print(student2.age)

print('TEST_8:')
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

print('TEST_9:')
class Student:
    age = Versioned()

print(Student.age.__class__)