def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9

class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        if self._login != value:
            raise AttributeError('Изменение логина невозможно')
        self.login

    @property
    def password(self):
        return hash_function(self._password)
    
    @password.setter
    def password(self, new_password):
        self._password = new_password


account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)