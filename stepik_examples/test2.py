def roman_to_arabic(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
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

# Example usage:
roman_numeral = "XII"
arabic_numeral = roman_to_arabic(roman_numeral)
print(f"{roman_numeral} in Arabic numerals is {arabic_numeral}")



def arabic_to_roman(arabic):
    roman_dict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    
    roman_numeral = ""
    
    for value in sorted(roman_dict.keys(), reverse=True):
        while arabic >= value:
            roman_numeral += roman_dict[value]
            arabic -= value
    
    return roman_numeral

# Example usage:
arabic_numeral = 12
roman_numeral = arabic_to_roman(arabic_numeral)
print(f"{arabic_numeral} in Roman numerals is {roman_numeral}")
