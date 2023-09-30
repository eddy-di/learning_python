class SortKey:
    def __init__(self, *arguments):
        self.arguments = arguments

    def __call__(self, obj):
        return [getattr(obj, i) for i in self.arguments]
    

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

users.sort(key=SortKey('name'), reverse=True)
print(users)
users.sort(key=SortKey('name', 'age'), reverse=True)
print(users)
users.sort(key=SortKey('age'), reverse=True)
print(users)
users.sort(key=SortKey('age', 'name'), reverse=True)

