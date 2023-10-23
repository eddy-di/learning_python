class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = 'strict'


class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, honey!'
    
    def be_kind(self):
        self.mood = 'kind'


class Daughter(Mother, Father):
    def __init__(self, mood='neutral'):
        super().__init__(mood)

    def greet(self):
        return Mother().greet()
    
    def be_kind(self):
        return super().be_kind()
    
    def be_strict(self):
        return super().be_strict()
    

class Son(Mother, Father):
    def __init__(self, mood='neutral'):
        super().__init__(mood)

    def greet(self):
        return Father().greet()
    
    def be_kind(self):
        return super().be_kind()
    
    def be_strict(self):
        return super().be_strict()
    

# tests

print('TEST_1:')
father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())

print('TEST_2:')
father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)

print('TEST_3:')
daughter = Daughter()

print(daughter.greet())
print(daughter.mood)
daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)

print('TEST_4:')
son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)