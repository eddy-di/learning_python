class NonNegativeObject:
    def __init__(self, **kwargs):
        for a in kwargs.keys():
            if isinstance(kwargs[a], int|float) and kwargs[a] < 0 :
                self.__dict__[a] = abs(kwargs[a])
            else:
                self.__dict__[a] = kwargs[a]

    def __getattribute__(self, __name: str):
        return object.__getattribute__(self, __name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value


point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)