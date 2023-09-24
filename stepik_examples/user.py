class User:
    def __init__(self, name: str, age: int):
        if type(name) == str and len(name) > 0 and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        
        if age in range(0, 111):
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self, new_name: str):
        if type(new_name) == str and len(new_name) > 0 and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')
    
    def set_age(self, new_age: int):
        if new_age in range(0, 111):
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')
    

try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)
