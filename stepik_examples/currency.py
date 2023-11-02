class Currency:
    def __init__(self, value: int|float, currency: str):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f'{round(self.value, 2)} {self.currency}'
    
    def change_to(self, currency):
        __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1,  'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
        }
        res = 0
        for k, v in __RATE[self.currency].items():
            if k == currency:
                res = self.value * v
        self.currency = currency
        self.value = res

    def __add__(self, other):
        if other.currency == self.currency:
            return self.__class__(self.value + other.value, self.currency)
        else:
            other.change_to(self.currency)
            return self.__class__(self.value + other.value, self.currency)
    
    def __sub__(self, other):
        if other.currency == self.currency:
            return self.__class__(self.value - other.value, self.currency)
        else:
            other.change_to(self.currency)
            return self.__class__(self.value - other.value, self.currency)
    
    def __mul__(self, other):
        if other.currency == self.currency:
            return self.__class__(self.value * other.value, self.currency)
        else:
            other.change_to(self.currency)
            return self.__class__(self.value * other.value, self.currency)
    
    def __truediv__(self, other):
        if other.currency == self.currency:
            return self.__class__(self.value / other.value, self.currency)
        else:
            other.change_to(self.currency)
            return self.__class__(self.value / other.value, self.currency)



# tests

print()
print('TEST_1:')
money1 = Currency(10, 'EUR')
money2 = Currency(20, 'USD')
print(money1)
print(money2)

print()
print('TEST_2:')
money = Currency(10, 'EUR')

money.change_to('RUB')
print(money)

print()
print('TEST_3:')
print(Currency(5, 'EUR') + Currency(5, 'EUR'))
print(Currency(11, 'USD') - Currency(5, 'EUR'))
print(Currency(5, 'RUB') * Currency(11, 'USD'))
print(Currency(5, 'USD') / Currency(5, 'EUR'))

print()
print('TEST_4:')
money = Currency(100, 'USD')
print(money)

money.change_to('RUB')
print(money)

money.change_to('EUR')
print(money)

money.change_to('USD')
print(money)

print()
print('TEST_5:')
money = Currency(2000, 'RUB')
currencies = ['EUR', 'USD', 'RUB']
operation_funcs = ['__sub__', '__mul__', '__add__', '__truediv__']
operation_signs = ['-', '*', '+', '/']
currency = 0
operation = 0

values = [46, 54, 18, 81, 16, 86, 40, 82, 31, 74, 82, 39, 72, 40, 16, 72, 16, 24, 74, 30, 37, 87, 67, 95, 54, 79, 86,
          69, 44, 24, 92, 22, 80, 10, 46, 93, 10, 81, 43, 30, 12, 80, 99, 77, 89, 71, 55, 93, 77, 70, 26, 38, 16, 49,
          34, 33, 98, 22, 13, 79, 67, 99, 48, 97, 38, 96, 43, 72, 64, 74, 97, 52, 96, 86, 37, 36, 52, 63, 43, 13, 39,
          43, 52, 33, 92, 56, 17, 20, 94, 21, 28, 57, 96, 77, 99, 88, 38, 28, 70, 59]

for value in values:
    money.change_to(currencies[currency % 3])
    current_currency = currency % 3 - 1
    current_operation = operation % 4
    print(f'{money} {operation_signs[current_operation]} {value} {currencies[current_currency]} = ', end='')
    print(Currency.__dict__[operation_funcs[current_operation]](money, Currency(value, currencies[current_currency])))
    currency += 1
    operation += 1