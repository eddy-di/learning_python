class ProtectedObject:
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            object.__setattr__(self, attr, val)

    def __getattribute__(self, attr: str):
        if attr[0] == '_':
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, attr)
        
    def __getattr__(self, attr):
        if attr[0] == '_':
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, attr)
    
    def __setattr__(self, attr: str, __value) -> None:
        if attr[0] == '_':
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, attr, __value)

    def __delattr__(self, attr) -> None:
        if attr[0] == '_':
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, attr)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = 'PG'
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)

print(type(object.__getattribute__))