class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
    @fullname.setter
    def fullname(self, text):
        splitted = text.split()
        self.name = splitted[0]
        self.surname = splitted[1]

person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)


