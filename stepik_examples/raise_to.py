class RaiseTo:
    def __init__(self, power) -> None:
        self.degree = power

    def __call__(self, x):
        return x ** self.degree
    
raise_to_three = RaiseTo(3)
raise_to_four = RaiseTo(4)

print(raise_to_three(3))
print(raise_to_four(2))