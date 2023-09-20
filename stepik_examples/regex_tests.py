import re

def is_fraction(string: str) -> bool:
    fraction_regex = '^-?\d+/(?!0*$)(\d*)$'
    return bool(re.match(fraction_regex, string))


inputs = ['1000/1', '-54/9', 
           '71', '1', 
           '1/0', '', 
           '/4', '1000', 
           '-987/1', '0/1', 
           '-/56', '1/1234', 
           '2-/4', '3/-7', 
           '5/8-', '--1/2', 
           '-7/3-', '-7-/-3-', 
           '/4/5', '4/5/', 
           '54365486548645/472342935648904709456', '5/2/4', 
           '5/2/4/2', '1000/10', 
           '1000/00001', '-1000/00001', 
           '1000/00004123', '1000/0000', '1000/00000008000']

fraction_regex = '^-?\d+/(?!0*$)(\d*)$'

outputs = []

for num in inputs:
    outputs.append(is_fraction(num))


print(outputs)