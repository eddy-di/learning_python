class Vehicle:
    '''An example of a Vehicle class'''

    def __init__(self, max_speed: int, milage: int, model: str):
        self.max_speed = max_speed
        self.milage = milage
        self.model = model


car = Vehicle(190, 100, 'Tesla')

print(car.max_speed)
print(car.milage)
print(car.model)