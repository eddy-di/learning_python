from random import randrange

class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides

    def __call__(self):
        return randrange(1, self.sides + 1)
    

kingdice = Dice(20)
print(callable(kingdice))