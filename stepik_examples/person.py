class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def set_name(self, name: str):
        self.name = name

    def set_surname(self, surname: str):
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'
    
    def set_fullname(self, text: str):
        splitted = text.split()
        self.set_name(splitted[0])
        self.set_surname(splitted[1])

    fullname = property(fget=get_fullname, fset=set_fullname)


person = Person('Брайан', 'Керниган')
print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))