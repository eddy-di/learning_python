def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
    except Exception as error:
        error = 'Файл не найден'
        print(error) 


# tests

print('TEST_1:')
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.write('Сражения и путешествия берут своё')
    
print_file_content('Precepts_of_Zote.txt')

print('TEST_2:')
print_file_content('Precepts_of_Zote2.txt')

print('TEST_3:')
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    print('Сражения и путешествия берут своё', file=file)
    print('Во время отдыха твоё тело становится сильнее, а раны заживают', file=file)
    print('Чем больше отдыхаешь, тем сильнее становишься', file=file)
    
print_file_content('Precepts_of_Zote.txt')

print('TEST_4:')
print_file_content('missing_file.txt')

print('TEST_5:')
with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.writelines(
        ['Сражения и путешествия берут своё\n', 'Во время отдыха твоё тело становится сильнее, а раны заживают'])

print_file_content('Precepts_of_Zote.txt')