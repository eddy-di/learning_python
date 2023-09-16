import random

digits = '0123456789'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_ '

pass_num = int(input('Сколько паролей надо сделать?\n'))
pass_length = int(input('Какую длину хошь?\n'))
include_digits = input('Включать ли цифры 0123456789? \'y\' = да \'n\' = нет:\n')
include_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? \'y\' = да \'n\' = нет:\n')
include_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? \'y\' = да \'n\' = нет:\n')
include_punct = input('А символы включать !#$%&*+-=?@^_? \'y\' = да \'n\' = нет:\n')
not_include_similar = input('Исключить ли неоднозначные символы il1Lo0O? \'y\' = да \'n\' = нет:\n')

chars = ''

if include_digits.lower() == 'y': 
    chars = chars + digits
if include_lower.lower() == 'y': 
    chars = chars + lower_case
if include_upper.lower() == 'y': 
    chars = chars + upper_case
if include_punct.lower() == 'y':
    chars = chars + punctuation
if not_include_similar.lower() == 'y':
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')

def generate_password(length, chars):
    length = pass_length
    chars = chars
    for i in range(pass_num):
        password = ''
        while len(password) < length:
            password += random.choice(chars)
        print(password)


generate_password(pass_length, chars)