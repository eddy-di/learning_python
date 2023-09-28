class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'AnyClass: {", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()])}'

    def __repr__(self):
        return f'AnyClass({", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()])})'


attrs = {
    'name': 'Margaret Heafield Hamilton',
    'birth_date': '17.09.1936',
    'age': 86,
    'career': 'computer scientist'
}
obj = AnyClass(**attrs)
print(obj)

attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)

# print(obj.name)
# print(obj.birth_date)
# print(obj.age)
# print(obj.career)
