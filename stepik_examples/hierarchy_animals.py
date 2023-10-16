class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass


# tests

print('TEST_1:')
print(issubclass(Fish, Animal))
print(issubclass(Bird, Animal))
print(issubclass(FlyingBird, Animal))
print(issubclass(FlyingBird, Bird))

print('TEST_2:')
animal = Animal()

print(animal.sleep())
print(animal.eat())

print('TEST_3:')
fish = Fish()

print(fish.sleep())
print(fish.eat())
print(fish.swim())

print('TEST_4:')
bird = Bird()
print(bird.sleep())
print(bird.eat())
print(bird.lay_eggs())

print('TEST_5:')
flying_bird = FlyingBird()
print(flying_bird.sleep())
print(flying_bird.eat())
print(flying_bird.lay_eggs())
print(flying_bird.fly())

print('TEST_6:')
animal = Animal()

methods = ['swim', 'lay_eggs', 'fly']
for method in methods:
    print(hasattr(animal, method))