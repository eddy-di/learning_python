class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            self.__dict__[attr] = value
    
    def __delattr__(self, attr):
        raise AttributeError('Удаление атрибута невозможно')




videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)
