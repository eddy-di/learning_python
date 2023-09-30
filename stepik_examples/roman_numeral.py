from functools import total_ordering

@ total_ordering
class RomanNumeral:
    def __init__(self, roman_num):
        self.number = roman_num

    def __str__(self):
        return self.number
    
    def __int__(self):
        return self.roman_to_arabic(self.number)
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.arabic_to_roman(self.roman_to_arabic(self.number) + self.roman_to_arabic(other.number)))
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.arabic_to_roman(self.roman_to_arabic(self.number) - self.roman_to_arabic(other.number)))
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.roman_to_arabic(self.number) == self.roman_to_arabic(other.number)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.roman_to_arabic(self.number) < self.roman_to_arabic(other.number)
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.roman_to_arabic(self.number) <= self.roman_to_arabic(other.number)
        return NotImplemented
    
    @staticmethod
    def roman_to_arabic(roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic = 0
        prev_value = 0
        for symbol in reversed(roman):
            value = roman_dict[symbol]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
            prev_value = value
        return arabic

    @staticmethod
    def arabic_to_roman(arabic):
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                    10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                    100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        roman_numeral = ""
        for value in sorted(roman_dict.keys(), reverse=True):
            while arabic >= value:
                roman_numeral += roman_dict[value]
                arabic -= value
        return roman_numeral


a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)