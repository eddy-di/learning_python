class Pet:
    counter = 0
    name = []
    def __init__(self, name=None) -> None:
        self.name = name
        if self.name != None:
            Pet.counter += 1
            Pet.name.append(self)

    @classmethod
    def first_pet(cls):
        if len(cls.name) > 0:
            return cls.name[0]
        else:
            return None
    
    @classmethod
    def last_pet(cls):
        if len(cls.name) > 0:
            return cls.name[-1]
        else:
            return None
    
    @classmethod
    def num_of_pets(cls):
        return cls.counter
    

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet4 = Pet('Ratchet')
pet5 = Pet('Ratchet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())