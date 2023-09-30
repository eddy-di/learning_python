class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.kwargs = self.__dict__.update(kwargs)

    def __getattribute__(self, __name):
        return object.__getattribute__(self, __name)
    
    def __getattr__(self, attr):
        if attr not in self.__dict__:
            return self.default
            


    
god = DefaultObject(name='Kratos', mythology='greek')
print('name' in god.__dict__)
print('mythology' in god.__dict__)


