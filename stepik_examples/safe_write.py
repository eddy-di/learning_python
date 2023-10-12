from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    flag = False
    with open('empty.txt', 'w') as testing_file:
        try:
            yield testing_file
            testing_file.close()
        except Exception as error:
            flag = True
            print(f'Во время записи в файл было возбуждено исключение {type(error).__name__}')
            testing_file.close()
    if flag:
        return filename
    else:
        f = open(filename, 'w')
        r = open('empty.txt', 'r')
        for line in r:
            f.write(line)
        r.close()
        f.close()
        return f

        





# tests

print('TEST_1:')
with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')
    
with open('undertale.txt') as file:
    print(file.read())

print('TEST_2:')
with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
    
with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())

print('TEST_3:')
with safe_write('poem.txt') as file:
    print('''Я кашлянул в звенящей тишине,
И от шального эха стало жутко…,
Расскажет ли утятам обо мне,
под утро мной испуганная утка?''', file=file)

with safe_write('poem.txt') as file:
    file.insert('Стихотворение про утку')       # неверный метод для записи в файл

with open('poem.txt') as file:
    print(file.read())